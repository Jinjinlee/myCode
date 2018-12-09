#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 11:13:41 2018

@author: lijinjin
"""

try:print(0 / 0)
except ZeroDivisionError:print("cannot divide by zero")


integer_list = [1, 2, 3]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [ integer_list, heterogeneous_list, [] ]
list_length = len(integer_list)
list_sum = sum(integer_list)

tweet = {
         "user" : "joelgrus",
         "text" : "Data Science is Awesome",
         "retweet_count" : 100,
         "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

wc = sorted(word_counts.items(),key=lambda word, count: count, reverse=True)


def lazy_range(n):
    """a lazy version of range""" 
    i= 0
    while i < n:
        yield i 
        i += 1