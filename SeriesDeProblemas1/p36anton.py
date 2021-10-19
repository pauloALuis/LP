import math


def trapezoidal_rule (f, i, N) :
    '''
    Calcula o intregral de uma função num certo intervalo através da Regra do Trapézio
    @param f : função que é integrada
    @param i : intervalo
    @param N : Número de trapézios em que o intervalo é dividído
    @return o valor aproximado do integral da função f no intervalo i
    '''
    last = i[0] # x(n-1)
    x = (i[1] - i[0])/N # delta x, tamanho de cada trapézio do intervalo
    sum = 0 
    for i in range(1, N) :
        sum += f(last) + f(last + x)  # last + x representa o x(n) = x(n-1) + tamanho de cada trapézio do intervalo
        last += x # Atualização do x(n-1)

    return sum * x/2 

def f (x, t=(1, 2, 3, 10**3, math.pi)):
    '''
    Calcula o valor de uma função para uma certa abcissa
    @param x : valor da abcissa
    @return o valor da função para a abcissa x
    '''
    return t[0] * x + math.sin(t[1] * t[3] * x + t[4]) + math.cos(t[2] * t[3] * x + t[4])



print(trapezoidal_rule(f, [0, math.pi], 10000))