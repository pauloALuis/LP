#!/usr/bin/env python3

"""


Sites:
https://www.w3schools.com/python/python_tuples.asp - tuplos
https://docs.python.org/3/library/math.html - math library functions
https://pt.wikipedia.org/wiki/Vetor_(matemática) - vetores wikipedia
"""
import math

#ex 3.b)
def vetorModulo(v):
    """
    função que calcula o módulo de um vetor
    """
    return math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)

#ex 3.c)
def produtoInterno(v1, v2):
    """
    função que calcula o produto interno (produto escalar) entre dois vetores
    """
    return v1[0] * v2[0] + v1[1] * v2[1] +v1[2] * v2[2]


#ex 3.d)
def produtoExterno(v1, v2):
    """
    função que calcula o produto externo (produto vectorial) entre dois vetores
    retorna o vetor prependicular aos dois vetores inseridos nos parametros de entrada
    """
    vetorProduto = [0.0, 0.0, 0.0]

    vetorProduto[0] = v1[1] * v2[2] - v2[1] * v1[2]
    vetorProduto[1] = v2[0] * v1[2] - v1[0] * v2[2]
    vetorProduto[2] = v1[0] * v2[1] - v2[0] * v1[1]

    return vetorProduto


if __name__ == "__main__":
    #ex 3.a)
    r_a = (math.pi, math.pi / 2.0, 2 * math.pi)
    r_b = (math.pi ** 2, math.pi, - math.pi)

    #ex 3.b)
    print()
    print("módulo do vetor r_a: ", vetorModulo(r_a))
    print("módulo do vetor r_b: ", vetorModulo(r_b))
    print()

    #ex 3.c)
    print("Produto interno: ", produtoInterno(r_a, r_b))
    print()

    #ex 3.d)
    vect = produtoExterno(r_a, r_b)
    print("Produto externo = vetor[", vect[0], ", " ,vect[1], ", ", vect[2] , "]")
pass
