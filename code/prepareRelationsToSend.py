#!/usr/sfw/bin/python
# -*- coding: utf-8 -*-

import glob, os, re, sys, urllib.request



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
    #print("!!!!!"+word)
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

"""
given a list with n element and an index index,
return the n-gram containing all cells from index+1 to index
"""
def buildNgram(rotatingNgram, index):
    ngram = ""
    for i in range(0,len(rotatingNgram)):
        if i>0:
            ngram += " "
        ngram += rotatingNgram[(index+i+1)%len(rotatingNgram)]
    return ngram

"""
prepare the output context with size between 50 and 200 characters
matching exactly the input text, using the ngram for the search
and extending it left or right.
"""
def outputSentence(ngram, ngramSize, wordList, ngramPositionInWordlist, ngrams, text, previousWords, nextWords, previousTokens, nextTokens, firstWord, secondWord):
    # filter possible positions of the ngram using the left context, trying x words on the left
    # until there is only 1 candidate
    
    # if the ngram is only a bigram, we include the previous word (only useful if the ngram is supposed to be a trigram
    res = re.search("^"+firstWord,ngram)
    if not(res):
        #print("only a bigram: "+ngram)
        ngramPositionInWordlist += 1       
    
    currentPosition = ngramPositionInWordlist
    positionsInText = ngrams[ngram]
    nbCandidates = len(positionsInText)
    currentPositionsInText = []
    
    for positionInText in positionsInText:
        currentPositionsInText.append(positionInText)
    
    #print(str(nbCandidates)+" candidats")
    #for currentPositionInText in currentPositionsInText:
    #    print(text[currentPositionInText][1] + "=!!!!=" + wordList[ngramPositionInWordlist] + "?" + ngram)
  
    while (currentPosition > 0 and nbCandidates >1):
        currentPosition = currentPosition - 1
        positionNumber = 0
        wordOk = ""            
        for currentPositionInText in currentPositionsInText:
            if currentPositionInText>-1:
                #print("p"+str(positionNumber)+":"+text[previousWords[currentPositionInText]][1] + "==" + wordList[currentPosition] + "? ..." +ngram)
                if text[previousWords[currentPositionInText]][1] == wordList[currentPosition]:
                    currentPositionsInText[positionNumber] = previousWords[currentPositionInText]
                    wordOk = wordList[currentPosition]
                else :
                    currentPositionsInText[positionNumber] = -1
                    nbCandidates -= 1
            positionNumber += 1
        ngram = wordOk + " " + ngram
    foundPosition = -1
    
    positionNumber = 0
    for currentPositionInText in currentPositionsInText:
        if currentPositionInText > -1:
            foundPosition = positionNumber
            positionNumber += 1
    
    # now we should have only one candidate
    # we are ready to compute the context
    context = ""
    #context = str(len(positionsInText)) + str(nbCandidates) + text[foundPosition][1] + " " + text[nextWords[foundPosition]][1] + " " + text[nextWords[nextWords[foundPosition]]][1]
    #context = str(nbCandidates)
    if foundPosition > -1:
       
       previousString = "" 
       foundPunctuationOnTheLeft = False
       foundPunctuationOnTheRight = False
       foundNgram = False
       positionInWordList = ngramPositionInWordlist
       positionInText = positionsInText[foundPosition]
       firstPositionInText = positionInText
       #print("found position of " + ngram + ": " + str(positionInText))
       
       while len(context)<185 and (not(foundPunctuationOnTheLeft) or not(foundPunctuationOnTheRight) or not(foundNgram)):
           previousString = context
           #print(str(positionInText) + " : " + context + str(foundNgram) + str(foundPunctuationOnTheLeft) + str(foundPunctuationOnTheRight) + str(not(foundPunctuationOnTheLeft) or not(foundPunctuationOnTheRight) or not(foundNgram)))
           # first we compute the context corresponding to the ngram    
           if not(foundNgram):  
               #print("looking for ngram")             
               context += text[positionInText][1]
               if text[positionInText][1]==secondWord:
                   foundNgram = True
               positionInText = nextTokens[positionInText]
           else:
               if not(foundPunctuationOnTheLeft):
                   #print("extending to the left")
                   # if the word on the left is not punctuation, we add it
                   res = re.search(";",text[positionInText][1])
                   if res:
                       foundPunctuationOnTheLeft = True
                   else :
                       firstPositionInText = previousTokens[firstPositionInText]                   
                       if text[firstPositionInText][0] == -1:
                           foundPunctuationOnTheLeft = True
                       else :
                           context = text[firstPositionInText][1] + context

               # if we didn't reach 200 characters, we add the word on the right
               if len(context)<185 and not(foundPunctuationOnTheRight):
                   #print("extending to the right")
                   res = re.search(";",text[positionInText][1])
                   if res:
                       foundPunctuationOnTheRight = True
                   else :
                       context += text[positionInText][1]
                       if text[positionInText][0] == -1:
                           if len(context)>49:
                               foundPunctuationOnTheRight = True
                           else:
                               foundPunctuationOnTheRight = False
                   positionInText = nextTokens[positionInText]                   
                   
       if len(context)>185:
           context = previousString
       
    return context


# store in the folder variable the address of the folder containing this program
folder = os.path.abspath(os.path.dirname(sys.argv[0]))
carNumber = 0
wordNb = 0
previousWords = {}
nextWords = {}
previousTokens = {}
nextTokens = {}
previousWord = -1
previousToken = -1
text = {}
ngramSize = 3
# this dictionary associates, to each ngram of size ngramSize, the list of positions of the ngram in the text
ngrams = {}
c = []
rotatingNgramIndex = 0
rotatingNgram = []
rotatingNgramLocation = []


