import unittest

from obsluga_ruchow.sprawdzanie_ruchow import stworz_tablice
from obsluga_ruchow.sprawdzanie_ruchow import sprawdz_pola
from stale.stale import GRACZ
from stale.stale import KOMPUTER
from stale.stale import PUSTO


class Postaw_Znak_Tests(unittest.TestCase):

    def setUp(self):
        self.plansza = stworz_tablice()

    def test_kolumny1(self):
        self.plansza[0][1] = GRACZ
        self.plansza[1][1] = GRACZ
        self.plansza[2][1] = GRACZ
        wynik = sprawdz_pola(self.plansza)
        self.assertTrue(wynik)

    def test_kolumny2(self):
        self.plansza[1][0] = PUSTO
        self.plansza[2][0] = PUSTO
        self.plansza[0][0] = PUSTO
        wynik = sprawdz_pola(self.plansza)
        self.assertFalse(wynik)

    def test_wiersze(self):
        self.plansza[0][0] = KOMPUTER
        self.plansza[0][1] = KOMPUTER
        self.plansza[0][2] = KOMPUTER
        wynik = sprawdz_pola(self.plansza)
        self.assertTrue(wynik)

    def test_po_skosie1(self):
        self.plansza[0][0] = GRACZ
        self.plansza[1][1] = GRACZ
        self.plansza[2][2] = GRACZ
        wynik = sprawdz_pola(self.plansza)
        self.assertTrue(wynik)

    def test_po_skosie2(self):
        self.plansza[0][2] = GRACZ
        self.plansza[1][1] = KOMPUTER
        self.plansza[2][0] = KOMPUTER
        wynik = sprawdz_pola(self.plansza)
        self.assertFalse(wynik)

    def test_kto_wygral(self):
        self.plansza[1][0] = GRACZ
        self.plansza[2][0] = GRACZ
        self.plansza[0][0] = GRACZ
        wynik = sprawdz_pola(self.plansza)
        self.assertTrue(wynik == GRACZ)

    def test_kto_wygral2(self):
        self.plansza[1][0] = GRACZ
        self.plansza[2][0] = GRACZ
        self.plansza[0][0] = GRACZ
        wynik = sprawdz_pola(self.plansza)
        self.assertFalse(wynik == KOMPUTER)


if __name__ == '__main__':
    unittest.main()
