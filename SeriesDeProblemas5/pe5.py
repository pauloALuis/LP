"""
pe5.py
27/08/2021
"""

import re

def f1(s:str):
    l1 = re.split(" ", s)
    l2 = []
    for el in l1:
        print(el)
        if re.match("s", el):
            l2.append(re.findall("s[a-e-i-o-u]", el))
    return l2

print(f1("sol las sol asa sr"))