class Dreptunghi:
    lungime = 0
    latime = 0
    culoare = None

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        print(f'Dreptunghiul are lungimea {self.lungime}, latimea {self.latime}'
              f' si culoarea {self.culoare}.')

    def aria(self):
        return self.lungime * self.latime

    def perimetrul(self):
        return 2*(self.lungime+self.latime)

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare
