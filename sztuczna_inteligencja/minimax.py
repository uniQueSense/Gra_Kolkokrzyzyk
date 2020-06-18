from obsluga_ruchow.sprawdzanie_ruchow import sasiadujace
from obsluga_ruchow.sprawdzanie_ruchow import sprawdz_pola
from stale.stale import GRACZ
from stale.stale import INF
from stale.stale import ILOSC_WIERSZY
from stale.stale import ILOSC_KOLUMN
from stale.stale import KOMPUTER
from stale.stale import PUSTO


def ocena_pola(plansza):
    """ Ocena planszy w funkcji minimax"""
    if sprawdz_pola(plansza) == KOMPUTER:
        return 10
    elif sprawdz_pola(plansza) == GRACZ:
        return -10
    else:
        return 0


def puste_pola(plansza):
    """ Zapisuje indexy pustych pól w grze """
    index = []
    for kol in range(ILOSC_KOLUMN):
        for wiersz in range(ILOSC_WIERSZY):
            if plansza[wiersz][kol] == PUSTO:
                index.append((wiersz, kol))
    return index


def pola_zajete(plansza):
    """ Zapisuje indexy zajętych pól w grze """
    index = []
    for kol in range(ILOSC_KOLUMN):
        for wiersz in range(ILOSC_WIERSZY):
            if plansza[wiersz][kol] != PUSTO:
                index.append((wiersz, kol))
    return index


def minimax_ustawianie(poziom, max, plansza):
    """ Funkcja minimax do etapu rozstawiania pionków """
    puste = puste_pola(plansza)
    if not poziom or not len(puste):
        return None, ocena_pola(plansza)
    if max:
        index = puste[0]
        wartosc = -INF
        for wiersz, kol in puste:
            tab = [[kol for kol in wiersz] for wiersz in plansza]
            tab[wiersz][kol] = KOMPUTER
            k, stan = minimax_ustawianie(poziom - 1, False, tab)
            if stan >= wartosc:
                wartosc = stan
                index = [wiersz, kol]
        return index, wartosc
    else:
        index = puste[0]
        wartosc = INF
        for wiersz, kol in puste:
            tab = [[kol for kol in wiersz] for wiersz in plansza]
            tab[wiersz][kol] = GRACZ
            k, stan = minimax_ustawianie(poziom - 1, True, tab)
            if stan < wartosc:
                wartosc = stan
                index = [wiersz, kol]
        return index, wartosc


def minimax_przemieszczanie(poziom, max, plansza):
    """ Funkcja minimax do etapu przemieszczania pionków """
    zajete = pola_zajete(plansza)
    puste = puste_pola(plansza)
    if not poziom:
        return None, None, ocena_pola(plansza)
    elif max:
        index0 = zajete[0]
        index1 = puste[0]
        wartosc = -INF
        for wiersz, kol in zajete:
            tab = [[kol for kol in wiersz] for wiersz in plansza]
            for wiersz_wstaw, kol_wstaw in puste:
                if sasiadujace(kol, wiersz, kol_wstaw, wiersz_wstaw) and tab[wiersz][kol] == KOMPUTER:
                    tab[wiersz][kol] = PUSTO
                    tab[wiersz_wstaw][kol_wstaw] = KOMPUTER
                    k, j, stan = minimax_przemieszczanie(poziom - 1, False, tab)
                    if stan > wartosc:
                        wartosc = stan
                        index0 = [wiersz, kol]
                        index1 = [wiersz_wstaw, kol_wstaw]
        return index0, index1, wartosc
    else:
        index0 = zajete[0]
        index1 = puste[0]
        wartosc = INF
        for wiersz, kol in zajete:
            tab = [[kol for kol in wiersz] for wiersz in plansza]
            for wiersz_wstaw, kol_wstaw in puste:
                if sasiadujace(kol, wiersz, kol_wstaw, wiersz_wstaw) and tab[wiersz][kol] == GRACZ:
                    tab[wiersz][kol] = PUSTO
                    tab[wiersz_wstaw][kol_wstaw] = GRACZ
                    k, j, stan = minimax_przemieszczanie(poziom - 1, True, tab)
                    if stan < wartosc:
                        wartosc = stan
                        index0 = [wiersz, kol]
                        index1 = [wiersz_wstaw, kol_wstaw]
        return index0, index1, wartosc
