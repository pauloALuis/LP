"""
Paulo Luis 17359
questao1.py
31/08/2021
"""

import math
import random

def ln2(n : int, i : int = 1, sum: float = 0):
    """
    função que calcula recursivamente a soma dos n termos da sucessão ((-1)^(n-1)/)n
    lança uma exceção para numeros decimais ou não positivos
    @param n : n termos da sucessão
    @param i: termos atual da sucessão
    @param soma soma da sucessão
    @return -1 se n for um numero decimal
    @return -2 se n for menor que 1
    @return soma dos n termos da sucessão
    """
    try:
        int(str(n))
    except:
        return -1
    try:
        math.sqrt(n)
    except:
        return -2

    if i < n:
        sum += ((-1)**(i-1)) /i
        i += 1
        return ln2(n, i, sum)
    else:
        return sum

print("soma final = ", ln2(60))

def ln2_list(n = 101):
    """
    função que cria uma lista de tuplos em que o primeiro elemento de cada tuplo é um número uniformemente aleatório
    e o segundo elemento é o valor da soma devolvido pela função ln2
    @param n : numero de elementos (tuplos) da lista
    @return lista com n tuplos
    """
    l = []
    for i in range(1,n):
        t = ("{:.2f}".format(random.uniform(1,500)), "{:.6f}".format(ln2(i)))
        l.append(t)
    return l

# escreve no ficheiro ln2.txt os tuplos da lista
with open("ln2.txt", "w+") as f:
    for el in ln2_list():
        f.write(str(el) + "\n")

print(ln2_list.__doc__)
print(ln2.__doc__)


