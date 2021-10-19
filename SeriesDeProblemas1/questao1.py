#!/usr/bin/env python3

"""
p31.py
2020/10/30
"""
import random
import math

#ex 1
def fatorial(n):
    """
    função que calcula o fatorial de n termos
    @param n - número de termos da sucessão
    @return fatorial de n
    """
    fat = 1
    for i in range(1, n + 1):
        if n == 0:
            return 1
        fat  = fat * i
    return fat

#ex 2
def sen(x, sum, n):
    """
    função que calcula o seno(x) 
    @param x - sen(x), valor do seno
    @param sum - soma da interação recursiva da sucessão que calcula o valor aproximado de seno
    @param n - número de iterações
    @return soma com o valor aproximado de sen(x)
    """
    sum += (((-1)**n)  / math.factorial(2*n + 1)) * (x**(2 * n + 1))

    if n > 0:
        return sen(x, sum, n-1)
    return sum

#ex 3
def string(s):
    s2 = ""
    for i in s:
        if ord() % 2 == 0:
            s2 += "0"
        else:
            s2 += "1"
    return s2


def ord():
    return random.randint(0, 9)

#ex 4
def stringToUpperCase(s):
    s2 = ""
    counter = 0
    for i in s:
        s2 += s[counter].capitalize()
        counter += 1
    return s2

if __name__ == "__main__" :
    x = 4
    #ex 1)
    print(x,"! = ", fatorial(x))

    #ex 2)
    print("sen(", x ,") = ", sen(math.pi/2.0, 0, 30))

    #ex 3)
    print(string("abcdewfwdew"))

    #ex 4)
    print(stringToUpperCase("string"))
pass