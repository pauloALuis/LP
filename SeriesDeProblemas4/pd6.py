"""
pd6.py
25/08/2021
"""

#6.a)
class Stock(BaseException):
    def __init__(self, nome : str, stock : int):
        self.nome = nome
        self.stock = stock
        self.sem_stock = "Impossível aceder à ferramenta " + self.nome

    def __str__(self):
        return "Ferramenta: " + self.nome + "\nStock: " + str(self.stock)

    #6.b)
    def get_ferramenta(self):
        if self.stock < 1:
            try:
                raise self
            except BaseException as b:
                return self.sem_stock
        else:
            return self

ferramenta1 = Stock("ferramenta 1", 0)
ferramenta2 = Stock("bora bora", 10)
ferramenta3 = Stock("ferramenta 1", 15)
ferramenta4 = Stock("bora bora", 20)
ferramenta5 = Stock("ferramenta 1", 30)
ferramenta6 = Stock("bora bora", 35)
ferramenta7 = Stock("ferramenta 1", 40)
ferramenta8 = Stock("bora bora", 45)

#print(ferramenta1.get_ferramenta())
#print(ferramenta2.get_ferramenta())

#6.c)
class ConjuntoStock(set):
    def __init__(self, st: set):
        super(ConjuntoStock, self).__init__(st)
    
    def add_stock(self, stock: Stock):
        self.add(stock)
    
    def check_stocks(self):
        sum = 0
        for i in self:
            sum += i.stock
        if sum < 100:
            try:
                raise BaseException(self)
            except BaseException:
                return "algo está errado neste conjunto! a soma de stocks é inferior a 100"
        else:
            return "A soma de stcoks é " + str(sum) + "!!"


set1 = ConjuntoStock({ferramenta1, ferramenta2, ferramenta3, ferramenta4, ferramenta5})
set2 = ConjuntoStock({ferramenta6, ferramenta7, ferramenta8})

print(set1.check_stocks())
print(set2.check_stocks())

#6.c)


