#!/usr/bin/env python3

"""

pb1.py
18/08/2021
"""

import math
import random

#ex 3.a)
def l1(n = 10, o = 2, m = 0):
    lista = []
    for i in range(0, n):
        x = random.randint(-2, 2)
        distNormal = (1 / o * math.sqrt(2 * math.pi)) * math.exp(-0.5 * (((x - m) / o) ** 2))
        lista.append(distNormal)
    return lista

#ex 3.b)
def l2(l1):
    l22 = []
    l = l1()
    l2 = iter(l)
    x=0
    while True:
        try:
            x = next(l2)
            if x >= 0:
                l22.append(x)
        except StopIteration:
            break
    return l22
    
#ex 3.c)
def sum1(l1):
    sum = 0
    lista = l1()
    l2 = iter(lista)
    x = 0
    while True:
        try:
            x = next(l2)
            if x >= 0:
                sum += x
        except StopIteration:
            break
    return sum

#ex 3.d)
def sum2(l1):
    sum = 0
    lista = l1()
    l2 = iter(lista)
    print(lista)
    x = 0
    while True:
        try:
            x = next(l2)
            s = str(x)
            if int(s[0]) % 2 == 0:
                sum += x
        except StopIteration:
            break
    return sum

if __name__ == "__main__":
    #print("lista 2 = ", l2(l1))

    print(sum2(l1))
pass 