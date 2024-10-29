class Julkaisu:

    julkaisu_maara=0

    def __init__(self, nimi, etunimi, sukunimi):
        Julkaisu.julkaisu_maara=Julkaisu.julkaisu_maara+1
        self.nimi=nimi
        self.etunimi = etunimi
        self.sukunimi = sukunimi

    def tulosta_tiedot(self):
        print(f"{self.nimi}, {self.etunimi} {self.sukunimi}")

class Lehti(Julkaisu):
    def __init__(self, nimi, etunimi, sukunimi):
        super().__init__(nimi, etunimi, sukunimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()


class Kirja(Julkaisu):
    def __init__(self, nimi, etunimi, sukunimi, sivumaara):
        super().__init__(nimi, etunimi, sukunimi)
        self.sivumaara=sivumaara 

        
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"{self.sivumaara} sivua\n ")

julkaisut=[]
julkaisut.append(Kirja("Hytti n:o 6", "Rosa", "Liksom", 200))
julkaisut.append(Lehti("Aku Ankka", "Aki", "Hyyppä" ))

for j in julkaisut:
    j.tulosta_tiedot()