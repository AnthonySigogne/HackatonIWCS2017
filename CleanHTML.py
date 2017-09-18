#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import html2text
from pattern.fr import parsetree

sources = [
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
"http://www.jeuxdemots.org/HACK/hack_texts/La%20Bête%20humaine_I%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20Bête%20humaine_II%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20Bête%20humaine_III%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20Bête%20humaine_IV%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20Bête%20humaine_IX%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20Bête%20humaine_V%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20Bête%20humaine_VI%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20Bête%20humaine_VII%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20Bête%20humaine_VIII%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20Bête%20humaine_X%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20Bête%20humaine_XI%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20Bête%20humaine_XII%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20Curée_I%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20Curée_II%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20Curée_III%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20Curée_IV%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20Curée_V%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20Curée_VI%20-%20Wikisource.htm",
"http://www.jeuxdemots.org/HACK/hack_texts/La%20Curée_VII%20-%20Wikisource.htm",
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

for url in sources :
    print("=== Analyzing text: "+url+"===")
    
    # crawl
    response = requests.get(url)
    h = html2text.HTML2Text()
    text = h.handle(response.content.decode("utf8"))

    # parse
    text = parsetree(text, relations=True, lemmata=True)
    for sentence in text :
        for chunk in sentence.chunks :
            for word in chunk.words :
                print(word.string+"¤"+word.lemma+"¤"+word.tag)


