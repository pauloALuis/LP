#!/usr/bin/env python3

"""
p35.py
2020/10/30

Sites:
https://pt.wikipedia.org/wiki/Equação_cúbica
"""
from inspect import signature

def n_args(*args):
    """
    função que calcula o número de argumentos de uma função
    """
    return len(args)

#ex 5.a)
def sistema_equacoes(A, b):
    """
    função que retorna uma string que representa um sistema de equações lineares de 3 icógnitas 
    """
    s = ""
    var = ["x", "y", "z"]
    for i in range(int(len(A))):
        for j in range(int(len(A))):
            if int(A[i][j]) >= 0:
                if j != 0:
                    s += " + "
                s += str(A[i][j]) + var[j]
            else:
                s += " - "
                s += str(abs(A[i][j])) + var[j]
        s+= " = "+ str(b[i]) +"\n"        
    return s

#ex 5.b)
def det(A):
    return (A[0][0]*A[1][1]*A[2][2] + A[0][1]*A[1][2]*A[2][0] + A[0][2]*A[1][0]*A[2][1]) - (A[2][0]*A[1][1]*A[0][2] + A[2][1]*A[1][2]*A[0][0] + A[2][2]*A[1][0]*A[0][1])
    
#ex 5.c)
def cramer(A, b):
    """
    utilização da regra de cramer para solucionar equações lineares de 3 icógnitas
    parametro A - matriz dos coeficientes
    parametro b - vetor dos termos independentes
    retorna o [X, Y e Z] em lista, que são os valores das icógnitas
    """
    d = det(A)
    
    x = det([[b[0], A[0][1], A[0][2]], [b[1], A[1][1], A[1][2]],[b[2], A[2][1], A[2][2]]])
    y = det([[A[0][0] ,b[0], A[0][2]], [A[1][0], b[1], A[1][2]],[A[2][0], b[2], A[2][2]]])
    z = det([[A[0][0], A[0][1], b[0]], [A[1][0], A[1][1], b[1]],[A[2][0], A[2][1], b[2]]])

    X = x / d
    Y = y / d
    Z = z / d
    return [X, Y, Z]

if __name__ == "__main__":
    #ex 5.a)
    matriz = [[6, 1, 1],[4, -2, 5], [2, 8, 7]]
    solution = [2, 3, 4]

    print("Equação:")
    print(sistema_equacoes(matriz, solution))
    print()

    #ex 5.b)
    print("Determinante = ", det(matriz))

    #ex 5.c)
    print(cramer(matriz, solution))
    

pass
