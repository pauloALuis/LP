#!/usr/bin/env python3

"""
p34.py
2020/10/30

Sites:
https://en.wikipedia.org/wiki/Newton%27s_method - método de newton
https://pt.wikipedia.org/wiki/Equação_cúbica
https://www.w3schools.com/python/ref_string_split.asp - split function
https://en.wikipedia.org/wiki/Approximation_error - aproximation error
"""
import math

#ex 4.a)
def p(x):
    """
    função que calcula um polinomio de 3º grau
    """

    s = ""
    grau = len(x) -1
    count = 0

    if x[0] != 0:
        while count < len(x):
            s +=  str(x[count]) + "x"
            if grau != 0:
                s += "**" + str(grau) + " + "
            grau -= 1
            count += 1
    else:
        print("o coeficiente do termo de 3º grau não pode ser 0")
    return s

#ex 4.b)
def newton(p: str, error: int, i: list):

    #derivada = p[0] * 3 * i[0]**2 + p[1] * 2 * i[0] + p[2]
    derivada = calc_derivada(p, i)
    sucessao_anterior = i[0]
    x = 0
    while(True) :
        if derivada != 0 :
            x = sucessao_anterior - calc_polinomio(p, sucessao_anterior) / derivada
            #print("erro:", abs((sucessao_anterior - x)/sucessao_anterior))
            if abs((sucessao_anterior - x)/sucessao_anterior) <= error:
                if x >= i[0] and x <= i[1] :
                    return x
                else:
                    break
            sucessao_anterior = x
        else:
            break
    return None

def calc_derivada(p: str, i: list):
    return p[0] * 3 * i[0] **2 + p[1] * 2 * i[0] + p[2]

def calc_polinomio(p, l):
    return p[0] * l ** 3 + p[1] * l ** 2 + p[2] * l + p[3]

if __name__ == "__main__":
    #ex 4.a)
    x = [8, 4, 6, 7]
    intervalo = [-1, 1]
    print("polinomio de 3º grau: " ,p(x))
    print("raiz do polinomio pelo método de Newton: ", newton(x, 0.000001, intervalo))
pass
