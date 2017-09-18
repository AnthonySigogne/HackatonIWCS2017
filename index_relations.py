#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
import uuid
from elasticsearch import Elasticsearch

es = Elasticsearch(['http://elastic:changeme@localhost:9200'])

with open("relations_utf8.txt", "r") as f :
    for line in f :
        try :
            # extraction relations for a word
            mot1, relations = line.strip().split(":",1)
            mot1 = mot1.split(">")[0]
            for relation in re.finditer("[{,]?(?P<mot2>[^:]+):{(?P<relation>[0-9]+),(?P<poids>[0-9]+)}", relations) :
                mot2 = relation.group("mot2").split(">")[0]
                rel = int(relation.group("relation"))
                poids = int(relation.group("poids"))
                print(mot1,mot2,rel,poids)

                # index relation in elasticsearch
                res = es.index(index="relations", doc_type='relation', id=str(uuid.uuid4()), body={
                    "mot1":mot1,
                    "mot2":mot2,
                    "relation":rel,
                    "poids":poids
                })

        except Exception as inst:
            print(inst)
