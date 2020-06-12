from stale.stale import *

def postaw_znak(osy, osx, kogo_ruch, ilosc, plansza):
    blad = 4
    if plansza[osy][osx] == PUSTO:
        ilosc = ilosc + 1
        if kogo_ruch == GRACZ:
            plansza[osy][osx] = GRACZ
            return KOMPUTER, ilosc, blad
        elif kogo_ruch == KOMPUTER:
            plansza[osy][osx] = KOMPUTER
            return GRACZ, ilosc, blad
    else:
        blad = 2
        return kogo_ruch, ilosc, blad

def porusz_znak(osy0, osx0, osy1, osx1, kogo_ruch, plansza):
    blad = 4
    if kogo_ruch == GRACZ:
        if plansza[osy0][osx0] == GRACZ:
            if plansza[osy1][osx1] == PUSTO:
                plansza[osy0][osx0] = PUSTO
                plansza[osy1][osx1] = GRACZ
                return KOMPUTER, blad
            elif plansza[osy1][osx1] == KOMPUTER or plansza[osy1][osx1] == GRACZ:
                blad = 2
                return GRACZ, blad
        elif plansza[osx0][osy0] == KOMPUTER:
            blad = 1
            return kogo_ruch, blad
        elif plansza[osx0][osy0] == PUSTO:
            blad = 0
            return kogo_ruch, blad
    elif kogo_ruch == KOMPUTER:
        if plansza[osy0][osx0] == KOMPUTER:
            if plansza[osy1][osx1] == PUSTO:
                plansza[osy0][osx0] = PUSTO
                plansza[osy1][osx1] = KOMPUTER
                return GRACZ, blad
            else:
                return KOMPUTER, blad
        else:
            return kogo_ruch, blad