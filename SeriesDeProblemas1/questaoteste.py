"""
questão teste 
18/08/2021
"""
import math

#1)
def string_vocals(s: str):
    """
    calculates the index of first and last vocal in a string
    @param s : the string given
    @return the tuple with indexes of first and last vocals in the string s
    """
    first_checked = False
    vocals = ["a", "e", "i", "o", "u"]
    result = ['', '']
    for i in range(len(s)):
        for vocal in vocals:
            if s[i] == vocal:
                if not(first_checked):
                    result[0] = str(i)
                    first_checked = True
                result[1] = str(i)
    return tuple(result)

print(string_vocals("abcde"))

#2)
def cartesiano_to_polar(t: tuple):
    l = ['', '']
    x= int(t[0])
    y = int(t[1])
    r = pitagoras(x, y)
    arctan = 0
    if x > 0:
        arctan = math.atan(y/x)
    elif x < 0 and y >= 0:
        arctan = math.atan(y/x) + math.pi
    elif x < 0 and y < 0:
        arctan = math.atan(y/x) - math.pi
    elif x == 0 and y > 0:
        print("entrou")
        arctan = math.pi / 2
    elif x == 0 and y < 0:
        arctan = - math.pi / 2
    else:
        arctan = "undifened"

    return (r, arctan)

def pitagoras(x: str, y: str):
    return math.sqrt(math.pow(int(x), 2) + math.pow(int(y), 2))

print(cartesiano_to_polar(string_vocals("abcde")))

#3
def calc_coordenates_circ(raio: float, phi: float):
    return (math.cos(phi) * raio, math.sin(phi) * raio)
    
print(calc_coordenates_circ(5.0, 0.25 * math.pi)) #45 graus

#4
def calc_lower_vocals(s: str):
    i = 0
    vocals = ["a", "e", "i", "o", "u"]
    for char in s:
        for vocal in vocals:
            if char == vocal:
                i +=1
    return i

print(calc_lower_vocals("aAbeeiI"))