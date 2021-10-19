#!/usr/bin/env python3

"""
pb1.py
19/08/2021
"""


strings_list = ["Bernardo Martinho Marques , 18373 , , ,",
                "Bernardo Martinho Marques , 18373 2021",
                "Bernardo Martinho Marques , 18373 LEI",
                "Bernardo Martinho Marques , 18373 IP Beja",
                ]

vocals = ["a", "e", "i", "o", "u"]

#6.a)
def l1(s: str):
    """
    function that returns all the words of a string in a list
    @param s : the string
    @return the list with the words of "s"
    """  
    return s.split(" ")

def list_to_set(l: list):
    """
    @param l : list to cast
    @return a set of "l"
    """
    return set(l)

def gen_random_word():
    return 


print (l1(strings_list[0]))
print (list_to_set(l1(strings_list[0])))
    
#6.b)
def sets_list():
    """
    method that creates a list "l" with sets of words
    @return the list "l"
    """
    l = []
    [l.append(list_to_set(l1(s))) for s in strings_list]
    return l

print()
print("Lista de Sets:")
print(sets_list())

#6.c)
def char_repetition(s: str = "aaabbbccc"):
    """
    @return the number of the duplicated chars in a string
    """
    #print(len(s), " - ", len(set(s)), " = " , (len(s) - len(set(s))))
    return len(s) - len(set(s))

print(char_repetition())

def vocal_repetition(vocals: list = vocals, s: str = "aaabbbccc"):
    """
    method that calculates the number of vocals duplicated in a string
    @param s : the string
    @return number of vocals duplicated in "s" 
    """
    counter = 0
    l = []
    [l.append(False) for _ in range(len(vocals))]

    for letter in s:
        for vocal in range(len(vocals)):
            if letter == vocals[vocal] and l[vocal] == True:
                counter +=1
            elif letter == vocals[vocal] and l[vocal] == False:
                l[vocal] = True
    return counter

print("vogais repetidas = ", vocal_repetition())

#6.d)
def equal_words(s1: str, s2: str):
    """
    method that calculates the number of words there are comun in two strings
    """
    l = [[ 1 for word2 in list_to_set(l1(s2)) if word1 == word2] for word1 in list_to_set(l1(s1))]
    return len(l)

print(equal_words(strings_list[0], strings_list[1]))