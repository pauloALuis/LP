"""
pc7.py
22/08/2021
"""

import pickle
import random
import string

file = "./SeriesProb/SeriesDeProblemas3/pc7-file-1.txt"
file2 = "./SeriesProb/SeriesDeProblemas3/pc7-file-2.txt"
file3 = "./SeriesProb/SeriesDeProblemas3/picke-file-3.txt"

#7.a)
def f1(d: dict = {"a" : "one", "b" : "two"}):
    """
    method that serializate a dict and saves him in a file
    @param d : a dictionary
    """
    f = open(file, "w")
    f.write(repr(d))
    f.close()

#f1()

#7.b)
def f2():
    """
    method that dumps a list of tuples into a 
    serialize file and then loads the list
    """
    list = [('a', 'b', 'c'), ('d', 'e', 'f'), (1, 2, 3)]
    file_name = "./SeriesProb/SeriesDeProblemas3/picke-file1.pkl"

    file = open(file_name, "wb")
    pickle.dump(list, file)
    file.close()

    file = open(file_name, "rb")
    loaded_list = pickle.load(file)
    file.close()
    print(loaded_list)

#f2()

#7.c)
def gen_numbers_to_file(file_name : str):
    """
    method that fills a file with numbers 
    @param file_name : the name of the file
    """
    with open(file_name, "w") as f:
        for _ in range(0, 100):
            f.write(str(random.randint(0,1000)) + "\n")
        f.close()
gen_numbers_to_file(file2)

def f3():
    """
    method that reads a file data to a list and then serializes them 
    """
    file_name = "./SeriesProb/SeriesDeProblemas3/picke-file2.pkl"
    l = []
    with open(file2, "r") as f:
        for _ in range(0,100):
            l.append(int(f.readline()))

    f = open(file_name, "wb")
    pickle.dump(l, f)
    f.close()
    
f3()

#7.d)
def gen_list():
    """
    generate a list with 100 positions with random numbers
    """
    l : list = []
    [l.append(random.randint(0, 1000)) for _ in range(100)]
    return l

def gen_dict():
    """
    generates a dictionary with 10 entries
    key is a string and the value is a float
    """
    d : dict = {}
    for _ in range(0, 10):
        key = random.choice(string.ascii_letters)
        value = random.uniform(0, 10)
        d[key] = value
    return d

def f4(file_name : str, d : dict, l : list):
    """
    method that serialize a dict 
    and a list in a serialization file
    @param file_name : the name of the file
    """
    file = open(file_name, "wb")
    pickle.dump(list(l), file)
    pickle.dump(dict(d), file)
    file.close()

f4(file3, gen_dict(), gen_list())



