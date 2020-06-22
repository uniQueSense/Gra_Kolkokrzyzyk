from stale.stale import GRACZ
from stale.stale import ILOSC_KOLUMN
from stale.stale import ILOSC_WIERSZY
from stale.stale import KOMPUTER


def sprawdz_pola(plansza):
    """ Sprawdzanie czy ktoś nie wygrał i zawracanie zwyciezcy """
    for kolumna in range(ILOSC_KOLUMN):
        if plansza[0][kolumna] == plansza[1][kolumna] == plansza[2][kolumna]:
            if plansza[0][kolumna] == GRACZ:
                return GRACZ
            elif plansza[0][kolumna] == KOMPUTER:
                return KOMPUTER
    for wiersz in range(ILOSC_WIERSZY):
        if plansza[wiersz][0] == plansza[wiersz][1] == plansza[wiersz][2]:
            if plansza[wiersz][0] == GRACZ:
                return GRACZ
            elif plansza[wiersz][0] == KOMPUTER:
                return KOMPUTER
    if plansza[0][0] == plansza[1][1] == plansza[2][2]:
        if plansza[0][0] == GRACZ:
            return GRACZ
        elif plansza[0][0] == KOMPUTER:
            return KOMPUTER
    if plansza[0][2] == plansza[1][1] == plansza[2][0]:
        if plansza[1][1] == GRACZ:
            return GRACZ
        elif plansza[1][1] == KOMPUTER:
            return KOMPUTER
    return 0


def sasiadujace(osx0, osy0, osx1, osy1):
    """ Sprawdza czy pionek sasiaduje z wybranym polem """
    if abs(osx1 - osx0) <= 1 and abs(osy1 - osy0) <= 1:
        return True
    else:
        return False


def kto_wygral(punkt_gracz, punkt_ai, plansza):
    zwycięzca = sprawdz_pola(plansza)
    if zwycięzca:
        if zwycięzca == GRACZ:
            punkt_gracz += 1
        if zwycięzca == KOMPUTER:
            punkt_ai += 1
        zwycięzca = sprawdz_pola(plansza)
        return zwycięzca
    return False
