class Cerc:
    raza = 0
    culoare = None

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(f'Cercul are culoarea {self.culoare} si raza {self.raza}.')

    def aria(self):
        s = self.raza ** 2
        return s

    def diametru(self):
        d = self.raza * 2
        return d

    def circumferinta(self, raza):
        pi = 3.14
        l = 2 * pi * raza
        return l