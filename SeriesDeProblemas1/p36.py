#!/usr/bin/env python3

"""

p36.py
2020/10/30
"""

import math

#ex 6.a)
def represent_f(x, t = [1, 2, 3], W = 10**3, O = math.pi):
    """
    função para escrever a função f(x)
    """
    return "f(" + str(x) + ") = " + str(t[0]) + "*" + str(x) + "*sin(" + str(t[1]) + "*"+str(W)+ "*"+str(x)+ "+" + str(O) + ") + cos( " + str(t[2]) + "*" + str(W) + "*" + str(x)+ " + " + str(O)+")"


#calculo da função f(x)
"""
função que calcula a função f(x)
"""
def f(x, t = [1, 2, 3], w = 10**3, o = math.pi):
    return t[0] * x + math.sin(t[1] * w * x + o) + math.cos(t[2] * w * x + o)



#ex 6.2)
def regra_trapezoidal(f , i, N):
    sum = 0
    anterior = i[0]
    divisao = (i[1] - i[0])/N
    
    for k in range(1, N):
        sum += f(anterior) + f(anterior + divisao) 
        anterior += divisao
    return sum * divisao / 2.0



if __name__ == "__main__" :
    #ex 6.a)
    print(represent_f(5), " = ", f(5))
    
    #ex 6.b)
    print(regra_trapezoidal(f, [0, math.pi], 1000))
pass
