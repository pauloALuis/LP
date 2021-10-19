"""
pd8.py
25/08/2021
"""

class Filme():
    def __init__(self, nome, realizador, data):
        self.nome = nome
        self.realizador = realizador
        self.data = data

    def __str__(self):
        return "Filme: " + self.nome + " \nRealizador: " + self.realizador + " \nData: " + self.data + "\n"

class IteradorFilmes(object):
    def __init__(self, filmes: list[Filme]):
        self.filmes = filmes

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        self.n +=1
        return self.filmes[self.n -1]

#8.a)
class ColecaoFilmes(object):
    def __init__(self, nome, it_filmes):
        self.nome = nome
        self.it_filmes = it_filmes
        self.n = 0

    def __init__(self, nome, it_filmes):
        self.nome = nome
        self.it_filmes = it_filmes
        self.n = 0
        
    def add_filmes_to_colection(self):
        self.n += 1

    #8.b e 8.d)
    def __str__(self):
        if self.n == 0:
            return "Esta cidade não tem ruas"
        else:
            s ="A coleção de filmes e series designada de \"" + self.nome + "\" contem os:\n"
            for _ in range(0, self.n):
                s += str(next(self.it_filmes)) + "\n"
        return s

#8.c)
class FilmesSeries(Filme):
    def __init__(self, nome, realizador, data, episodios, temporadas):
        super().__init__(nome, realizador, data)
        self.episodios = episodios
        self.temporadas = temporadas
    
    #8.d)
    def __str__(self):
        return "Serie: " + self.nome + " \nRealizador: " + self.realizador + " \nData: " + self.data + "\nEpisodios: " + str(self.episodios) + "\nTemporadas: " + str(self.temporadas) + "\n"

filme1 = Filme("Filme demais", "Bernardo", "2/2/2")
filme2 = Filme("Filme bacano", "Martinho", "3/3/3")
filme3 = Filme("Filme bue bom", "Marques", "4/4/4")
filme4 = Filme("Filme do catano", "IP Beja", "5/5/5")
fs1 = FilmesSeries("Serie brutal", "Realizador1", "6/6/6", 20, 3)
fs2 = FilmesSeries("Serie potente", "Realizador2", "7/7/7", 30, 2)
fs3 = FilmesSeries("Serie do outro mundo", "Realizador3", "8/8/8", 50, 5)
fs4 = FilmesSeries("Serie bue baril", "Realizador4", "9/9/9", 100, 8)
it_filmes = IteradorFilmes([filme1, filme2, filme3, filme4, fs1, fs2, fs3, fs4])
it = iter(it_filmes)

filmes_colection = ColecaoFilmes("Filmes de Acção", it)
for i in range(8):
    filmes_colection.add_filmes_to_colection()
print(filmes_colection)

