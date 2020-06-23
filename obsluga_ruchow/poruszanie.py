from funkcje_rysujace.napisy_przyciski import blad_puste_pole
from funkcje_rysujace.napisy_przyciski import blad_zly_pionek
from funkcje_rysujace.napisy_przyciski import blad_zajete_pole
from funkcje_rysujace.napisy_przyciski import brak_bledu

from dane import stale



def postaw_znak(osy, osx, kogo_ruch, ilosc, plansza):
    """ Funkcja nadpisuje wartościami GRACZ lub KOMPUTER tablicę gry """
    if plansza[osy][osx] == stale.PUSTO:
        ilosc = ilosc + 1
        if kogo_ruch == stale.GRACZ:
            plansza[osy][osx] = stale.GRACZ
            return stale.KOMPUTER, ilosc, brak_bledu
        elif kogo_ruch == stale.KOMPUTER:
            plansza[osy][osx] = stale.KOMPUTER
            return stale.GRACZ, ilosc, brak_bledu
    else:
        return kogo_ruch, ilosc, blad_zajete_pole


def porusz_znak(osy0, osx0, osy1, osx1, kogo_ruch, plansza):
    """ Funkcja obsługuje zmianę miejsca pionka na planszy """
    print('osy0: {}, osx0: {}, osy1: {}, osx1: {}, kogo_ruch: {}'.format(osy0, osx0, osy1, osx1, kogo_ruch))
    if kogo_ruch == stale.GRACZ:
        if plansza[osy0][osx0] == stale.GRACZ:
            if plansza[osy1][osx1] == stale.PUSTO:
                plansza[osy0][osx0] = stale.PUSTO
                plansza[osy1][osx1] = stale.GRACZ
                return stale.KOMPUTER, brak_bledu
            else:
                return stale.GRACZ, blad_zajete_pole
        elif plansza[osx0][osy0] == stale.KOMPUTER:
            return kogo_ruch, blad_zly_pionek
        elif plansza[osx0][osy0] == stale.PUSTO:
            return kogo_ruch, blad_puste_pole
    elif kogo_ruch == stale.KOMPUTER:
        if plansza[osy0][osx0] == stale.KOMPUTER:
            if plansza[osy1][osx1] == stale.PUSTO:
                plansza[osy0][osx0] = stale.PUSTO
                plansza[osy1][osx1] = stale.KOMPUTER
                return stale.GRACZ, brak_bledu
            else:
                return stale.KOMPUTER, brak_bledu
        else:
            return kogo_ruch, brak_bledu
