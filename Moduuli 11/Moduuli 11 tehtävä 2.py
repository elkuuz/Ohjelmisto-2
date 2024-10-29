class Auto:
    def __init__(self, rekisteri, nopeus):
        self.rekisteri=rekisteri
        self.huippunopeus=nopeus
        self.hetkinopeus=0
        self.kuljettumatka=0

    def kiihdyta(self, muutos):
        uusinopeus=self.hetkinopeus+muutos

        if uusinopeus > self.huippunopeus:
            self.hetkinopeus = self.huippunopeus
        elif uusinopeus < 0:
            self.hetkinopeus = 0
        else:
            self.hetkinopeus = uusinopeus

    def kulje(self, tunnit):
        uusimatka=self.hetkinopeus*tunnit
        self.kuljettumatka+=uusimatka

    def tulosta_tiedot(self):
        print(f"Rekisteri: {self.rekisteri}, Huippunopeus: {self.huippunopeus} Mittarilukema: {self.kuljettumatka}")


class Sahkoauto(Auto):
    def __init__(self, rekister, nopeus, kilowatit):
        super().__init__(rekister, nopeus)
        self.kilowatit=kilowatit

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Sähköauton teho: {self.kilowatit}")


class Bensa_auto(Auto):
    def __init__(self, rekister, nopeus, tankki_litrat):
        super().__init__(rekister, nopeus)
        self.tankki_litrat=tankki_litrat

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Tankin koko: {self.tankki_litrat}")


autolista=[]
autolista.append(Sahkoauto("ABC-1", 150, 52.5 ))
autolista.append(Bensa_auto("ABC-2", 150, 32.3 ))

for i in autolista:
    i.kiihdyta(100)
    i.kulje(3)
    i.tulosta_tiedot()



