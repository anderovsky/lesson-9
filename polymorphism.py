class Shape:
    def area(self):
        raise NotImplementedError("Objekt nemá implementovanú metódu")

class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return (self.a * self.b) / 2

rectangle = Rectangle(a=5, b=7)
print(rectangle.area())


#platba - vypise rozne moznosti platby - karta, paypal, hotovost
# class Platba:
#     def zaplat(self):
#         raise NotImplementedError("Chyba")
#
# class kreditna_karta(Platba):
#     def zaplat(self, suma):
#         suma.self = suma
#         return f"Zaplatil si {suma} kreditnou kartou"
#
# class kreditna_karta(Platba):
#     def zaplat(self):
#         return "Zaplatil si kreditnou kartou"

# def vypis_transakciu(platba):
#     return platba.zaplat()

class Platba:
    def __init__(self, suma):
        self.suma = suma

class kreditna_karta(Platba):
    def zaplat(self):
        return "Zaplatil si kreditnou kartou"

def zaplat(self, suma):


karta = kreditna_karta()
print(karta.zaplat())
