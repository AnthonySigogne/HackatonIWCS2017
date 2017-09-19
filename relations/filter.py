#!/usr/bin/env python
# -*- coding: utf-8 -*-

#python3

import pickle
import os
import re

# final relations dict
relations = {}

# relations we want to extract
allowed_rels = {
    "17":"r_has_carac",
    "23":"r_has_carac",
    "6":"r_is_a",
    "9":"r_has_part",
    "15":"r_lieu",
    "24":"r_has_agent",
    "26":"r_has_patient",
    "16":"r_has_instrument",
    "41":"r_has_consequence",
    "53":"r_make_use_of"
}

for filename in os.listdir("./") :
    with open(filename, "r", encoding="latin-1") as f :
        if not filename.endswith(".txt") : continue
        print("load filename : "+filename)
        for line in f :
            try :
                # extraction relations for a word
                mot1, rels = line.strip().split(":",1)
                mot1 = mot1.split(">")[0]
                for relation in re.finditer("[{,]?(?P<mot2>[^:]+):{(?P<relation>[0-9]+),(?P<poids>[0-9]+)}", rels) :
                    mot2 = relation.group("mot2").split(">")[0]
                    rel = relation.group("relation")
                    if rel in allowed_rels :
                        relations["%s %s"%(mot1, mot2)] = allowed_rels[rel]
                        relations["%s %s"%(mot2, mot1)] = allowed_rels[rel]
            except Exception as inst:
                print(inst)

print("pickle relations...")
pickle.dump( relations, open( "relations.pickled", "wb" ) , protocol=2)
