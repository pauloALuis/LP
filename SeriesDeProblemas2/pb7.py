#!/usr/bin/env python3

"""

pb1.py
19/08/2021
"""

import random

#7.a)
words = ["Aa bb CC", "dd ee ff"]

def dict_gen(s1: str, s2: str):
    """
    method that creates a dictionaries with two stirng of the same length
    @param s1 : keys string
    @param s2 : values string
    @return dict with keys and values of the respective words
    """
    dict = {}
    if len(s1) == len(s2):
        [dict.update({s1.split(" ")[i]: s2.split(" ")[i]}) for i in range(0, len(s1.split(" ")))]
    return dict

print(dict_gen(words[0], words[1]))

#7.b)
def dict_gen2(s: str):
    """
    method that creates a dict depending on a string
    @param s : string
    @return a dict
    """
    s2 = ""
    sum = 0
    dict = {}
    for i in range(len(s)):
        if s[i] == " ":
            dict.update({sum : s2})
            sum = 0
            s2 = ""
        elif i == len(s) - 1:
            sum += i
            dict.update({sum : s2 + s[i]})
        else:
            s2 += s[i]
            sum += i
    return dict 

print(dict_gen2("ab cd ef ghih hj"))

#7.c)
def rm_pair_keys(d: dict):
    d2 = {}
    for key in d:
        if len(d[key]) % 2 == 0:
            d2.update({key: ""})
        else:
            d2.update({key: d[key]})
    return d2

dict = {"1": "abc", "2": "fr", "3": "lala"}
print(rm_pair_keys(dict))

#7.4)
def dict_gen3():
    d = {}
    l = []
    key = random.randint(0, 20)
    for _ in range(key):
        l.append(0)
    d.update({key: l})
    return d
print("dict criado: ", dict_gen3())

