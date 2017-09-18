#!/usr/sfw/bin/python
# -*- coding: utf-8 -*-

import glob, os, re, sys, urllib.request

letters = {}
letters["a"] = 1
letters["b"] = 1
letters["c"] = 1
letters["d"] = 1
letters["e"] = 1
letters["f"] = 1
letters["g"] = 1
letters["h"] = 1
letters["i"] = 1
letters["j"] = 1
letters["k"] = 1
letters["l"] = 1
letters["m"] = 1
letters["n"] = 1
letters["o"] = 1
letters["p"] = 1
letters["q"] = 1
letters["r"] = 1
letters["s"] = 1
letters["t"] = 1
letters["u"] = 1
letters["v"] = 1
letters["w"] = 1
letters["x"] = 1
letters["y"] = 1
letters["z"] = 1

replacements = {}
replacements["æ"] = "ae"
replacements["à"] = "a"
replacements["á"] = "a"
replacements["á"] = "a"
replacements["ã"] = "a"
replacements["ä"] = "a"
replacements["â"] = "a"
replacements["ç"] = "c"
replacements["é"] = "e"
replacements["è"] = "e"
replacements["ë"] = "e"
replacements["ê"] = "e"
replacements["ï"] = "i"
replacements["î"] = "i"
replacements["ì"] = "i"
replacements["ñ"] = "n"
replacements["ô"] = "o"
replacements["ö"] = "o"
replacements["ó"] = "o"
replacements["œ"] = "oe"
replacements["ü"] = "u"
replacements["ù"] = "u"
replacements["ú"] = "u"

def removeAccent(word, replacements):
    for letter in replacements:
        word = word.replace(letter, replacements[letter])
    print("!!!!!"+word)
    return word

"""
"http://www.jeuxdemots.org/HACK/hack_texts/Au%20bonheur%20des%20dames_1%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Au%20bonheur%20des%20dames_10%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Au%20bonheur%20des%20dames_11%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Au%20bonheur%20des%20dames_12%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Au%20bonheur%20des%20dames_13%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Au%20bonheur%20des%20dames_14%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Au%20bonheur%20des%20dames_2%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Au%20bonheur%20des%20dames_3%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Au%20bonheur%20des%20dames_4%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Au%20bonheur%20des%20dames_5%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Au%20bonheur%20des%20dames_6%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Au%20bonheur%20des%20dames_7%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Au%20bonheur%20des%20dames_8%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Au%20bonheur%20des%20dames_9%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Germinal_Partie%20III_Chapitre%201%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Germinal_Partie%20III_Chapitre%202%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Germinal_Partie%20III_Chapitre%203%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Germinal_Partie%20III_Chapitre%204%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Germinal_Partie%20III_Chapitre%205%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Germinal_Partie%20II_Chapitre%201%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Germinal_Partie%20II_Chapitre%202%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Germinal_Partie%20II_Chapitre%203%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Germinal_Partie%20II_Chapitre%204%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Germinal_Partie%20II_Chapitre%205%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Germinal_Partie%20IV_Chapitre%201%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Germinal_Partie%20IV_Chapitre%202%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Germinal_Partie%20IV_Chapitre%203%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Germinal_Partie%20IV_Chapitre%204%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Germinal_Partie%20IV_Chapitre%205%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Germinal_Partie%20IV_Chapitre%206%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Germinal_Partie%20IV_Chapitre%207%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Germinal_Partie%20I_Chapitre%201%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Germinal_Partie%20I_Chapitre%202%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Germinal_Partie%20I_Chapitre%203%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Germinal_Partie%20I_Chapitre%204%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Germinal_Partie%20I_Chapitre%205%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Germinal_Partie%20I_Chapitre%206%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Germinal_Partie%20VII_Chapitre%201%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Germinal_Partie%20VII_Chapitre%202%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Germinal_Partie%20VII_Chapitre%203%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Germinal_Partie%20VII_Chapitre%204%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Germinal_Partie%20VII_Chapitre%205%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Germinal_Partie%20VII_Chapitre%206%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Germinal_Partie%20VI_Chapitre%201%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Germinal_Partie%20VI_Chapitre%202%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Germinal_Partie%20VI_Chapitre%203%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Germinal_Partie%20VI_Chapitre%204%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Germinal_Partie%20VI_Chapitre%205%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Germinal_Partie%20V_Chapitre%201%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Germinal_Partie%20V_Chapitre%202%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Germinal_Partie%20V_Chapitre%203%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Germinal_Partie%20V_Chapitre%204%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Germinal_Partie%20V_Chapitre%205%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Germinal_Partie%20V_Chapitre%206%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20B%EAte%20humaine_I%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20B%EAte%20humaine_II%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20B%EAte%20humaine_III%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20B%EAte%20humaine_IV%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20B%EAte%20humaine_IX%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20B%EAte%20humaine_V%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20B%EAte%20humaine_VI%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20B%EAte%20humaine_VII%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20B%EAte%20humaine_VIII%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20B%EAte%20humaine_X%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20B%EAte%20humaine_XI%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20B%EAte%20humaine_XII%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20Cur%E9e_I%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20Cur%E9e_II%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20Cur%E9e_III%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20Cur%E9e_IV%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20Cur%E9e_V%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20Cur%E9e_VI%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20Cur%E9e_VII%20-%20Wikisource.htm",
"""
allUrl = [
"http://www.jeuxdemots.org/HACK/hack_texts/La%20Fortune%20des%20Rougon_I%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20Fortune%20des%20Rougon_II%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20Fortune%20des%20Rougon_III%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20Fortune%20des%20Rougon_IV%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20Fortune%20des%20Rougon_V%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20Fortune%20des%20Rougon_VI%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20Fortune%20des%20Rougon_VII%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Le%20Ventre%20de%20Paris_I%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Le%20Ventre%20de%20Paris_II%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Le%20Ventre%20de%20Paris_III%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Le%20Ventre%20de%20Paris_IV%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Le%20Ventre%20de%20Paris_V%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Le%20Ventre%20de%20Paris_VI%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Nana_Chapitre%201%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Nana_Chapitre%2010%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Nana_Chapitre%2011%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Nana_Chapitre%2012%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Nana_Chapitre%2013%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Nana_Chapitre%2014%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Nana_Chapitre%202%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Nana_Chapitre%203%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Nana_Chapitre%204%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Nana_Chapitre%205%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Nana_Chapitre%206%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Nana_Chapitre%207%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Nana_Chapitre%208%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/Nana_Chapitre%209%20-%20Wikisource.htm"
]

for url in allUrl:
   res = re.search(".*[/]([^/]*)$",url)
   if res:
      print(res.group(1))
      # Récupère la page de résultats Gallica en l'enregistrant dans le même dossier
      site = urllib.request.urlopen(url)
      data = site.read()
      print(removeAccent(res.group(1).replace("%20","_"),replacements))   
      file = open(removeAccent(res.group(1).replace("%20","_"),replacements), "wb")
      file.write(data)
      file.close()
