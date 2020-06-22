from funkcje_rysujace.napisy_przyciski import blad1
from funkcje_rysujace.napisy_przyciski import blad2
from funkcje_rysujace.napisy_przyciski import blad3
from funkcje_rysujace.napisy_przyciski import blad5

from stale.stale import GRACZ
from stale.stale import KOMPUTER
from stale.stale import PUSTO


def postaw_znak(osy, osx, kogo_ruch, ilosc, plansza):
    """ Funkcja nadpisuje wartościami GRACZ lub KOMPUTER tablicę gry """
    if plansza[osy][osx] == PUSTO:
        ilosc = ilosc + 1
        if kogo_ruch == GRACZ:
            plansza[osy][osx] = GRACZ
            return KOMPUTER, ilosc, blad5
        elif kogo_ruch == KOMPUTER:
            plansza[osy][osx] = KOMPUTER
            return GRACZ, ilosc, blad5
    else:
        return kogo_ruch, ilosc, blad3


def porusz_znak(osy0, osx0, osy1, osx1, kogo_ruch, plansza):
    """ Funkcja obsługuje zmianę miejsca pionka na planszy """
    if kogo_ruch == GRACZ:
        if plansza[osy0][osx0] == GRACZ:
            if plansza[osy1][osx1] == PUSTO:
                plansza[osy0][osx0] = PUSTO
                plansza[osy1][osx1] = GRACZ
                return KOMPUTER, blad5
            else:
                return GRACZ, blad3
        elif plansza[osx0][osy0] == KOMPUTER:
            return kogo_ruch, blad2
        elif plansza[osx0][osy0] == PUSTO:
            return kogo_ruch, blad1
    elif kogo_ruch == KOMPUTER:
        if plansza[osy0][osx0] == KOMPUTER:
            if plansza[osy1][osx1] == PUSTO:
                plansza[osy0][osx0] = PUSTO
                plansza[osy1][osx1] = KOMPUTER
                return GRACZ, blad5
            else:
                return KOMPUTER, blad5
        else:
            return kogo_ruch, blad5
