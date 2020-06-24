import unittest

from dane import stale
from funkcje_rysujace import obszar_gry
from obsluga_ruchow import poruszanie


class Poruszanie_Pionka_Tests(unittest.TestCase):

    def setUp(self):
        self.plansza = obszar_gry.stworz_tablice()

    def test_poruszanie1(self):
        self.plansza[1][1] = stale.GRACZ
        self.plansza[1][2] = stale.KOMPUTER
        wynik = poruszanie.porusz_znak(1, 1, 1, 2, stale.GRACZ, self.plansza)[0]
        self.assertNotEqual(wynik, stale.KOMPUTER)

    def test_poruszanie2(self):
        self.plansza[0][0] = stale.GRACZ
        self.plansza[0][0] = stale.GRACZ
        wynik = poruszanie.porusz_znak(0, 0, 0, 0, stale.GRACZ, self.plansza)[0]
        self.assertEqual(wynik, stale.GRACZ)

    def test_poruszanie3(self):
        self.plansza[0][0] = stale.GRACZ
        self.plansza[2][2] = stale.KOMPUTER
        wynik = poruszanie.porusz_znak(0, 0, 2, 2, stale.KOMPUTER, self.plansza)[0]
        self.assertEqual(wynik, stale.KOMPUTER)



if __name__ == '__main__':
    unittest.main()
