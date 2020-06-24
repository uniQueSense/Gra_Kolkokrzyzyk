import unittest
from dane import stale
from funkcje_rysujace import obszar_gry
from obsluga_ruchow import sprawdzanie_ruchow


class Postaw_Znak_Tests(unittest.TestCase):

    def setUp(self):
        self.plansza = obszar_gry.stworz_tablice()

    def test_kolumny1(self):
        self.plansza[0][1] = stale.GRACZ
        self.plansza[1][1] = stale.GRACZ
        self.plansza[2][1] = stale.GRACZ
        self.assertTrue(sprawdzanie_ruchow.sprawdz_pola(self.plansza))

    def test_kolumny2(self):
        self.plansza[1][0] = stale.PUSTO
        self.plansza[2][0] = stale.PUSTO
        self.plansza[0][0] = stale.PUSTO
        self.assertFalse(sprawdzanie_ruchow.sprawdz_pola(self.plansza))

    def test_wiersze(self):
        self.plansza[0][0] = stale.KOMPUTER
        self.plansza[0][1] = stale.KOMPUTER
        self.plansza[0][2] = stale.KOMPUTER
        self.assertTrue(sprawdzanie_ruchow.sprawdz_pola(self.plansza))

    def test_po_skosie1(self):
        self.plansza[0][0] = stale.GRACZ
        self.plansza[1][1] = stale.GRACZ
        self.plansza[2][2] = stale.GRACZ
        self.assertTrue(sprawdzanie_ruchow.sprawdz_pola(self.plansza))

    def test_po_skosie2(self):
        self.plansza[0][2] = stale.GRACZ
        self.plansza[1][1] = stale.KOMPUTER
        self.plansza[2][0] = stale.KOMPUTER
        self.assertFalse(sprawdzanie_ruchow.sprawdz_pola(self.plansza))

    def test_kto_wygral(self):
        self.plansza[1][0] = stale.GRACZ
        self.plansza[2][0] = stale.GRACZ
        self.plansza[0][0] = stale.GRACZ
        wynik = sprawdzanie_ruchow.sprawdz_pola(self.plansza)
        self.assertEqual(wynik, stale.GRACZ)

    def test_kto_wygral2(self):
        self.plansza[1][0] = stale.GRACZ
        self.plansza[2][0] = stale.GRACZ
        self.plansza[0][0] = stale.GRACZ
        wynik = sprawdzanie_ruchow.sprawdz_pola(self.plansza)
        self.assertNotEqual(wynik, stale.KOMPUTER)


if __name__ == '__main__':
    unittest.main()
