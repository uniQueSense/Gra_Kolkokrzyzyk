import unittest

from dane import stale
from funkcje_rysujace import obszar_gry
from obsluga_ruchow import poruszanie


class Poruszanie_Pionka_Tests(unittest.TestCase):

    def setUp(self):
        self.plansza = obszar_gry.stworz_tablice()

    def test_porszanie1(self):
        self.osx0 = 1
        self.osy0 = 1
        self.osx1 = 2
        self.osy1 = 1
        self.plansza[self.osy0][self.osx0] == stale.GRACZ
        self.plansza[self.osy1][self.osx1] == stale.KOMPUTER
        wynik = poruszanie.porusz_znak(self.osy0, self.osx0, self.osy1, self.osx1, stale.GRACZ, self.plansza)[0]
        self.assertFalse(wynik == stale.KOMPUTER)

    def test_porszanie2(self):
        self.osx0 = 0
        self.osy0 = 0
        self.osx1 = 0
        self.osy1 = 0
        self.plansza[self.osy0][self.osx0] == stale.GRACZ
        self.plansza[self.osy1][self.osx1] == stale.GRACZ
        wynik = poruszanie.porusz_znak(self.osy0, self.osx0, self.osy1, self.osx1, stale.GRACZ, self.plansza)[0]
        self.assertTrue(wynik == stale.GRACZ)

    def test_porszanie3(self):
        self.osx0 = 0
        self.osy0 = 0
        self.osx1 = 2
        self.osy1 = 2
        self.plansza[self.osy0][self.osx0] == stale.GRACZ
        self.plansza[self.osy1][self.osx1] == stale.KOMPUTER
        wynik = poruszanie.porusz_znak(self.osy0, self.osx0, self.osy1, self.osx1, stale.KOMPUTER, self.plansza)[0]
        self.assertTrue(wynik == stale.KOMPUTER)



if __name__ == '__main__':
    unittest.main()
