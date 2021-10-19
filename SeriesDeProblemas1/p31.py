#!/usr/bin/env python3


import math

#ex 1.a)
def fibonacci(n):
    """
    função calcula os números de fibonacci e que retorna o "n" termo da sucessção
    Sucessão de fibonacci: F{n} = F{n-1} + F{n-2}
    n - parametro de entrada que indica o número da sucessão de Fibonacci a procurar
    count - contador
    return - núemro da sucessão de fibonacci do termo n
    """
    count = 0 #lala
    sum = 0
    f1 = 0
    f2 = 1

    if n == 0:
        print("não existe o termo 0 da sucessão")
    elif n == 1:
        return 1
    else:
        while count < n:
            sum = f1 + f2
            f2 = f1
            f1 = sum
            count += 1
        return f1

    """ outra forma de calcular a mesma recursivamente
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    """

#ex 1.b)
def reciprocoFibonacci(n):
    """
    Função que calcula a constante reciproca das sucessão de fibonacci
    n - termo n da sucessão de fibonacci
    return - soma da sucessão reciproca no termo n
    """

    k = 1
    sum = 0

    while k <= n:
        sum += 1.0 / fibonacci(k)
        k += 1
    return sum

# outra forma de calcular a soma da constante reciproca recursivamente
def reciprocoFibonacci2(n, soma):
    if n == 0:
        print("não existe o termo 0 da sucessão")
    else:
        soma += (1 / fibonacci(n))
        if n != 1:
            return reciprocoFibonacci2(n - 1, soma)
    return soma

#ex 1.c)
def reciprocoFibonacciComErro(n, erro):
    k = 1
    sum = 0.0
    term = 1
    last_term = 1

    while k <= n:
        sum += 1.0 / fibonacci(k)
        if k > 2:
            last_term = sum
            term = 1.0 / fibonacci(k) + sum
            print("erro: ", abs((last_term - term) / last_term))
            if math.sqrt(((last_term - term) / last_term) ** 2)  <= erro:
                break
        k += 1
    return sum

if __name__ == "__main__":
    erro = 0.001
    print(fibonacci(20))
    print(reciprocoFibonacci(4))
    print()
    print(reciprocoFibonacci(50))
    print(reciprocoFibonacci2(2, 0))
    print(reciprocoFibonacci2(3, 0))
    print(reciprocoFibonacci2(4, 0))
    print( "lala", reciprocoFibonacciComErro(1000, erro))
pass
