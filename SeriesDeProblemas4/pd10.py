"""
pd10.py
26/08/2021
"""

import math
import string

#10.a)
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

n = 20
x = fib(n)
s = ""


#10.b)
def fib_sqrt(fib_num: int):
    yield math.sqrt(fib_num)

s_sqrt = ""
for i in range(n): 
    y = next(x)
    j = fib_sqrt(y)
    print(str(y), end=" ")
    if y > 0:
        s += str("{:.3f}".format(next(j))) + " "
    else:
        s = "0 "
print("\n", s)

#10.c)
def f3():
     for i in list(string.ascii_lowercase):
         yield i

#10.d)
def f4(letter):
    vocals = ["a", "e", "i", "o", "u"]
    is_vocal = False
    for vocal in vocals:
        if vocal == letter:
            is_vocal = True
            yield "V"
    if not(is_vocal):
        yield letter
    is_vocal = False

x = f3()
s = "\n"
for i in range(len(list(string.ascii_lowercase))):
    letter = next(x)
    print(letter, end=" " )
    j = f4(letter)
    s += next(j) + " "
print(s)