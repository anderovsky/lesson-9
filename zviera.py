class Zviera:
    def hlas(self):
        raise NotImplementedError("nezadane zviera")

class Pes(Zviera):
    def hlas(self):
        return "Haf"

class Macka(Zviera):
    def hlas(self):
        return "Mnau"

def vydaj_zvuk(zviera):
    return zviera.hlas()

pes = Pes()
macka = Macka()

for x in [pes, macka]:
    print(vydaj_zvuk(x))