import unittest

from app.dreptunghi import Dreptunghi


class TestDreptunghi(unittest.TestCase):
    def setUp(self) -> None:
        self.dreptunghi = Dreptunghi(2, 3, 'rosu')
        # self.dreptunghi.lungime = 2
        # self.dreptunghi.latime = 3
        # self.dreptunghi.culoare = 'rosu'

    def tearDown(self) -> None:
        pass

    # metode de test
    def test_descrie(self):
        desc_dreptunghi = f'Dreptunghiul are lungimea {self.dreptunghi.lungime}, latimea {self.dreptunghi.latime} si culoarea {self.dreptunghi.culoare}.'
        print(f'{self.dreptunghi.lungime}, {self.dreptunghi.latime}, {self.dreptunghi.culoare}')
        # print(f'{self.dreptunghi.descrie()}')
        self.assertTrue(print(f'{desc_dreptunghi}') == self.dreptunghi.descrie())

    def test_aria(self):
        assert self.dreptunghi.aria() == 6

    def test_perimetrul(self):
        assert self.dreptunghi.perimetrul()

    def test_schimba_culoarea(self):
        culoare_noua = self.dreptunghi.schimba_culoarea('verde')
        print(f'{self.dreptunghi.culoare}')
        self.assertTrue(print(f'{self.dreptunghi.culoare }') == culoare_noua)
        # self.assertTrue(self.dreptunghi.culoare == 'verde')