# Consider all texts in the data folder to create an index of all their 4-grams
for file in fileList:
    file = os.path.join(os.path.join(folder,"100files"),file)
    # Display the address of the file being treated
    print("Currently extacting words from file "+file)
    
    # in this file we will put one sentence per line, coding each token (either word or sequence of punctuation and HTML tags) by its location (character nb), its type and the corresponding string
    
    # in this file we will put one sentence per line, in order to have something which is ready to treat by TreeTagger
    for line in open(file,"r",encoding="utf8"):
        #print(line)
        res = re.search("^<p>(.*)</p>$",line)
        if res:
            line = res.group(1)
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
                   text[carNumber] = newToken
                   previousTokens[carNumber] = previousToken
                   nextTokens[previousToken] = carNumber
                   previousToken = carNumber
                   #print(punct)
               
                   # check if a sentence has just ended
                   res = re.search("[.!?;]", punct)
                   if res:
                      # we put -1 to say that this is the end of a sentence
                      text[carNumber][0] = -1
                
                # add the found word
                if len(word)>0:                   
                   newToken = []
                   newToken.append(1)               
                   newToken.append(word)
                   location = carNumber+len(punct)
                   previousWords[location] = previousWord
                   nextWords[previousWord] = location
                   previousWord = location
                   previousTokens[location] = previousToken
                   nextTokens[previousToken] = location
                   previousToken = location
                   text[location] = newToken
                   
                   if wordNb > ngramSize-1:
                       if wordNb == ngramSize-1:
                           rotatingNgram.append(word)
                           rotatingNgramLocation.append(location)
                       else :
                           rotatingNgram[rotatingNgramIndex] = word
                           rotatingNgramLocation[rotatingNgramIndex] = location
                       ngram = buildNgram(rotatingNgram,rotatingNgramIndex)
                       if ngram not in ngrams:
                           ngrams[ngram] = []
                       ngrams[ngram].append(rotatingNgramLocation[(rotatingNgramIndex+1)%len(rotatingNgram)])
                       #print(str(location)+" : "+ngram)
                   else :
                       rotatingNgram.append(word)
                       rotatingNgramLocation.append(location)
                   
                   wordNb += 1
                   rotatingNgramIndex = (rotatingNgramIndex + 1) % ngramSize
                       
                   #print(word)
                   
                # update the line and the character number
                carNumber += len(punct)+len(word)
                line = splitNextWord[2]
                


# Open the list of relations and find the real contexts
triplets = {}
output = open(os.path.join(folder,"foundRelations.corrected.txt"),"w",encoding="utf8")

for line in open(os.path.join(folder,"foundRelations.txt"),"r",encoding="utf8"):
    # ignore the line if it contains "wiki"
    res = re.search("^.*wiki.*$", line)
    if not res :
        res = re.search("^([^;]+);([^;]+);([^;]+);(.+)$", line)
        if res:
            word1 = res.group(1)
            firstWord = word1
            relType = res.group(2)
            word2 = res.group(3)
            secondWord = word2
            badContext = res.group(4)
            triplet = word1+";"+relType+";"+word2
            
            #build the ngram starting with the left-most word among word1 and word2
            ngram = ""
            ngramPositionInWordlist = 0
            wordList = []
            rotatingNgramIndex = 0
            rotatingNgram = []
            stop = False
            countdown = -1
            wordCount = 0
            foundNgram = False
            while not(stop) and len(badContext)>0:
                next = nextWord(badContext)
                if len(next[0])>0:
                    #we found the next word, let's build the next nGram
                    word = next[0]
                    wordList.append(word)
                    wordCount += 1
                    if not(foundNgram) and (word == word1 or word == word2):
                        if word == word2:
                           firstWord = word2
                           secondWord = word1
                        countdown = ngramSize
                        ngramPositionInWordlist = wordCount-1
                        foundNgram = True
                        #print(word1+"|"+word2+"||"+str(wordCount)+"|||"+wordList[ngramPositionInWordlist])
                    if wordCount < ngramSize + 1:
                        rotatingNgram.append(word)
                    else:
                        rotatingNgram[rotatingNgramIndex] = word
                    if countdown > 0:
                        ngram = buildNgram(rotatingNgram,rotatingNgramIndex)
                        countdown -= 1
                    if countdown == 0:
                        ngram = buildNgram(rotatingNgram,rotatingNgramIndex)
                        countdown = -1
                        #stop = True
                    rotatingNgramIndex = (rotatingNgramIndex+1) % ngramSize
                badContext = next[2]                
            if ngram in ngrams and not triplet in triplets:
                triplets[triplet] = 1
                #print("|"+ngram+"||"+wordList[ngramPositionInWordlist]+"||||"+str(wordList))
                output.writelines(word1+";"+relType+";"+word2+";"+outputSentence(ngram, ngramSize, wordList, ngramPositionInWordlist - (countdown+1), ngrams, text, previousWords, nextWords, previousTokens, nextTokens, firstWord, secondWord)+"\n")
            #else:
            #    output.writelines("!!!!!!!!!!!!!!!!!!!!!!!!!!!"+" not found "+ngram+"\n")
            #    print("not found "+ngram)
output.close()