from obsluga_ruchow.spr import sprawdz_pola
INF = 10

def ocena_pola(plansza):
    if sprawdz_pola(plansza) == 1:
        return 10
    elif sprawdz_pola(plansza) == -1:
        return -20
    else:
        return 0


def puste_pola(plansza):
    tab = []
    for kol in range(3):
        for wiersz in range(3):
            if plansza[wiersz][kol] == 0:
                indx = [wiersz, kol]
                tab.append(indx)
    return tab

def minimax_ustawianie(poziom, max, plansza):
    puste = puste_pola(plansza)
    if poziom == 0 or len(puste) == 0:
        return None, ocena_pola(plansza)
    if max:
        index = puste[0]
        wartosc = -50000000
        for wiersz, kol in puste:
            tab = [[kol for kol in wiersz] for wiersz in plansza]
            tab[wiersz][kol] = 1
            k, stan = minimax_ustawianie(poziom - 1, False, tab)
            if stan > wartosc:
                wartosc = stan
                index = [wiersz, kol]
        return index, wartosc
    else:
        index = puste[0]
        wartosc = 50000000
        for wiersz, kol in puste:
            tab = [[kol for kol in wiersz] for wiersz in plansza]
            tab[wiersz][kol] = -1
            k, stan = minimax_ustawianie(poziom - 1, True, tab)
            if stan < wartosc:
                wartosc = stan
                index = [wiersz, kol]
        return index, wartosc


