"""
pc2.py
20/08/2021
"""

import random

vocals = ["a", "e", "i", "o", "u"]

#2.a)
def f1(s : str, n: int = 3):
    """
    method that substirngs a string "n" times in positions 4 - 8 and 13 - 20  
    @param s : string to be substringed
    @param n : substring times
    @return string "s" substringed "n" times
    """
    result = ""
    if check_len(s):
        for _ in range(0, n):
            result += s[1: 4] + s[8: 13]
    else:
        return ""
    result2 = replace_vocals(result)
    return result2

def check_len(s: str):
    """
    method that checks the length of a string
    @param s: the string
    @return True if the length of the string s is between 0 to 20
    """
    return len(s) > 0 and len(s) < 20  

def replace_vocals(s: str):
    """
    method that replaces vocals of a string to "b"
    @param s : the string
    @return the replaced string 
    """
    x = s
    for vocal in vocals: 
        x = x.replace(vocal, "b") 
    return x
    
print(f1("aejjjjiou"))

#2.b)
def f2(s :str):
    """
    method that creates a tuple depending on a char of a string
    @param s: the string
    @return tuple where the first element is the char and 
            second is the number of ocurrences if its s vocal. 
            Else, second element is 0 
    """
    counter = 0
    char = get_random_char(s)
    if is_vocal(char):
        for c in s:
            if c == char:
                counter += 1
    return (char, counter)

def is_vocal(c: str):
    """
    checks if a char is a vocal
    @param c : the char
    @return True if "c" is a vocal
    """
    for vocal in vocals:
        if vocal == c and len(c) == 1:
            return True 
    return False

def get_random_char(s: str):
    """
    metohd that returns a random char of a string
    @param s : the string
    @return a random char
    """
    return s[random.randint(0, len(s))]

print(f2("aaaabb"))

#2.c)
def f3(l: list = ["bernardo", "martinho", "marques", "IP Beja", "2021", "LP", "bue fixe"]):
    """
    method that returns a string with the content of the strings in a list, if the length of the list is higher than 6
    @param l : the list
    @return concatenated string
    """
    if len(l) > 6:
        s = ""
        for el in l:
            s+= el + " "
        return s

print("String: ", f3())

#2.d)
def get_tuple_info(t: tuple = ("abcd acd", "a ab efghij", "a abc efgh lalaal")):
    l = []
    t2 = ("", "", "")
    counter = 0
    highest = ""
    lowest = ""
    for string in t:
        for word in string.split(" "):
            if counter == 0:
                lowest = word
                highest = word
            if len(word) > len(highest):
                highest = word
            if len(word) < len(lowest):
                lowest = word
            counter +=1
        t2 = (len(string), highest, lowest)
        counter = 0
        l.append(t2)
    return l

print(get_tuple_info())