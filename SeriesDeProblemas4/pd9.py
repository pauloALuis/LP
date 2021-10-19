"""
pd9.py
26/08/2021
"""

import math 

#9.a)
def odd_numbers_gen(n):
    i = 1
    while i < n:
        yield i
        i += 2

gen = odd_numbers_gen(40)
for i in range(20):
    print(next(gen))

#9.b)
l = []
def f2(n):
    yield [n, n * math.sqrt(n)]
l.append(next(f2(2)))
l.append(next(f2(3)))
l.append(next(f2(4)))
l.append(next(f2(5)))
print(l)

#9.c)
def f3(n):
    yield format(math.pi, "."+str(n)+"f")

l2 = []
for i in range(1,20):
    l2.append(next(f3(i)))
print(l2)

#9.d)
def f4(s: str):
    yield str(s)
s = "lala a "
for i in range(4):
    s += next(f4(s + str(i)))
print(s)