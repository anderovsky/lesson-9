class City:
    def __init__(self, name, region, country, citizens, zip, area):
        self.name = name
        self.region = region
        self.country = country
        self.citizens = citizens
        self.zip = zip
        self.area = area

    def full_adress(self):
        print(f"Adresa ktorú hľadáte je v meste: {self.name}, v regióne: {self.region}, krajine: {self.country}, má {self.citizens} obyvateľov a PSČ je {self.zip} v oblasti: {self.area}")

bratislava = City(name="Bratislava", region="Západoslovenský kraj", country="Slovensko", citizens=475503, zip=83102, area="Bratislava")
bratislava.full_adress()
print(bratislava.citizens)