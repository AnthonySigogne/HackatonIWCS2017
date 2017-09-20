#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import cPickle
import requests
import html2text
from pattern.fr import parsetree, singularize
from pattern.search import search

# load relations
print "load relations..."
#relations = cPickle.load(open("relations/relations.pickled","rb"))
relations = {}

def submit_context(context) :
    url = "http://www.jeuxdemots.org/HACK/hack-submit.php"

    querystring = {"relations_text":context,"submitter":"anthony@byprog.com","mdp":"22w2MSsj","submit":"Soumettre"}

    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"url\"\r\n\r\nhttps://www.byprog.com\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'cache-control': "no-cache",
        }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

def singularize_text(text) :
    return " ".join([singularize(w) for w in text.split(" ")])

def compute_context(sentence, match) :
    min_left = match.group(1)[0].index-15 if match.group(1)[0].index-15 >= 0 else 0
    #left_context = " ".join([w.string for w in sentence[min_left:match.group(1)[0].index]])
    max_right = match.stop+15 if match.stop+15 <= len(sentence) else len(sentence)
    #right_context = " ".join([w.string for w in sentence[match.stop+1:max_right]])
    #return "%s %s %s"%(left_context, match.string, right_context)
    return " ".join([w.string for w in sentence[min_left:max_right]])

def write_context(f, mot1, rel, mot2, sentence, match) :
    f.write("%s;%s;%s;%s\n"%(mot1.string.encode("utf8"),rel.encode("utf8"),mot2.string.encode("utf8"),compute_context(sentence, match).encode("utf8")))

"""
sources = [
    "http://www.jeuxdemots.org/HACK/hack_texts/Au%20bonheur%20des%20dames_1%20-%20Wikisource.htm",
    "http://www.jeuxdemots.org/HACK/hack_texts/Germinal_Partie%20III_Chapitre%201%20-%20Wikisource.htm",
]
"""

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

