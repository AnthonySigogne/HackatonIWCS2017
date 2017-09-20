while read p; do
  echo $p
  x=`python2 -c "import urllib;print urllib.quote(raw_input())" <<< "$p"`
  curl -X GET "http://www.jeuxdemots.org/HACK/hack-submit.php?relations_text=${x}&submitter=test@lirmm.fr&mdp=TEST&submit=Soumettre"
done < $1
