#!/usr/bin/env python3

"""
Avaliação 1
pb1.py
18/08/2021
"""

import random

#1.a)
def l1(n: int = 10, l: list = []):
    """
    method that creates a list with random numbers "n" times
    @param n: number of the length of the list
    @param l: list to append
    @return list with "n" random integer numbers between 0 and 1 inclusive
    """
    if len(l) < n:
        l.append(random.randint(0,100))
        return l1(n,l)
    return l

print(l1())

#1.b)
def list_sum(n: int = 0, l: list = l1(), sum: int = 0):
    """
    method that sum the odds numbers in the list
    @param n : variable to scroll throught the list elements
    @param l : the list
    @param sum : the sum of the odd numbers in the list
    @param print_manager: variable to manage the print type
    @return the sum variable
    """
    if n < len(l):
        if l[n] % 2 == 1:
            sum += l[n]
            #print the sum
            print(l[n], " + ", end="", flush=True) 
            # makes print ion the same line on terminal
        return list_sum(n + 1, l, sum)
    print(" = ", sum)
    return sum

print("soma dos nº impares da lista = ", list_sum())

#1.c)
def f1(n: int):
    """
    method that subtract the argument by 1
    @param n : an integer
    @return n minus 1 
    """
    return n-1

sum = list_sum()
print(sum,  "- 1 = ", f1(sum))

def sub_odd_elements(lista: list = [],  n : int = 0, l1: list = l1()):
    """
    recursive method that substract the odd elements of a list by 1
    @param lista : list to return
    @param n : counter
    @param l1 : list of integers
    @return new list with odd numbers of "l1" subtracted by 1
    """
    if n < len(l1):
        if l1[n] % 2 == 1:
            lista.append(f1(l1[n]))
        else:
            lista.append(l1[n])
        return sub_odd_elements(lista, n+1, l1)
    return lista

print(sub_odd_elements())