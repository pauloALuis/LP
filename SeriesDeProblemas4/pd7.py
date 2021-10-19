"""
pd7.py
25/08/2021
"""

class IteradorRuas(object):
    def __init__(self, nome, c, l):
        self.nome = nome
        self.c = c
        self.l = l

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        return self

    def __str__(self):
        return "Rua: " + self.nome + " Comprimento: " + str(self.c) + " Largura: " + str(self.l) 

it_ruas = IteradorRuas("Travessa Bonita ", 10, 20 )
it = iter(it_ruas)

#6.c)
class Cidade(object):
    def __init__(self, nome, it_ruas):
        self.nome = nome
        self.it_ruas = it_ruas
        self.n = 0
        
    def add_rua(self):
        self.n += 1

    def __str__(self):
        if self.n == 0:
            return "Esta cidade não tem ruas"
        else:
            s ="A cidade " + self.nome + " tem as seguintes ruas:\n"
            for _ in range(0, self.n):
                s += str(next(self.it_ruas)) + "\n"
        return s

it_ruas2 = IteradorRuas("Travessa Bonita ", 10, 20 )
it2 = iter(it_ruas2)
cidade = Cidade("Cidadezorra", it2)
for i in range(3):
    cidade.add_rua()
print(cidade)