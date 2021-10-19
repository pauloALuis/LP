#!/usr/bin/env python3

"""
p37.py
2020/11/5
"""

def emprestimo(valor, anos, spread = 0.03, costs = 0.003):
    meses = anos * 12
    juros = (spread - costs) / 12
    juros_mes =  ( 1 + juros) ** meses
    return  valor * ((juros * juros_mes) / (juros_mes - 1))

if __name__ == "__main__" :
    print("Prestação por mês:", emprestimo(100000, 5),"€")
pass