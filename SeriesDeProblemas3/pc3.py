"""
pc3.py
21/08/2021
"""

#3.a)
def f1(s: str = "ieu, rfg iuerh . "):
    """
    method that return list with 3 lists. 
    first list divides the string s by "."
    second list divides the string s by ","
    third list divides the string s by " "
    @param s : the string
    @return a list with 3 lists inside
    """
    l1 = s.split(".")
    l2= s.split(",")
    l3 = s.split(" ")
    return [l1, l2, l3]

print(f1())

#3.b)
def f2( s : str = "ksfduygei fuweigf wiwuegf87g"):
    """ 
    @param s : the string
    @return list with the words of a string in upper case
    """
    s = s.upper()
    return s.split(" ")

print(f2())

#3.c)
def f3(l: list = ["aiugdsf usaedg", "iudf iurth", "toeir", "yerh"]):
    """
    method that return all the word that begin with a vocal inside a list of strings
    @param l : list of string
    @return string with all the words that begin with a vocal
    """
    vocals = ["a", "e", "i", "o", "u"]
    s = ""
    for element in l:
        s2 = element.split(" ")
        for s3 in s2:
            for vocal in vocals:
                if s3[0] == vocal:
                    s+= s3 + "\n"
    return s

print(f3())

#3.d)
def f4(s: str = "iasuyg weygf wiuegf wieugf"):
    """
    method that return the first letter of each word ina  string
    @param s: the string
    @return the first letter of the word in string "s"
    """
    s2 = s.split(" ")
    result = ""
    for s3 in s2:
        result += s3[0]
    return result

print(f4())