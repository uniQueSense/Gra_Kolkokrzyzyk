from dane import kolory
from dane import stale
from funkcje_rysujace import klasy

ZASADY = [
    'Witaj w grze Kółko i krzyżyk!',
    'Zasady gry:',
    '1. Gra jest toczona pomiędzy graczem a komputerem.',
    '2. Gracz oraz przeciwnik rozstawiają na planszy po trzy swoje pionki.',
    '3. Po rozstawieniu w systemie turowym,',
    '    każdy z grających wybiera pionek',
    '    oraz pole puste,na które chce przenieść pionek.',
    '4. Gra toczy się do momentu, w którym jeden z graczy',
    '    ustawi w jednym rzędzie swoje 3 pionki.']


class Assets:
    # Informacje zawarte w menu

    assetZasady = None

    @staticmethod
    def load():
        Assets.assetZasady = [
            klasy.Tekst(stale.OSX_INFO, stale.OSY_INFO + 30 * i, kolory.KOLOR_TEKSTU, stale.OPIS_ROZM, stale.CZCIONKA,
                        x) for i, x in enumerate(ZASADY)]

    @staticmethod
    def napisz(okno):
        for x in Assets.assetZasady:
            x.napisz(okno)
