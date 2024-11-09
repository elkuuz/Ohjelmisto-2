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


auto=Auto("ABC-123", 142 )

print(f"Uuden auton rekisteri on {auto.rekisteri} ja huippunopeus on {auto.huippunopeus}")
print(f"Uuden auton hetkellinen nopeus on {auto.hetkinopeus} ja kuljettumatka on {auto.kuljettumatka}")


auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)

print(f"Auton tämänhetkinen nopeus {auto.hetkinopeus} km/h")

auto.kiihdyta(-200)

print(f"Auton tämänhetkinen nopeus hätäjarrutuksen jälkeen on {auto.hetkinopeus} km/h")

auto.kiihdyta(60)

auto.kuljettumatka=2000

auto.kulje(1.5)

print(f"Kuljettu matka on {auto.kuljettumatka} kmh")