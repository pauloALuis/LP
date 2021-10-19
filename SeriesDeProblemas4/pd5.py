"""
pd5.py
24/08/2021
"""

#5.a)
class Planta(object):
    def __init__(self, nome_cientifico, nome_comum):
        self.cientifico = nome_cientifico
        self.comum = nome_comum

#5.b)
class Arvore(Planta):
    def __init__(self, nome_cientifico, nome_comum):
        super().__init__(nome_cientifico, nome_comum)

#5.c)
def f3(obj: object):
    if obj == Planta:
        return Arvore
    else:
        return obj

print(f3(Planta))

#5.d)
class ArvoreEstendida(Arvore):
    def __init__(self, nome_cientifico, nome_comum, l : list):
        super().__init__(nome_cientifico, nome_comum)
        self.l = l
    
    def __str__(self):
        s = ""
        for el in self.l:
            s += el + "\n"
        return "Nome cientifico: " + self.cientifico + "\nNome Comum: " + self.comum + "\nInfo:\n" + s 

arv_est = ArvoreEstendida("cientifico", "comum", ["bonita", "alta", "verde"])
print(arv_est)

