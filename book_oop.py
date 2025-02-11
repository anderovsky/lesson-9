class Kniha:
    def __init__(self, nazov: str, autor: str, isbn: str, rok_vydania: int):
        self.nazov = nazov
        self.autor = autor
        self.isbn = isbn
        self.rok_vydania = rok_vydania
        self.dostupna = True

    def vypozicat(self):
        if self.dostupna:
            self.dostupna = False
            return True
        return False

    def vratit(self):
        self.dostupna = True

    def __str__(self):
        return f"{self.nazov} ({self.rok_vydania}) - {self.autor} [ISBN: {self.isbn}] {'Dostupná' if self.dostupna else 'Vypožičaná'}"


class Kniznica:
    def __init__(self):
        self.knihy = []

    def pridat_knihu(self, kniha: Kniha):
        self.knihy.append(kniha)

    def vyhladat_podla_nazvu(self, nazov: str):
        return [k for k in self.knihy if nazov.lower() in k.nazov.lower()]

    def vypozicat_knihu(self, isbn: str):
        for kniha in self.knihy:
            if kniha.isbn == isbn and kniha.dostupna:
                return kniha.vypozicat()
        return False

    def vratit_knihu(self, isbn: str):
        for kniha in self.knihy:
            if kniha.isbn == isbn and not kniha.dostupna:
                kniha.vratit()
                return True
        return False

    def zobraz_dostupne_knihy(self):
        return [str(k) for k in self.knihy if k.dostupna]


# Príklad použitia
kniznica = Kniznica()
kniha1 = Kniha("1984", "George Orwell", "123456789", 1949)
kniha2 = Kniha("Malý princ", "Antoine de Saint-Exupéry", "987654321", 1943)

kniznica.pridat_knihu(kniha1)
kniznica.pridat_knihu(kniha2)

print("Dostupné knihy:", kniznica.zobraz_dostupne_knihy())
kniznica.vypozicat_knihu("123456789")
print("Po vypožičaní:", kniznica.zobraz_dostupne_knihy())
kniznica.vratit_knihu("123456789")
print("Po vrátení:", kniznica.zobraz_dostupne_knihy())
