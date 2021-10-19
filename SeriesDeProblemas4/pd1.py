"""
pd1.py
23/08/2021
"""

#1.a)
class Bibliografia:
    def __init__(self, nome, ano, autor):
        self.nome = nome
        self.ano = ano
        self.autor = autor
    
#1.b
class Livro(Bibliografia):
    def __init__(self, nome, ano, autor, editora):
        super().__init__(nome, ano, autor)
        self.editora = editora

    #1.d)
    def change_livro(self, nome, ano, autor, editora):
        self.nome = nome
        self.ano = ano
        self.autor = autor
        self.editora = editora
    
    def print_book(self):
        print("nome: ", self.nome + "\nano ", str(self.ano), 
                "\nautor: ", self.autor, "\neditora: ", self.editora, "\n")
#1.c)
def get_book_refs(file_name : str = "books-refs.txt"):
    l = []
    f = open(file_name, "r")
    rows = f.readlines()
    for row in rows:
        r = row.split(" ")
        l.append(Livro(r[0], int(r[1]), r[2], r[3]))
    return l

l = get_book_refs()
for el in l:
    el.print_book()
l[0].change_livro("yooo", 2019, "Eu", "EditMaster")
print()
print("primeiro livro mudado:")
for el in l:
    el.print_book()


class Artigo(Bibliografia):
    def __init__(self, nome, ano, autor, jornal):
        super().__init__(nome, ano, autor)
        self.jornal = jornal
    

