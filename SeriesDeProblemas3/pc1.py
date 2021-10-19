"""
pc1.py
20/08/2021
"""

#1.a)
def f1(s : str, n: int = 3):
    """
    method that substirngs a string "n" times in positions 4 - 8 and 13 - 20  
    @param s : string to be substringed
    @param n : substring times
    @return string "s" substringed "n" times
    """
    result = ""
    if not(len(s) == 0 or len(s) > 20):
        for _ in range(0, n):
            result += s[1: 4] + s[8: 13]  + "\n"
    else:
        print("Invalid String")
        return ""
    return result

#1.b)
def dict_gen(s: str):
    """
    generate dictionarybased on string "s"
    @param s : string
    """
    d = {}
    for i in s:    
        counter = 0
        for j in s:
            if i == j:
                counter+=1
        d.update({i: counter})
    return d

#1.c)
def concat_str(l: list = ["abc", "def", "cdef", "abcd"]):
    """
    method that returns a string resulting of the concatenation of the string in the list
    @param l: list of strings
    @return string with the string with even length
    """
    result = ""
    for s in l:
        if len(s) % 2 == 0:
            result += s
    return result

#1.d)
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

if __name__ == "__main__":
    #1.a)
    print(f1("bernardomarques"))
    
    #1.b)
    print(dict_gen("aaabbbbccccbbbaaaa"))

    #1.c)
    print("concat = ", concat_str())

    #1.d)
    print(get_tuple_info())
pass

