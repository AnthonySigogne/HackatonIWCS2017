urlencodepipe() {
  local LANG=C; local c; while IFS= read -r c; do
    case $c in [a-zA-Z0-9.~_-]) printf "$c"; continue ;; esac
    printf "$c" | od -An -tx1 | tr ' ' % | tr -d '\n'
  done <<EOF
$(fold -w1)
EOF
  echo
}

urlencode() { printf "$*" | urlencodepipe ;}

while read p; do
  echo $p
  x=`python2 -c "import urllib;print urllib.quote(raw_input())" <<< "$p"`
  curl -X GET "http://www.jeuxdemots.org/HACK/hack-submit.php?relations_text=${x}&submitter=test@lirmm.fr&mdp=TEST&submit=Soumettre"
done < $1
