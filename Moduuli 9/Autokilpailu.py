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


autot=[]

for i in range(1, 11):
    rekisteritunnus=f"ABC-{i}"
    huippunopeus=random.randint(100, 200)
    auto=Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)

kilpailu_kaynnissa=True

while kilpailu_kaynnissa:
    for auto in autot:
        muutosnopeus=random.randint(-10, 15)
        auto.kiihdyta(muutosnopeus)

        auto.kulje(1)

        if auto.kuljettumatka>=10000:
            kilpailu_kaynnissa=False
            break



print("Kilpailu on päättynyt. Tulokset:")
print(f"{'Rekisteritunnus': <15} {'Huippunopeus (km/h)': <20} {'Tämänhetkinen nopeus (km/h)': <30} {'Kuljettu matka (km)': <20}")
print("-" * 85)
for auto in autot:
    print(f"{auto.rekisteri:<15} {auto.huippunopeus:<20} {auto.hetkinopeus:<30} {auto.kuljettumatka:<20}")
