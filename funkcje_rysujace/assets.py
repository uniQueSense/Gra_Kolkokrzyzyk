from funkcje_rysujace.klasy import Tekst
from stale.stale import CZCIONKA
from stale.stale import KOLOR_TEKSTU
from stale.stale import OPIS_ROZM
from stale.stale import OSX_INFO
from stale.stale import OSY_INFO


class Assets:
    """ Informacje zawarte w menu """

    @staticmethod
    def load(okno):
        Assets.ZASADY1 = Tekst(OSX_INFO, OSY_INFO, KOLOR_TEKSTU, OPIS_ROZM, CZCIONKA,
                               'Witaj w grze Kółko i krzyżyk!').napisz(okno)
        Assets.ZASADY2 = Tekst(OSX_INFO, OSY_INFO + 30, KOLOR_TEKSTU, OPIS_ROZM, CZCIONKA, 'Zasady gry:').napisz(okno)
        Assets.ZASADY3 = Tekst(OSX_INFO, OSY_INFO + 60, KOLOR_TEKSTU, OPIS_ROZM, CZCIONKA,
                               '1. Gra jest toczona pomiędzy graczem a komputerem.').napisz(okno)
        Assets.ZASADY4 = Tekst(OSX_INFO, OSY_INFO + 90, KOLOR_TEKSTU, OPIS_ROZM, CZCIONKA,
                               '2. Gracz oraz przeciwnik rozstawiają na planszy po trzy swoje pionki.').napisz(okno)
        Assets.ZASADY5 = Tekst(OSX_INFO, OSY_INFO + 120, KOLOR_TEKSTU, OPIS_ROZM, CZCIONKA,
                               '3. Po rozstawieniu w systemie turowym,').napisz(okno)
        Assets.ZASADY6 = Tekst(OSX_INFO, OSY_INFO + 150, KOLOR_TEKSTU, OPIS_ROZM, CZCIONKA,
                               '    każdy z grających wybiera pionek').napisz(okno)
        Assets.ZASADY7 = Tekst(OSX_INFO, OSY_INFO + 180, KOLOR_TEKSTU, OPIS_ROZM, CZCIONKA,
                               '    oraz pole puste,na które chce przenieść pionek.').napisz(okno)
        Assets.ZASADY8 = Tekst(OSX_INFO, OSY_INFO + 210, KOLOR_TEKSTU, OPIS_ROZM, CZCIONKA,
                               '4. Gra toczy się do momentu, w którym jeden z graczy').napisz(okno)
        Assets.ZASADY9 = Tekst(OSX_INFO, OSY_INFO + 230, KOLOR_TEKSTU, OPIS_ROZM, CZCIONKA,
                               '    ustawi w jednym rzędzie swoje 3 pionki.').napisz(okno)
