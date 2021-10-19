"""
pc10.py
23/08/2021
"""
import random
import sqlite3
import math

#10.a)
def f1(n : int = 10):
    l = []
    for i in range(n): 
        try:
            l.append(random.randint(0,100) / random.randint(-5, 5))
        except:
            print("erro na iteração: ", i)
    return l         
#print(f1())

#10.b)
def f2(file_name : str = "ola.txt"):
    """
    method that reads a file
    @param file_name : the name of the file
    @return a list with content of file 
    """
    try:
        f = open(file_name, "r")
        l = [line[:2] for line in  f.readlines()]
        return l
    except:
        return "nao foi possivel abrir o ficheiro"
#print(f2())

#10.c)
def f3():
    """
    method that read the content of a sqllite3 table
    """
    con = sqlite3.connect('teste.db')
    cur = con.cursor()
    try:
        cur.execute("select * from familiy")
    except:
        print("nao foi possivel aceder ao ficheiro da db")
#f3()

#10.d)
def f4():
    l = []
    for i in range(0, 10):
        try:
            x = random.uniform(-math.pi, math.pi)
            l.append(math.sin(x) / math.cos(x))
            #print("{:.2f}".format(x))
        except:
            print("erro na iteração ", i)
    return l
print(f4())