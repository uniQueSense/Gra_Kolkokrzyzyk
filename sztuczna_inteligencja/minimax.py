from dane import stale
from obsluga_ruchow import sprawdzanie_ruchow


def ocena_pola(plansza):
    """ Ocena planszy w funkcji minimax"""
    if sprawdzanie_ruchow.sprawdz_pola(plansza) == stale.KOMPUTER:
        return 10
    elif sprawdzanie_ruchow.sprawdz_pola(plansza) == stale.GRACZ:
        return -10
    else:
        return 0


def puste_pola(plansza):
    """ Zapisuje indexy pustych pól w grze """
    index = []
    for kol in range(stale.ILOSC_KOLUMN):
        for wiersz in range(stale.ILOSC_WIERSZY):
            if plansza[wiersz][kol] == stale.PUSTO:
                index.append((wiersz, kol))
    return index


def pola_zajete(plansza):
    """ Zapisuje indexy zajętych pól w grze """
    index = []
    for kol in range(stale.ILOSC_KOLUMN):
        for wiersz in range(stale.ILOSC_WIERSZY):
            if plansza[wiersz][kol] != stale.PUSTO:
                index.append((wiersz, kol))
    return index


def minimax_ustawianie(poziom, max, plansza):
    """ Funkcja minimax do etapu rozstawiania pionków """
    puste = puste_pola(plansza)
    if not poziom:
        return None, ocena_pola(plansza)
    if max:
        index = puste[0]
        wartosc = -stale.INF
        for wiersz, kol in puste:
            tab = [[kol for kol in wiersz] for wiersz in plansza]
            tab[wiersz][kol] = stale.KOMPUTER
            _, stan = minimax_ustawianie(poziom - 1, False, tab)
            if stan >= wartosc:
                wartosc = stan
                index = [wiersz, kol]
        return index, wartosc
    else:
        index = puste[0]
        wartosc = stale.INF
        for wiersz, kol in puste:
            tab = [[kol for kol in wiersz] for wiersz in plansza]
            tab[wiersz][kol] = stale.GRACZ
            _, stan = minimax_ustawianie(poziom - 1, True, tab)
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
        wartosc = -stale.INF
        for wiersz, kol in zajete:
            tab = [[kol for kol in wiersz] for wiersz in plansza]
            for wiersz_wstaw, kol_wstaw in puste:
                if sprawdzanie_ruchow.sasiadujace(kol, wiersz, kol_wstaw, wiersz_wstaw) and tab[wiersz][kol] == stale.KOMPUTER:
                    tab[wiersz][kol] = stale.PUSTO
                    tab[wiersz_wstaw][kol_wstaw] = stale.KOMPUTER
                    _, _, stan = minimax_przemieszczanie(poziom - 1, False, tab)
                    if stan > wartosc:
                        wartosc = stan
                        index0 = [wiersz, kol]
                        index1 = [wiersz_wstaw, kol_wstaw]
        return index0, index1, wartosc
    else:
        index0 = zajete[0]
        index1 = puste[0]
        wartosc = stale.INF
        for wiersz, kol in zajete:
            tab = [[kol for kol in wiersz] for wiersz in plansza]
            for wiersz_wstaw, kol_wstaw in puste:
                if sprawdzanie_ruchow.sasiadujace(kol, wiersz, kol_wstaw, wiersz_wstaw) and tab[wiersz][kol] == stale.GRACZ:
                    tab[wiersz][kol] = stale.PUSTO
                    tab[wiersz_wstaw][kol_wstaw] = stale.GRACZ
                    _, _, stan = minimax_przemieszczanie(poziom - 1, True, tab)
                    if stan < wartosc:
                        wartosc = stan
                        index0 = [wiersz, kol]
                        index1 = [wiersz_wstaw, kol_wstaw]
        return index0, index1, wartosc
