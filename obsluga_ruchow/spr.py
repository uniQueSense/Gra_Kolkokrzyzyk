KOMPUTER = 1
GRACZ = -1

def sprawdz_pola(plansza):
    for kolumna in range(3):
        if plansza[0][kolumna] == plansza[1][kolumna] and plansza[1][kolumna] == plansza[2][kolumna]:
            if plansza[0][kolumna] == 1:
                return KOMPUTER
            elif plansza[0][kolumna] == -1:
                return GRACZ
    for wiersz in range(3):
        if plansza[wiersz][0] == plansza[wiersz][1] and plansza[wiersz][1] == plansza[wiersz][2]:
            if plansza[wiersz][0] == 1:
                return KOMPUTER
            elif plansza[wiersz][0] == -1:
                return GRACZ
    if plansza[0][0] == plansza[1][1] and plansza[1][1] == plansza[2][2]:
        if plansza[0][0] == 1:
            return KOMPUTER
        elif plansza[0][0] == -1:
            return GRACZ
    if plansza[0][2] == plansza[1][1] and plansza[1][1] == plansza[2][0]:
        if plansza[1][1] == 1:
            return KOMPUTER
        elif plansza[1][1] == -1:
            return GRACZ
    return 0

def sasiadujace(osx0, osy0, osx1, osy1):   # sprawdza czy pionek sasiaduje z wybranym polem
    if osx0 == 0:
        if osy0 == 0:
            if osx1 != 2 and osy1 !=2:
                return True
        if osy0 == 1:
            if osx1 != 2:
                return True
        if osy0 == 2:
            if osx1 != 2 and osy1 != 0:
                return True
    elif osx0 == 1:
        if osy0 == 0:
            if osy1 != 2:
                return True
        if osy0 == 1:
            return True
        if osy0 == 2:
            if osy1 != 0:
                return True
    elif osx0 == 2:
        if osy0 == 0:
            if osx1 != 0 and osy1 != 2:
                return True
        if osy0 == 1:
            if osx1 != 0:
                return True
        if osy0 == 2:
            if osx1 != 0 and osy1 != 0:
                return True
    return False


