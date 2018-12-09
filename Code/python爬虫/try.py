#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 16:52:49 2018

@author: lijinjin
"""


from urllib.request import urlopen 
from urllib.error import HTTPError 
from bs4 import BeautifulSoup
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read()) 
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title 

if __name__ == '__main__':
    title = getTitle("http://www.pythonscraping.com/pages/page1.html") 
    
    if title == None:
        print ("Title could not be found")
    else:
        print (title)
        

for sentence in sentences:
    if "google" in sentence.lower():
        taggedWords = pos_tag(word_tokenize(sentence))

for word in taggedWords:
    if word[0].lower() == "google" and word[1] in nouns:
        print (sentence)
        
        
        