import unittest

from app.cerc import Cerc


class TestCerc(unittest.TestCase):
    def setUp(self) -> None:
        self.cerc = Cerc(raza=5, culoare='verde')

    def tearDown(self) -> None:
        pass

    def test_descrie_cerc(self):
        text = f'Cercul are culoarea {self.cerc.culoare} si raza {self.cerc.raza}.'
        assert print(text) == self.cerc.descrie_cerc()

    def test_aria(self):
        assert self.cerc.aria() == 25

    def test_diametru(self):
        assert self.cerc.diametru() == 10

    def test_circumferinta(self):
        print(f'{self.cerc.circumferinta(5)}')
        assert self.cerc.circumferinta(self.cerc.raza) == 2*5*3.14
