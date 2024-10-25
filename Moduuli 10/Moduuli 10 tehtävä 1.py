class hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros=alin_kerros

    def kerros_ylos(self):
        if self.kerros<self.ylin_kerros:
            self.kerros+=1
            print(f"Hissi on nyt kerroksessa {self.kerros}")
        else:
            print("Hissi on jo ylimmässä kerroksessa")


    def kerros_alas(self):
        if self.kerros>self.alin_kerros:
            self.kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.kerros}")
        else:
            print("Hissi on jo alimmassa kerroksessa")

    def siirry_kerrokseen(self, valitse_kerros):
        if self.kerros>valitse_kerros:
            while valitse_kerros<self.kerros:
                self.kerros_alas()

        elif self.kerros<valitse_kerros:
            while self.kerros<valitse_kerros:
                self.kerros_ylos()

        else:
            print(f"Hissi on jo kerroksessa {valitse_kerros}")


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissi_maara):
        self.hissit=[hissi(alin_kerros, ylin_kerros) for _ in range(hissi_maara)]

    def aja_hissia(self, hissi_numero, kohdekerros):
        if 0<=hissi_numero<len(self.hissit):
            print(f"Hissiä {hissi_numero} ajetaan kerrokseen {kohdekerros}")
            self.hissit[hissi_numero].siirry_kerrokseen(kohdekerros)

    def palohalytys(self):
        print("Palohälytys!!")
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(hissi.alin_kerros)


talo=Talo(0,10,5)

talo.aja_hissia(0,10)
talo.aja_hissia(1,4)
talo.aja_hissia(2,3)
talo.aja_hissia(3,2)
talo.aja_hissia(4,9)
talo.aja_hissia(5,5)

talo.palohalytys()