def postaw_znak(osy, osx, kogo_ruch, ilosc, plansza):
    if plansza[osy][osx] == 0:
        ilosc = ilosc + 1
        if kogo_ruch == -1:
            plansza[osy][osx] = -1
            return 1, ilosc
        elif kogo_ruch == 1:
            plansza[osy][osx] = 1
            return -1, ilosc
    elif plansza[osy][osx] == -1 or plansza[osy][osx] == 1:
        print("Zajęte pole", osy, osx)
        return kogo_ruch, ilosc

def porusz_znak(osy0, osx0, osy1, osx1, kogo_ruch, plansza):
    if kogo_ruch == -1:
        if plansza[osy0][osx0] == -1:
            if plansza[osy1][osx1] == 0:
                plansza[osy0][osx0] = 0
                plansza[osy1][osx1] = -1
                return 1
            else:
                print('tu stoi pionek')
                return kogo_ruch
        else:
            if plansza[osx0][osy0] == 1:
                print("wybrales pionek gracza 2")
            else:
                print("na tym polu nie ma pionków1")
            return kogo_ruch
    elif kogo_ruch == 1:
        if plansza[osy0][osx0] == 1:
            if plansza[osy1][osx1] == 0:
                plansza[osy0][osx0] = 0
                plansza[osy1][osx1] = 1
                return -1
            else:
                print('tu stoi pionek')
                return kogo_ruch
        else:
            if plansza[osx0][osy0] == 1:
                print("wybrales pionek gracza 1")
            else:
                print("na tym polu nie ma pionków2")
            return kogo_ruch