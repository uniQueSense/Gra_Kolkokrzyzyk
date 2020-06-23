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
    # @staticmethod
    # def load(okno):
    #     Assets.ZASADY1 = Tekst(stale.OSX_INFO, stale.OSY_INFO, kolory.KOLOR_TEKSTU, stale.OPIS_ROZM, stale.CZCIONKA,
    #                            'Witaj w grze Kółko i krzyżyk!').napisz(okno)
    #     Assets.ZASADY2 = Tekst(stale.OSX_INFO, stale.OSY_INFO + 30, kolory.KOLOR_TEKSTU, stale.OPIS_ROZM,
    #                            stale.CZCIONKA, 'Zasady gry:')
    #     Assets.ZASADY3 = Tekst(stale.OSX_INFO, stale.OSY_INFO + 60, kolory.KOLOR_TEKSTU, stale.OPIS_ROZM,
    #                            stale.CZCIONKA, '1. Gra jest toczona pomiędzy graczem a komputerem.')
    #     Assets.ZASADY4 = Tekst(stale.OSX_INFO, stale.OSY_INFO + 90, kolory.KOLOR_TEKSTU, stale.OPIS_ROZM,
    #                            stale.CZCIONKA, '2. Gracz oraz przeciwnik rozstawiają na planszy po trzy swoje pionki.')
    #     Assets.ZASADY5 = Tekst(stale.OSX_INFO, stale.OSY_INFO + 120, kolory.KOLOR_TEKSTU, stale.OPIS_ROZM,
    #                            stale.CZCIONKA, '3. Po rozstawieniu w systemie turowym,').napisz(okno)
    #     Assets.ZASADY6 = Tekst(stale.OSX_INFO, stale.OSY_INFO + 150, kolory.KOLOR_TEKSTU, stale.OPIS_ROZM,
    #                            stale.CZCIONKA, '    każdy z grających wybiera pionek')
    #     Assets.ZASADY7 = Tekst(stale.OSX_INFO, stale.OSY_INFO + 180, kolory.KOLOR_TEKSTU, stale.OPIS_ROZM,
    #                            stale.CZCIONKA, '    oraz pole puste,na które chce przenieść pionek.')
    #     Assets.ZASADY8 = Tekst(stale.OSX_INFO, stale.OSY_INFO + 210, kolory.KOLOR_TEKSTU, stale.OPIS_ROZM,
    #                            stale.CZCIONKA, '4. Gra toczy się do momentu, w którym jeden z graczy')
    #     Assets.ZASADY9 = Tekst(stale.OSX_INFO, stale.OSY_INFO + 240, kolory.KOLOR_TEKSTU, stale.OPIS_ROZM,
    #                            stale.CZCIONKA, '    ustawi w jednym rzędzie swoje 3 pionki.')
