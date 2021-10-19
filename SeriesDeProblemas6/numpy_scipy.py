"""
Paulo Luis 17359
pf7.py e pf8.py
29/08/2021
"""

# https://numpy.org/doc/stable/user/basics.creation.html

import numpy as np
import math
import scipy
import scipy.integrate as sci
import scipy.optimize

#7 - Numpy
def f1():
    times = 10
    a = np.zeros((10))
    b = np.repeat(math.pi, times)
    sum = np.sum([a, b])    
    mul = np.multiply(a, b)
    print("soma: ", sum)
    print("mul1: ", mul)

    c = np.swapaxes([b], 0, 1)
    print("c: ", c)
    mul = np.multiply(a, c)
    print("mul2: ", mul)
#f1()

#8 - Numpy
def f2():
    a = np.arange(10)
    print(a)
    x = np.random.randint(10, size=(10,10))
    print("x = ", x)
    mul = np.multiply(a, x)
    print("mul: ", mul)
    inv = np.linalg.inv(x)
    #print("inverse = ", inv)
    transpose = x.transpose()
    print("transpose = ", transpose)
f2()

#9 - SciPy
def f3():
    intervalo = [-4, 4]
    i = sci.quad(fun, intervalo[0], intervalo[1])
    print(i)
    roots = scipy.optimize.root(fun, intervalo, method='hybr')
    print(roots)

def fun(x):
    return (x + 2)**2
f3()

def f4():
    intervalo = [-math.pi, math.pi]
    fun2 = lambda x : math.sin(x)
    i = sci.quad(fun2, intervalo[0], intervalo[1])
    print(i)
    roots = scipy.optimize.root(fun2, intervalo, method='hybr')
    print(roots)
#f4()