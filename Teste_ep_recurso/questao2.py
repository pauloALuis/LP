"""
Paulo Luis 17359
questao2.py
31/08/2021
"""

import pickle

class Mobilia():
    """
    Classe que representa uma mobilia com um nome, uma cor, um material e um preço
    """
    n = 1
    def __init__(self, nome: str, cor : hex, material : str, preco: float):
        self.__id__ = Mobilia.n        
        Mobilia.n += 1
        self.nome = nome
        self.cor = cor
        self.material = material
        self.preco = preco

    def __str__(self):
        return "ID: "+ self.__id__ + " - Mobilia " + self.nome + " - Cor " + str(self.cor) + " - Material " + self.material + " - Preço -> " + str(self.preco) + "€" 

class ListaFabricantesMobilia(Mobilia, list):
    """
    Classe que reprenta a lista de fabricantes de uma mobilia
    Esta classe deriva de Mobilia e de lista
    """
    def __init__(self, nome, cor, material, preco, fabricantes: list):
        super(ListaFabricantesMobilia, self).__init__(nome, cor, material, preco)
        for el in fabricantes:
            print("elemento: ", el)
            self.append(el)

    def add_fabricante(self, fabricante : str):
        self.append(fabricante)

    def __str__(self):
        s = "Mobilia: " + self.nome + " - Fabricantes: \n"
        for el in self:
            s += el + "\n"
        return s

#lista de tuplos com 4 elementos
moblist = [
    ("mobilia1", hex(40), "madeira", 30.99),
    ("mobilia2", hex(50), "ferro", 40.20),
    ("mobilia3", hex(22), "aço", 20.56),
    ("mobilia4", hex(39), "pedra", 10.89),
    ("mobilia5", hex(105), "ouro", 99.99)
    ]

#compreensão de listas para criar a mobilia_list
mobilia_list = [Mobilia(el[0], el[1], el[2], el[3]) for el in moblist]

fab = ListaFabricantesMobilia(mobilia_list[0].nome, mobilia_list[0].cor, mobilia_list[0].material, mobilia_list[0].preco, ["fab_1", "fab_2"])
print(fab)

file_name = "moblist.pkl"
def serialize_moblist(file_name, mobilia_list):
    """
    função que armazena a moblist num ficheiro de serialização através da biblioteca pickle
    """
    file = open(file_name, "wb")
    pickle.dump(mobilia_list, file)
    file.close()

def deserialize_moblist(file_name: str):
    """
    função que desserializa a moblist
    @param file_name : node do ficheiro de serialização
    @return lista moblist descerializada
    """
    objects = []
    file = open(file_name, "rb")
    loaded_list = pickle.load(file)
    objects.append(pickle.load(file)) 
    file.close()

        
        
    return objects
    


serialize_moblist(file_name, mobilia_list)
mobilia_list2 = deserialize_moblist(file_name)

print(mobilia_list2)