fileList = [
    "Au_bonheur_des_dames_1_-_Wikisource.htm",
    "Au_bonheur_des_dames_10_-_Wikisource.htm",
    "Au_bonheur_des_dames_11_-_Wikisource.htm",
    "Au_bonheur_des_dames_12_-_Wikisource.htm",
    "Au_bonheur_des_dames_13_-_Wikisource.htm",
    "Au_bonheur_des_dames_14_-_Wikisource.htm",
    "Au_bonheur_des_dames_2_-_Wikisource.htm",
    "Au_bonheur_des_dames_3_-_Wikisource.htm",
    "Au_bonheur_des_dames_4_-_Wikisource.htm",
    "Au_bonheur_des_dames_5_-_Wikisource.htm",
    "Au_bonheur_des_dames_6_-_Wikisource.htm",
    "Au_bonheur_des_dames_7_-_Wikisource.htm",
    "Au_bonheur_des_dames_8_-_Wikisource.htm",
    "Au_bonheur_des_dames_9_-_Wikisource.htm",
    "Germinal_Partie_III_Chapitre_1_-_Wikisource.htm",
    "Germinal_Partie_III_Chapitre_2_-_Wikisource.htm",
    "Germinal_Partie_III_Chapitre_3_-_Wikisource.htm",
    "Germinal_Partie_III_Chapitre_4_-_Wikisource.htm",
    "Germinal_Partie_III_Chapitre_5_-_Wikisource.htm",
    "Germinal_Partie_II_Chapitre_1_-_Wikisource.htm",
    "Germinal_Partie_II_Chapitre_2_-_Wikisource.htm",
    "Germinal_Partie_II_Chapitre_3_-_Wikisource.htm",
    "Germinal_Partie_II_Chapitre_4_-_Wikisource.htm",
    "Germinal_Partie_II_Chapitre_5_-_Wikisource.htm",
    "Germinal_Partie_IV_Chapitre_1_-_Wikisource.htm",
    "Germinal_Partie_IV_Chapitre_2_-_Wikisource.htm",
    "Germinal_Partie_IV_Chapitre_3_-_Wikisource.htm",
    "Germinal_Partie_IV_Chapitre_4_-_Wikisource.htm",
    "Germinal_Partie_IV_Chapitre_5_-_Wikisource.htm",
    "Germinal_Partie_IV_Chapitre_6_-_Wikisource.htm",
    "Germinal_Partie_IV_Chapitre_7_-_Wikisource.htm",
    "Germinal_Partie_I_Chapitre_1_-_Wikisource.htm",
    "Germinal_Partie_I_Chapitre_2_-_Wikisource.htm",
    "Germinal_Partie_I_Chapitre_3_-_Wikisource.htm",
    "Germinal_Partie_I_Chapitre_4_-_Wikisource.htm",
    "Germinal_Partie_I_Chapitre_5_-_Wikisource.htm",
    "Germinal_Partie_I_Chapitre_6_-_Wikisource.htm",
    "Germinal_Partie_VII_Chapitre_1_-_Wikisource.htm",
    "Germinal_Partie_VII_Chapitre_2_-_Wikisource.htm",
    "Germinal_Partie_VII_Chapitre_3_-_Wikisource.htm",
    "Germinal_Partie_VII_Chapitre_4_-_Wikisource.htm",
    "Germinal_Partie_VII_Chapitre_5_-_Wikisource.htm",
    "Germinal_Partie_VII_Chapitre_6_-_Wikisource.htm",
    "Germinal_Partie_VI_Chapitre_1_-_Wikisource.htm",
    "Germinal_Partie_VI_Chapitre_2_-_Wikisource.htm",
    "Germinal_Partie_VI_Chapitre_3_-_Wikisource.htm",
    "Germinal_Partie_VI_Chapitre_4_-_Wikisource.htm",
    "Germinal_Partie_VI_Chapitre_5_-_Wikisource.htm",
    "Germinal_Partie_V_Chapitre_1_-_Wikisource.htm",
    "Germinal_Partie_V_Chapitre_2_-_Wikisource.htm",
    "Germinal_Partie_V_Chapitre_3_-_Wikisource.htm",
    "Germinal_Partie_V_Chapitre_4_-_Wikisource.htm",
    "Germinal_Partie_V_Chapitre_5_-_Wikisource.htm",
    "Germinal_Partie_V_Chapitre_6_-_Wikisource.htm",
    "La_Bete_humaine_I_-_Wikisource.htm",
    "La_Bete_humaine_II_-_Wikisource.htm",
    "La_Bete_humaine_III_-_Wikisource.htm",
    "La_Bete_humaine_IV_-_Wikisource.htm",
    "La_Bete_humaine_IX_-_Wikisource.htm",
    "La_Bete_humaine_V_-_Wikisource.htm",
    "La_Bete_humaine_VI_-_Wikisource.htm",
    "La_Bete_humaine_VII_-_Wikisource.htm",
    "La_Bete_humaine_VIII_-_Wikisource.htm",
    "La_Bete_humaine_X_-_Wikisource.htm",
    "La_Bete_humaine_XI_-_Wikisource.htm",
    "La_Bete_humaine_XII_-_Wikisource.htm",
    "La_Curee_I_-_Wikisource.htm",
    "La_Curee_II_-_Wikisource.htm",
    "La_Curee_III_-_Wikisource.htm",
    "La_Curee_IV_-_Wikisource.htm",
    "La_Curee_V_-_Wikisource.htm",
    "La_Curee_VI_-_Wikisource.htm",
    "La_Curee_VII_-_Wikisource.htm",
    "La_Fortune_des_Rougon_I_-_Wikisource.htm",
    "La_Fortune_des_Rougon_II_-_Wikisource.htm",
    "La_Fortune_des_Rougon_III_-_Wikisource.htm",
    "La_Fortune_des_Rougon_IV_-_Wikisource.htm",
    "La_Fortune_des_Rougon_V_-_Wikisource.htm",
    "La_Fortune_des_Rougon_VI_-_Wikisource.htm",
    "La_Fortune_des_Rougon_VII_-_Wikisource.htm",
    "Le_Ventre_de_Paris_I_-_Wikisource.htm",
    "Le_Ventre_de_Paris_II_-_Wikisource.htm",
    "Le_Ventre_de_Paris_III_-_Wikisource.htm",
    "Le_Ventre_de_Paris_IV_-_Wikisource.htm",
    "Le_Ventre_de_Paris_V_-_Wikisource.htm",
    "Le_Ventre_de_Paris_VI_-_Wikisource.htm",
    "Nana_Chapitre_1_-_Wikisource.htm",
    "Nana_Chapitre_10_-_Wikisource.htm",
    "Nana_Chapitre_11_-_Wikisource.htm",
    "Nana_Chapitre_12_-_Wikisource.htm",
    "Nana_Chapitre_13_-_Wikisource.htm",
    "Nana_Chapitre_14_-_Wikisource.htm",
    "Nana_Chapitre_2_-_Wikisource.htm",
    "Nana_Chapitre_3_-_Wikisource.htm",
    "Nana_Chapitre_4_-_Wikisource.htm",
    "Nana_Chapitre_5_-_Wikisource.htm",
    "Nana_Chapitre_6_-_Wikisource.htm",
    "Nana_Chapitre_7_-_Wikisource.htm",
    "Nana_Chapitre_8_-_Wikisource.htm",
    "Nana_Chapitre_9_-_Wikisource.htm"
]

