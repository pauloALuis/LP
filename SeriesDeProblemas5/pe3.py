"""
pe3.py
27/08/2021
"""

import glob
import os

#3.a)
def f1(file_name, path):
    s = ""
    for name in glob.glob(path, recursive=False):
        if os.path.isfile(name):
            f = open(name, "r")
            s += str(f.readlines())
    with open(file_name,  "w") as fn:
        fn.write(s)
    
f1("glob1.txt", ".\*")