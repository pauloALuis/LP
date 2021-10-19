"""
pc5.py
21/08/2021
"""

import random

file1 = "./SeriesProb/SeriesDeProblemas3/ola.txt"
file2 = "./SeriesProb/SeriesDeProblemas3/ola2.txt"
file3 = "./SeriesProb/SeriesDeProblemas3/ola3.txt"
file4 = "./SeriesProb/SeriesDeProblemas3/ola4.txt"

#5.a)
def f1(file_name: str):
    """
    method that writes in a file 100 random numbers between 0 and 100
    @param file_name : the name of the file
    """
    s = ""
    for _ in range(100):
        s += str(int(random.uniform(0,100))) + "\n"
    file = open(file_name, "w")
    file.write(s)
    file.close()

f1(file1)

#5.b)
def f2(file_name: str):
    """
    method that writes a file 100 random float numbers numbers between 0 and 1
    @param file_name : the name of the file
    """
    s = ""
    for _ in range(0, 100):
        s += str(random.uniform(0, 1)) + " "
    file = open(file_name, "w")
    file.write(s)
    file.close()

f2(file2)

#5.c)
def f3(file_name: str):
    """
    method that returns a list of tuples 
    each tuple contains the stirng and the number presented in each line of the file 
    @param file_name : the name of the file
    @return list of tuples
    """
    l = []
    with open(file_name) as f:
        for _ in range(10):
            s = f.readline()
            l.append((s.split(" ")[0], s.split(" ")[1][:1]))
    return l

print(f3(file3))

#5.d
def f4(file_name : str, n: int = 20):
    """
    method that writes the word "TESTE" at the index "n" in one file
    @param file_name: the name of the file
    @param n : the index to write the word "TESTE"
    """
    with open(file_name, "r") as f:
        s = f.readline()

    s = s[:n] + " TESTE " + s[n:]
    with open(file_name, "w") as f:
        s = "".join(s)
        f.write(s)

f4(file4)