folder = os.path.abspath(os.path.dirname(sys.argv[0]))

with open("output.txt", "w") as f :
    print "analyse sources..."
    for file in fileList:
        file = os.path.join(os.path.join(folder,"100files"),file)
        print "analyse source : "+file
        """
        # crawl
        response = requests.get(url)
        h = html2text.HTML2Text()
        try :
            text = h.handle(response.content.decode("utf8"))
        except :
            text = h.handle(response.content.decode("latin1"))
        """
        with open(file) as textfile :
            text = textfile.read()
        # parse
        text = parsetree(text, relations=True, lemmata=True)

        for sentence in text :
            # A + N
            for match in search(u'{JJ|RB} {NN|NNS|NNP}', sentence) :
                rel = relations.get(match.string, relations.get(singularize_text(match.string), False))
                print(0, match.string, rel)
                if rel :
                    write_context(f, match.group(2), rel, match.group(1), sentence, match)

            # N + A
            motifs = [
                u'{NN|NNS|NNP} PP? {JJ|RB|VBN} !NN|!NNS|!NNP',
                u'{NN|NNS|NNP} PP? {JJ|RB|VBN} et {JJ|RB|VBN} !NN|!NNS|!NNP',
                u'{NN|NNS|NNP} PP? {JJ|RB|VBN} , {JJ|RB|VBN} et {JJ|RB|VBN} !NN|!NNS|!NNP',
                u'{NN|NNS|NNP} PP? {JJ|RB|VBN} , {JJ|RB|VBN} , {JJ|RB|VBN} !NN|!NNS|!NNP'
            ]
            for motif in motifs :
                for match in search(motif, sentence) :
                    for i in range(2, 4) :
                        try :
                            candidate = "%s %s"%(match.group(1).string, match.group(i).string)
                            rel = relations.get(candidate, relations.get(singularize_text(candidate), False))
                            print(1, match.string, candidate, rel)
                            if rel and rel not in ["r_has_patient", "r_has_agent"]:
                                write_context(f, match.group(1), rel, match.group(i), sentence, match)
                        except :
                            pass

            # N-part de N
            for match in search(u'{NN|NNS|NNP} IN DT? {NN|NNS|NNP}', sentence) :
                candidate = "%s %s"%(match.group(2).string, match.group(1).string)
                rel = relations.get(candidate, relations.get(singularize_text(candidate), False))
                print(2, match.string, candidate, "r_has_part")
                if rel :
                    write_context(f, match.group(2), "r_has_part", match.group(1), sentence, match)

            # agent + V
            motifs = [
                u'{NN|NNS|NNP} VB RB? {VBN}',
                u'{NN|NNS|NNP} {VB} RB? !VBN'
            ]
            for motif in motifs :
                for match in search(motif, sentence) :
                    candidate = "%s %s"%(match.group(1).string, match.group(2).string)
                    rel = relations.get(candidate, relations.get(singularize_text(candidate), False))
                    print(3, match.string, candidate, "r_has_agent")
                    if rel :
                        write_context(f, match.group(2), "r_has_agent", match.group(1), sentence, match)

            # V + patient
            for match in search(u'VB? {VB|VBN} DT|PRP$|PRP JJ|RB? {NN|NNS|NNP}', sentence) :
                candidate = "%s %s"%(match.group(2).string, match.group(1).string)
                rel = relations.get(candidate, relations.get(singularize_text(candidate), False))
                print(4, match.string, candidate, "r_has_patient")
                if rel :
                    write_context(f, match.group(1), "r_has_patient", match.group(2), sentence, match)

            """
            # V + instrument
            motifs = [
                u'VB {VBN} NP? avec|par DT|PRP$|PRP JJ|RB? {NN|NNS|NNP}',
                u'{VB} NP? avec|par DT|PRP$|PRP JJ|RB? {NN|NNS|NNP}'
            ]
            for motif in motifs :
                for match in search(motif, sentence) :
                    candidate = "%s %s"%(match.group(2).string, match.group(1).string)
                    rel = relations.get(candidate, relations.get(singularize_text(candidate), False))
                    #print(match.string, candidate, rel)
                    if rel :
                        #print "%s;%s;%s;%s"%(match.group(2).string,rel,match.group(1).string,sentence.string)
                        pass
            """
