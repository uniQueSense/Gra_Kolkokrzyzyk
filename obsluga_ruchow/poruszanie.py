def postaw_znak(pole, kogo_ruch, ilosc, plansza):
    if plansza[pole] == 0:
        ilosc = ilosc + 1
        if kogo_ruch == 1:  # ruch gracza
            plansza[pole] = 1
            return 2, ilosc
        elif kogo_ruch == 2:  # ruch komputera
            plansza[pole] = 2
            return 1, ilosc
    if plansza[pole] == 1 or plansza[pole] == 2:
        print("powtórz")
        return kogo_ruch, ilosc


def porusz_znak(pole1, pole2, kogo_ruch, plansza):
    if kogo_ruch == 1:
        if plansza[pole1] == 1:
            if plansza[pole2] == 0:
                plansza[pole1] = 0
                plansza[pole2] = 1
                return 2
            else:
                print('tu stoi pionek')
                return kogo_ruch
        else:
            if plansza[pole1] == 2:
                print("wybrales pionek gracza 2")
            else:
                print("na tym polu nie ma pionków1")
            return kogo_ruch
    elif kogo_ruch == 2:
        if plansza[pole1] == 2:
            if plansza[pole2] == 0:
                plansza[pole1] = 0
                plansza[pole2] = 2
                return 1
            else:
                print('tu stoi pionek')
                return kogo_ruch
        else:
            if plansza[pole1] == 2:
                print("wybrales pionek gracza 1")
            else:
                print("na tym polu nie ma pionków2")
            return kogo_ruch