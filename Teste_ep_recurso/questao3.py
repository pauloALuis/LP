"""
Paulo Luis 17359
questao3.py
31/08/2021
"""

import matplotlib.pyplot as plt
import numpy as np
import math

def grafico_gen():
    """
    função que usa a biblioteca matplotlib para gerar um gráfico, com 100 pontos, das funções 
    "cos(x)", "x**3 - 2x**2" e a multiplicação das duas últimas
    """
    div = 6*math.pi / 100 # divisão em 100 pontos iguais
    x = -3* math.pi # começo do valor de x correspondente ao inicio do intervalo indicado
    xl = [] # valores de x em 100 pontos
    cosl = [] # valores da função cos(x) em 100 pontos
    fl = [] # valores da função x**3 - 2x**2 em 100 porntos
    cosl_fl = [] # valores da função x**3 - 2x**2 * cos(x) em 100 pontos
    #gerar as listas com as funções em 100 pontos
    for _ in range(100):
        f_cos = math.cos(x)
        f_y = 3**x - (2*x)**2
        f_cos_y = f_cos * f_y
        cosl.append(f_cos)
        fl.append(f_y)
        cosl_fl.append(f_cos_y)
        xl.append(x)
        x += div # incremento do valor de x pelo valor da divisão

    plt.plot(xl,cosl)
    plt.plot(xl, fl, color='red')
    plt.plot(xl, cosl_fl, color='yellow')
    plt.axis(xmin=-10, xmax=10, ymin=-10, ymax=10)
    plt.xlabel('x values from -3pi to 3pi')
    plt.ylabel('F(x)')
    plt.title('Grafico questao 3')
    plt.legend(['cos(x)', 'x^3 - 2 x^2', 'cos(x) * x^3 - 2 x^2']) 
    plt.savefig("cosmopoly.pdf")
    plt.show()
#grafico_gen()

#matriz A de dimensão (10 x 10) com numeros aleatorios uniformemente distribuios entre 0 e 1 unsando a bilioteca numpy
A = np.random.uniform(0, 1, size=(10,10))

#vetor v de 10 posições com numeros aleatorios uniformemente distribuios entre 1 e 2 unsando a bilioteca numpy
v = np.random.uniform(1,2, 10) 

#multiplicações matriciais de A * v e v * A utilizando o módulo multiply da biblioteca numpy
mul_A_v = np.multiply(A, v)
mul_v_A = np.multiply(v, A)
#escrita na consola
print("A:\n", A)
print()
print("v:\n", v)
print()
print("A * v:\n", mul_A_v)
print()
print("v * A:\n", mul_v_A)
grafico_gen()
