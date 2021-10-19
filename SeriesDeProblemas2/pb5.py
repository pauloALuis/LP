#!/usr/bin/env python3

"""
pb1.py
19/08/2021
"""

import numpy as np
import random
import string

#5.a)
def list_gen(n: int = 10):
    """
    method that generates a list
    @param n : length of the generated list
    @return generated object with a list
    """
    mu, sigma = 0, 3.2
    yield [int(np.random.normal(mu, sigma)) * 2 for _ in range(n)]

l =  list(list_gen())

#5.b)
def string_gen(n: int = 10):
    """
    method that generates a random lower case string with n characters
    @param n : the length of string
    @ generated object with a string
    """
    yield [random.choice(string.ascii_lowercase) for _ in range(n)]

[print(_) for _ in string_gen()]

#5.c)
def tuple_gen(n: int = 10):
    """
    method that generates a tuple with numbers in a uniform distribution
    @param n : the tuple length
    @return generated object with a tuple
    """
    yield tuple([(random.randint(0,100)) for _ in range(0,n)])

print([i for i in tuple_gen()]) 

#5.d)
def even_num_gen():
    """
    method that generates a random even number
    @return generated object with an even number
    """
    yield [random.randint(0, 25) * 2]

print("even numebr: ", next(even_num_gen()))

