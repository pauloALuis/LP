"""
pd3.py
23/08/2021
"""
#3.a)
class ObraArte:
    def __init__(self, nome1, data1, preco):
        self.nome1 = nome1
        self.data1 = data1
        self.preco = preco
    
    def __str__(self):
        return "Obra de Arte : nome - " + str(self.nome1) + "; data - " + str(self.data1) + "; preco - " + str(self.preco)

#3.b)
class Museu:
    def __init__(self, nome2, morada, data2):
        self.nome2 = nome2
        self.morada = morada
        self.data2 = data2

    def __str__(self):
        return str("Museu : nome - " + self.nome2 + "; morada - " + self.morada + "; data - " + self.data2)

#3.c)
class AutorObra:
    def __init__(self, nome3, data_nas, nacionalidade):
        self.nome3 = nome3
        self.data_nas = data_nas
        self.nacionalidade = nacionalidade
    
    def __str__(self):
        return "Autor da Obra : nome - " + self.nome2 + "; data de nascimento - " + self.data_nas + "; nacionalidade - " + self.nacionalidade

#3.d)
class ReferenciaObraCompleta(ObraArte, Museu, AutorObra):
    def __init__(self, nome1, data1, preco, nome2, morada, data2, nome3, data_nas, nacionalidade):
        self.obra = super(ObraArte, self).__init__(nome1, data1, preco)
        self.museu = super(Museu, self).__init__(nome2, morada, data2)
        self.autor = super(AutorObra, self).__init__(nome3, data_nas, nacionalidade)
    
    def __str__(self):
        return self.obra + self.museu + self.autor

ref = ReferenciaObraCompleta("obra arte", "2/2/2020", "10€", "museu", "travessa 2", "3/3/2021", "autor", "2/2/2020", "portuguesa")
print(ref)
