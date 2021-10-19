#!/usr/bin/env python3

"""

pb1.py
18/08/2021
"""

import random
import math

#4.a)
def generate_list(n: int = 10):
    """
    function that generates a list
    @param n : length of the list
    @return list with pair numbers between 0 and 50
    """
    l=[]
    [l.append(random.randint(0,25) * 2) for _ in range(0, n)]
    return l

#4.b)
def square_root_list(l: list):
    """
    method that returns a square root list of an list
    @param l: the list
    @return a square root list of "l"
    """
    l2 = []
    [l2.append(math.sqrt(i)) if i > 0 else l2.append(0.0) for i in l]
    return l2

l = generate_list(10)
print(l)
print(square_root_list(l))

#4.c)
def multiply_list(l: list, n: int = 3):
    """
    method that returns a list multiplied by "n"
    @param list: list to multiply
    @param n : number of multiplicity
    @return the list with elements multiplies by "n"
    """
    return list(map(lambda x: x*n, l))

print(multiply_list(l))

#4.d)
def remove_pair_numbers(l: list):
    """
    removes even numbers of a list
    @param l : the list
    @return the list l without even numbers
    """
    return list(filter(check_even, l ))

def check_even(n: int):
    """
    method that checks if a number is even or odd
    @param n : the number
    @return true if is evend and false if is odd number
    """
    return True if n % 2 == 0 else False


print(remove_pair_numbers(l))