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
return a table containing the first word of the input string as the first element
what precedes in the second element and what follows in the third element
"""
def nextWord(string):
   result = []
   string = string.replace("\n","¤").replace("[","|").replace("]","|").replace("{","|").replace("}","|")
   ponctuation = " _/?.,;:!’…¨«»+=()°*&\[\] '\-—\"\r\n	"
   #res = re.search("^(["+ponctuation+"]*)([^"+ponctuation+"]+)(["+ponctuation+"]*[^\r\n]*)[\r\n]*$",string)
   res = re.search("^((["+ponctuation+"]|<[^>]+>)*)([^<>"+ponctuation+"]+)(.*)$", string)
   if res:
      result.append(res.group(3))
      result.append(res.group(1))
      result.append(res.group(4))
   else:
      result.append("")
      result.append(string)
      result.append("")
   return result

# store in the folder variable the address of the folder containing this program
folder = os.path.abspath(os.path.dirname(sys.argv[0]))

# Consider all texts in the data folder
for file in glob.glob(folder+"\\100files\\*.htm"):
    # Display the address of the file being treated
    print("Currently extacting words from file "+file)
    carNumber = 0
    sentences = []
    
    # in this file we will put one sentence per line, coding each token (either word or sequence of punctuation and HTML tags) by its location (character nb), its type and the corresponding string
    outputFile = open(file+".sentences.txt","w",encoding="utf8")
    
    # in this file we will put one sentence per line, in order to have something which is ready to treat by TreeTagger
    outputCleanFile = open(file+".clean.txt","w",encoding="utf8")
    for line in open(file,"r",encoding="utf8"):
        #print(line)
        res = re.search("^<p>(.*)</p>$",line)
        if res:
            line = res.group(1)
            sentence = {}
            while len(line) > 0:
                # split the line in punctuation followed by word followed by punctuation
                splitNextWord = nextWord(line)
                punct = splitNextWord[1]
                word = splitNextWord[0]
            
                # add the found punctuation
                if len(punct)>0:
                   newToken = []
                   newToken.append(0)
                   newToken.append(punct)
                   sentence[carNumber] = newToken
                   #print(punct)
               
                # check if a sentence has just ended
                res = re.search("[.!?;]", punct)
                if res:
                   sentences.append(sentence)
                   sentence = {}
                
                # add the found word
                if len(word)>0:
                   newToken = []
                   newToken.append(1)               
                   newToken.append(word)
                   sentence[carNumber+len(punct)] = newToken
                   #print(word)
                   
                # update the line and the character number
                carNumber += len(punct)+len(word)
                line = splitNextWord[2]
            sentences.append(sentence)
    
    # save sentences
    for sentence in sentences:
        tokenNb = 0
        noWordYet = True
        previousTokenPunctuation = True
        for token in sentence:
            if tokenNb > 0:
                outputFile.writelines(",")
            if sentence[token][1] == "'" or sentence[token][1] == "’" or sentence[token][1] == "-" or sentence[token][1] == ", ":
                outputCleanFile.writelines(sentence[token][1])
                previousTokenPunctuation = True
            else:
                if not previousTokenPunctuation:                
                    if sentence[token][0] == 1:
                        if not noWordYet:
                            outputCleanFile.writelines(" ")
                else:
                    previousTokenPunctuation = False

            if sentence[token][0] == 1:
                outputCleanFile.writelines(sentence[token][1])
                noWordYet = False

            outputFile.writelines(str(token) + ":[" + str(sentence[token][0]) + "," + sentence[token][1] + "]")
            tokenNb += 1

        outputFile.writelines("\n")
        outputCleanFile.writelines("\n")