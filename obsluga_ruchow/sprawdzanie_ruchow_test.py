import unittest

from funkcje_rysujace.plansza import stworz_tablice
from obsluga_ruchow.sprawdzanie_ruchow import sprawdz_pola
from dane import stale



class Postaw_Znak_Tests(unittest.TestCase):

    def setUp(self):
        self.plansza = stworz_tablice()

    def test_kolumny1(self):
        self.plansza[0][1] = stale.GRACZ
        self.plansza[1][1] = stale.GRACZ
        self.plansza[2][1] = stale.GRACZ
        wynik = sprawdz_pola(self.plansza)
        self.assertTrue(wynik)

    def test_kolumny2(self):
        self.plansza[1][0] = stale.PUSTO
        self.plansza[2][0] = stale.PUSTO
        self.plansza[0][0] = stale.PUSTO
        wynik = sprawdz_pola(self.plansza)
        self.assertFalse(wynik)

    def test_wiersze(self):
        self.plansza[0][0] = stale.KOMPUTER
        self.plansza[0][1] = stale.KOMPUTER
        self.plansza[0][2] = stale.KOMPUTER
        wynik = sprawdz_pola(self.plansza)
        self.assertTrue(wynik)

    def test_po_skosie1(self):
        self.plansza[0][0] = stale.GRACZ
        self.plansza[1][1] = stale.GRACZ
        self.plansza[2][2] = stale.GRACZ
        wynik = sprawdz_pola(self.plansza)
        self.assertTrue(wynik)

    def test_po_skosie2(self):
        self.plansza[0][2] = stale.GRACZ
        self.plansza[1][1] = stale.KOMPUTER
        self.plansza[2][0] = stale.KOMPUTER
        wynik = sprawdz_pola(self.plansza)
        self.assertFalse(wynik)

    def test_kto_wygral(self):
        self.plansza[1][0] = stale.GRACZ
        self.plansza[2][0] = stale.GRACZ
        self.plansza[0][0] = stale.GRACZ
        wynik = sprawdz_pola(self.plansza)
        self.assertTrue(wynik == stale.GRACZ)

    def test_kto_wygral2(self):
        self.plansza[1][0] = stale.GRACZ
        self.plansza[2][0] = stale.GRACZ
        self.plansza[0][0] = stale.GRACZ
        wynik = sprawdz_pola(self.plansza)
        self.assertFalse(wynik == stale.KOMPUTER)


if __name__ == '__main__':
    unittest.main()
