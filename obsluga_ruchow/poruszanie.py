from funkcje_rysujace.napisy_przyciski import blad_puste_pole
from funkcje_rysujace.napisy_przyciski import blad_zly_pionek
from funkcje_rysujace.napisy_przyciski import blad_zajete_pole
from funkcje_rysujace.napisy_przyciski import brak_bledu

from dane.stale import GRACZ
from dane.stale import KOMPUTER
from dane.stale import PUSTO


def postaw_znak(osy, osx, kogo_ruch, ilosc, plansza):
    """ Funkcja nadpisuje wartościami GRACZ lub KOMPUTER tablicę gry """
    if plansza[osy][osx] == PUSTO:
        ilosc = ilosc + 1
        if kogo_ruch == GRACZ:
            plansza[osy][osx] = GRACZ
            return KOMPUTER, ilosc, brak_bledu
        elif kogo_ruch == KOMPUTER:
            plansza[osy][osx] = KOMPUTER
            return GRACZ, ilosc, brak_bledu
    else:
        return kogo_ruch, ilosc, blad_zajete_pole


def porusz_znak(osy0, osx0, osy1, osx1, kogo_ruch, plansza):
    """ Funkcja obsługuje zmianę miejsca pionka na planszy """
    print('osy0: {}, osx0: {}, osy1: {}, osx1: {}, kogo_ruch: {}'.format(osy0, osx0, osy1, osx1, kogo_ruch))
    if kogo_ruch == GRACZ:
        if plansza[osy0][osx0] == GRACZ:
            if plansza[osy1][osx1] == PUSTO:
                plansza[osy0][osx0] = PUSTO
                plansza[osy1][osx1] = GRACZ
                return KOMPUTER, brak_bledu
            else:
                return GRACZ, blad_zajete_pole
        elif plansza[osx0][osy0] == KOMPUTER:
            return kogo_ruch, blad_zly_pionek
        elif plansza[osx0][osy0] == PUSTO:
            return kogo_ruch, blad_puste_pole
    elif kogo_ruch == KOMPUTER:
        if plansza[osy0][osx0] == KOMPUTER:
            if plansza[osy1][osx1] == PUSTO:
                plansza[osy0][osx0] = PUSTO
                plansza[osy1][osx1] = KOMPUTER
                return GRACZ, brak_bledu
            else:
                return KOMPUTER, brak_bledu
        else:
            return kogo_ruch, brak_bledu
