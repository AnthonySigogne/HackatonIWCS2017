#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import html2text
from pattern.fr import parsetree

sources = [
"http://www.jeuxdemots.org/HACK/hack_texts/Au%20bonheur%20des%20dames_1%20-%20Wikisource.htm",
]

for url in sources :
    # crawl
    response = requests.get(url)
    h = html2text.HTML2Text()
    text = h.handle(response.content.decode("utf8"))

    # parse
    text = parsetree(text, relations=True, lemmata=True)
    for sentence in text :
        for chunk in sentence.chunks :
            for word in chunk.words :
                print word.string, word.lemma, word.tag
