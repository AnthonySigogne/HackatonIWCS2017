#!/usr/sfw/bin/python
# -*- coding: utf-8 -*-
#C:\python27\python.exe C:\Dropbox\Work\2012ExpressionsComposees\CreateGraph.py

import sys, os, re, string, time
from math import *

#------------------------------
# Chargement des paramètres
#------------------------------
args={}
i=1;

selectedRelations = {}
selectedRelations[6] = "r_isa"
selectedRelations[9] = "r_has_part"
selectedRelations[16] = "r_instr"
selectedRelations[17] = "r_carac"
selectedRelations[23] = "r_carac-1"
selectedRelations[15] = "r_lieu"
selectedRelations[24] = "r_agent-1"
selectedRelations[26] = "r_patient-1"
selectedRelations[41] = "r_conseq" 
selectedRelations[53] = "r_make"

inputFolder = os.path.abspath(os.path.dirname(sys.argv[0]))

# Addess of the tagged text containing (almost) all text files of the Hackathon:
inputTaggedTexts = inputFolder + "\\tagged.txt"

# Address of the JeuxDeMots data file
# huge one :
#inputJeuxDeMots = inputFolder + "\\09032017-LEXICALNET-JEUXDEMOTS-FR-NOHTML.txt";
# big one :
#inputJeuxDeMots = inputFolder + "\\06252017-LEXICALNET-JEUXDEMOTS-FR-NOHTML.txt";
# small one :
inputJeuxDeMots = inputFolder + "\\08152011-LEXICALNET-JEUXDEMOTS-FR-NOHTML.txt";

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
    return word

def readFile(inputJeuxDeMots, inputFolder, inputTaggedTexts, replacements, letters):

    allWords = {}
    i = 0

    # Associate all word indices with words in a dictionary
    try :
        for line in open(inputJeuxDeMots,"r"):
            if i % 1000 == 0:
                print("ligne "+str(i))
            i+=1
            # only take words with t=1 (real words)
            res = re.search("eid=([0-9]*).n=.(.+)..t=1.w=([0-9]*).*",line)
            if res:            
                id = res.group(1)
                word = res.group(2)
                # only take words whose first character is a letter
                firstLetter = word[0].lower()
                weight = int(res.group(3))
                if firstLetter in letters or firstLetter in replacements:
                    allWords[id] = word
    except ValueError:
        print(str(ValueError))
        pass

    
    # Create a dictionary of the neighborhoods of all words according to the relations in selectedRelations
    if 0 == 0:
            i = 0
            nbRelations = 0
            neighbors = {}
            
            for line in open(inputJeuxDeMots,"r"):
                if i % 1000 == 0:
                    print("ligne "+str(i))
                i+=1
                # extract the edges of the graph, including type and weight
                res = re.search("rid=([0-9]*).n1=([0-9]*).n2=([0-9]*).t=([0-9]*).w=([0-9]+).*",line)
                if res:     
                    try :
                        id1 = res.group(2)
                        id2 = res.group(3)
                        type = int(res.group(4))
                        weight = int(res.group(5))
                        edgeInfo = []
                        edgeInfo.append(type)
                        edgeInfo.append(weight)
                        # if the relation has positive weight, is of one of the expected types
                        # and links two indexed words, we memorize it by saving its weight and type in a dict of dict
                        if (weight>0) and (type in selectedRelations) and (id1 in allWords) and (id2 in allWords):
                            firstWord = allWords[id1]
                            secondWord = allWords[id2]
                            if firstWord not in neighbors:
                                neighbors[firstWord] = {}
                            neighbors[firstWord][secondWord] = edgeInfo
                            nbRelations += 1
                            #print(str(nbRelations) + "relations")
                    except ValueError:
                        print(str(ValueError) + line)
                        pass
            print(str(nbRelations) + "relations")            

    
    # Extract all sentences of the tagged text, then check which words are indexed (themselves or their lemma) in JeuxDeMots
    # and are in relation in JeuxDeMots
    sentence = []
    results = []
    sentenceString = ""
    for line in open(inputTaggedTexts,"r"):
        res = re.search("([^;]+);([^;]+);([^;]+)",line)
        if res:
            token = res.group(1)
            lemma = res.group(2)
            pos = res.group(3)
            position = []
            position.append(token)
            position.append(lemma)
            # if the sentence is finished:
            if token[0] == token[0].upper():
                # check for each pair of token if it is in the dict of relations of JeuxDeMots
                for loc1 in sentence:
                    for loc2 in sentence:
                        if not (loc1 == loc2):
                            word1 = ""
                            word2 = ""
                            if (loc1[0] in neighbors and loc2[0] in neighbors[loc1[0]]):
                                word1 = loc1[0]
                                word2 = loc2[0]
                            if (loc1[1] in neighbors and loc2[0] in neighbors[loc1[1]]):
                                word1 = loc1[1]
                                word2 = loc2[0]
                            if (loc1[0] in neighbors and loc2[1] in neighbors[loc1[0]]):
                                word1 = loc1[0]
                                word2 = loc2[1]
                            if (loc1[1] in neighbors and loc2[1] in neighbors[loc1[1]]):
                                word1 = loc1[1]
                                word2 = loc2[1]
                            if len(word1) > 0:
                                result = []
                                #print(word1+" found! ")
                                result.append(word1)
                                result.append(word2)
                                result.append(selectedRelations[neighbors[word1][word2][0]])
                                result.append(sentenceString)
                                results.append(result)
                sentence = []
                sentenceString = ""
                
            if position[0] in neighbors or position[1] in neighbors :
                sentence.append(position)
            sentenceString += token+" "


    outputFile = open(inputTaggedTexts+".output.txt","w")
    for result in results:
        for element in result:
            outputFile.writelines(element+";")
        outputFile.writelines("\n")
    outputFile.close()

readFile(inputJeuxDeMots, inputFolder, inputTaggedTexts, replacements, letters)