"""
pe4.py
27/08/2021
"""

import argparse
import math

#4.a)
def f1():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fact", type=int) 
    parser.add_argument("--pow", type=int) 
    args = vars(parser.parse_args())
    s = ""
    print(args)
    for arg in args:
        print(arg, "   ", args[arg])
        if args[arg] != None:
            if arg == "fact":
                s += "fatorial  de: " + str(args[arg]) + " = " + str(math.factorial(int(args[arg]))) + "\n"
            elif arg == "pow":
                s += "potencia: 10 ** " + str(args[arg]) + " = " + str(math.pow(10, int(args[arg]))) + "\n"
    return s

print(f1())