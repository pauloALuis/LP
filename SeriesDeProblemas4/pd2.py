"""
pd2.py
23/08/2021
"""
#2.a)
class InstrumentoMusical:
    def __init__(self, nome, tipo, marca, preco):
        self.nome = nome
        self.tipo = tipo
        self.marca = marca
        self.preco = preco
        self.__nota = 0 # private variable convention
    
    #2.d)
    def __init__(self) -> None:
        pass    
    
    #2.c
    def get_nota(self):
        return self.__nota

    def set_nota(self, nota):
        self.__nota = nota
    #2.b)
    def __str__(self):
        return "Instrumento Musical: \nNome : " + self.nome + "\nTipo: " + self.tipo + "\nMarca: " + self.marca + "\nPreco: "+ str(self.preco)+ "€\nNota: " + str(self.__nota)

inst = InstrumentoMusical("Guitarra", "cordas", "fender", 200)
inst.set_nota(10)
print(inst)




