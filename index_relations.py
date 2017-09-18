#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
import uuid
import json

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
                url = "http://localhost:9200/relations/relation/%s"%(uuid.uuid4())

                payload = json.dumps({
                    "mot1":mot1,
                    "mot2":mot2,
                    "relation":rel,
                    "poids":poids
                })
                headers = {
                    'authorization': "Basic ZWxhc3RpYzpjaGFuZ2VtZQ==",
                    'content-type': "application/json",
                    'cache-control': "no-cache",
                    }

                response = requests.request("PUT", url, data=payload, headers=headers)

                print(response.text)

        except Exception as inst:
            print(inst)
