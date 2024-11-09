import random

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

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot


    def tunti_kuluu(self):
        for auto in self.autot:
            muutosnopeus = random.randint(-10, 15)
            auto.kiihdyta(muutosnopeus)
            auto.kulje(1)


    def tulosta_tilanne(self):
        print(f"\nKilpailu: {self.nimi}")
        print(f"Pituus: {self.pituus} km")
        print(
            f"{'Rekisteritunnus': <15} {'Huippunopeus (km/h)': <20} {'Tämänhetkinen nopeus (km/h)': <30} {'Kuljettu matka (km)': <20}")
        print("-" * 85)
        for auto in self.autot:
            print(f"{auto.rekisteri:<15} {auto.huippunopeus:<20} {auto.hetkinopeus:<30} {auto.kuljettumatka:<20}")

    def kilpailu_ohi(self):
        return any(auto.kuljettumatka>=self.pituus for auto in self.autot)





if __name__ == "__main__":
    autot=[]
    for i in range(1, 11):
        rekisteritunnus = f"ABC-{i}"
        huippunopeus = random.randint(100, 200)
        auto = Auto(rekisteritunnus, huippunopeus)
        autot.append(auto)

    kisa=Kilpailu("Suuri Romuralli", 8000, autot)

    tunti=0

    while not kisa.kilpailu_ohi():
        kisa.tunti_kuluu()
        tunti+=1

        if tunti % 10==0:
            kisa.tulosta_tilanne()

    kisa.tulosta_tilanne()
    print("Kilpailu on ohi!")
