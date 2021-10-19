#!/usr/bin/env python3

"""
Avaliação 1
pb1.py
18/08/2021
"""

#ex 2.a)
def f1(s1: str = "bedgertgcde", n: int = 0, s2: str = ""):
    if n < len(s1):
        if s1[n] not in "aeiouAEIOU":
            s2 += s1[n]
        return f1(s1, n + 1, s2)
    return s2

#ex 2.b)
def f2(s1: str = "abcdefg", s2: str = "", n: int = 0):
    if n < len(s1):
        if s1[n] in "bB ":
            s2 += "a"
        else:
            s2 += s1[n]
        return f2(s1, s2, n + 1)
    return s2

#ex 2.c)
def f3(s1: str = "abcdefg", nVocals: int = 0, n: int = 0):
    if n < len(s1):
        if s1[n] in "aeiouAEIOU":
            nVocals += 1
        return f3(s1, nVocals, n + 1)
    return nVocals

#ex 2.d)
def f4(lista: list = [1, 2, 3, 4, 5, 6, 7, 8], a: int = 1, b: int = 7,n: int = 0, l: list = []):
    if a < 0 or b >= len(lista):
        return print("dados invalidos!")
    
    if n < len(lista):
        if  n >= a and n <= b and lista[n] % 2 == 0:
            l.append(lista[n]) 
        return f4(lista, a, b,  n + 1, l)
    return l

if __name__ == "__main__":
    print(f4())
pass 