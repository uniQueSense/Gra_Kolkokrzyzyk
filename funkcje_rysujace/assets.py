from funkcje_rysujace.klasy import Tekst
from dane import kolory
from dane import stale



class Assets:
    """ Informacje zawarte w menu """

    @staticmethod
    def load(okno):
        Assets.ZASADY1 = Tekst(stale.OSX_INFO, stale.OSY_INFO, kolory.KOLOR_TEKSTU, stale.OPIS_ROZM, stale.CZCIONKA,
                               'Witaj w grze Kółko i krzyżyk!').napisz(okno)
        Assets.ZASADY2 = Tekst(stale.OSX_INFO, stale.OSY_INFO + 30, kolory.KOLOR_TEKSTU, stale.OPIS_ROZM, stale.CZCIONKA, 'Zasady gry:').napisz(
            okno)
        Assets.ZASADY3 = Tekst(stale.OSX_INFO, stale.OSY_INFO + 60, kolory.KOLOR_TEKSTU, stale.OPIS_ROZM, stale.CZCIONKA,
                               '1. Gra jest toczona pomiędzy graczem a komputerem.').napisz(okno)
        Assets.ZASADY4 = Tekst(stale.OSX_INFO, stale.OSY_INFO + 90, kolory.KOLOR_TEKSTU, stale.OPIS_ROZM,stale. CZCIONKA,
                               '2. Gracz oraz przeciwnik rozstawiają na planszy po trzy swoje pionki.').napisz(okno)
        Assets.ZASADY5 = Tekst(stale.OSX_INFO, stale.OSY_INFO + 120, kolory.KOLOR_TEKSTU, stale.OPIS_ROZM, stale.CZCIONKA,
                               '3. Po rozstawieniu w systemie turowym,').napisz(okno)
        Assets.ZASADY6 = Tekst(stale.OSX_INFO, stale.OSY_INFO + 150, kolory.KOLOR_TEKSTU, stale.OPIS_ROZM, stale.CZCIONKA,
                               '    każdy z grających wybiera pionek').napisz(okno)
        Assets.ZASADY7 = Tekst(stale.OSX_INFO, stale.OSY_INFO + 180, kolory.KOLOR_TEKSTU, stale.OPIS_ROZM, stale.CZCIONKA,
                               '    oraz pole puste,na które chce przenieść pionek.').napisz(okno)
        Assets.ZASADY8 = Tekst(stale.OSX_INFO, stale.OSY_INFO + 210, kolory.KOLOR_TEKSTU, stale.OPIS_ROZM, stale.CZCIONKA,
                               '4. Gra toczy się do momentu, w którym jeden z graczy').napisz(okno)
        Assets.ZASADY9 = Tekst(stale.OSX_INFO, stale.OSY_INFO + 240, kolory.KOLOR_TEKSTU, stale.OPIS_ROZM, stale.CZCIONKA,
                               '    ustawi w jednym rzędzie swoje 3 pionki.').napisz(okno)
