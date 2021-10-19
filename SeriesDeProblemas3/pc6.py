"""
pc6.py
22/08/2021
"""

from __future__ import print_function
import sys

file4 = "./SeriesProb/SeriesDeProblemas3/ola4.txt"
file5 = "./SeriesProb/SeriesDeProblemas3/ola5.txt"
vocals = ["a", "e", "i", "o", "u"]

#6.a)
def error_print(args: list):
    """
    function that writes on error console and output 
    console what was written in the input console
    @param args : the list of words of input 
    """
    s = ""
    for arg in args: 
        s += arg + " "
        if arg == "exit":
            break
    print(s, file=sys.stderr)
    print(s, file=sys.stdout)

#s = input("Escreva qualquer coisa: Termine com exit: \n")
#error_print(s.split(" "))

#6.b)
def f2(file_name: str):
    """
    method that writes in error console "OOPS" whenever 
    the contents in the file has the syllable "te"
    @param file_name : the name of the file
    """
    last = ""
    with open(file_name) as fileobj:
        for line in fileobj:  
            for ch in line: 
                if last == "t" and ch == "e":
                    print("OOPS", file=sys.stderr)
                last = ch
            last = ""

#f2(file4)

#6.c)
def f3():
    """
    method that saves the digits of a string in a file
    """
    s = input("Escreva uma frase para que sejam guardados os dígitos num ficheiro: \n")
    content = ""
    for letter in s:
        if letter.isdigit():
            content += letter
    f = open(file5, "w")
    f.write(content)
#f3()

#6.d)
def f4():
    """
    method that writes the input with no vocals on the output
    """
    s = input("write something: \n")
    content = ""
    is_vocal = False
    for letter in s:
        for vocal in vocals:
            if letter == vocal:
                is_vocal = True
                break
        if not(is_vocal):
            content += letter
        is_vocal = False
    print("String with no vocals: ", content)
f4()