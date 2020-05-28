from obsluga_ruchow.poruszanie import porusz_znak

def sasiadujace(pole1, pole2, kogo_ruch,  plansza):   # sprawdza czy pionek sasiaduje z wybranym polem
    if pole1 == 0:    # 3 opcje
        for n in [1, 3, 4]:
            if pole2 == n:
                kogo_ruch = porusz_znak(pole1, pole2, kogo_ruch, plansza)
    elif pole1 == 2:
        for n in [1, 4, 5]:
            if pole2 == n:
                kogo_ruch = porusz_znak(pole1, pole2, kogo_ruch, plansza)
    elif pole1 == 6:
        for n in [3, 4, 7]:
            if pole2 == n:
                kogo_ruch = porusz_znak(pole1, pole2, kogo_ruch, plansza)
    elif pole1 == 8:
        for n in [4, 5, 7]:
            if pole2 == n:
                kogo_ruch = porusz_znak(pole1, pole2, kogo_ruch, plansza)
    elif pole1 == 1:   # 5 opcji
        for n in [0, 2, 3, 4, 5]:
            if pole2 == n:
                kogo_ruch = porusz_znak(pole1, pole2, kogo_ruch, plansza)
    elif pole1 == 3:
        for n in [0, 1, 4, 6, 7]:
            if pole2 == n:
                kogo_ruch = porusz_znak(pole1, pole2, kogo_ruch, plansza)
    elif pole1 == 5:
        for n in [1, 2, 4, 7, 8]:
            if pole2 == n:
                kogo_ruch = porusz_znak(pole1, pole2, kogo_ruch, plansza)
    elif pole1 == 7:
        for n in [3, 4, 5, 6, 8]:
            if pole2 == n:
                kogo_ruch = porusz_znak(pole1, pole2, kogo_ruch, plansza)
    elif pole1 == 4:   # sasiaduje ze wszystkimi
        kogo_ruch = porusz_znak(pole1, pole2, kogo_ruch, plansza)
    return kogo_ruch

