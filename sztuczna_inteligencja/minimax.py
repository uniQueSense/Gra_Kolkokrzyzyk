from obsluga_ruchow.spr import *
from stale.stale import KOMPUTER, GRACZ, PUSTO


def ocena_pola(plansza):
    if sprawdz_pola(plansza) == KOMPUTER:
        return 10
    elif sprawdz_pola(plansza) == GRACZ:
        return -10
    else:
        return 0


def puste_pola(plansza):
    tab = []
    for kol in range(3):
        for wiersz in range(3):
            if plansza[wiersz][kol] == 0:
                index = [wiersz, kol]
                tab.append(index)
    return tab


def pola_zajete(plansza):
    tab = []
    for kol in range(3):
        for wiersz in range(3):
            if plansza[wiersz][kol] == 1:
                index = [wiersz, kol]
                tab.append(index)
    return tab


def minimax_ustawianie(poziom, max, plansza):
    puste = puste_pola(plansza)
    if poziom == 0 or len(puste) == 0:
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
    zajete = pola_zajete(plansza)
    puste = puste_pola(plansza)
    if poziom == 0:
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
