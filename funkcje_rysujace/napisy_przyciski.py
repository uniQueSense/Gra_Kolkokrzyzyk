from funkcje_rysujace.assets import Assets
from funkcje_rysujace.klasy import Blok
from funkcje_rysujace.klasy import Przycisk
from funkcje_rysujace.pionki import rysuj_pionek
from funkcje_rysujace.plansza import rysuj_pole_gry
from funkcje_rysujace.klasy import Tekst
from dane.stale import BLAD_ROZM
from dane.stale import CZCIONKA
from dane.stale import DL_PRZYCISKU1
from dane.stale import DL_PRZYCISKU2
from dane.stale import DL_PRZYCISKU3
from dane.stale import DL_POLE_INF
from dane.stale import GRACZ
from dane.stale import KOLOR_AI
from dane.stale import KOLOR_BLEDU
from dane.stale import KOLOR_GRACZA
from dane.stale import KOLOR_KOGO_RUCH
from dane.stale import KOLOR_MENU
from dane.stale import KOLOR_POLE_INF
from dane.stale import KOLOR_PRZYCISK_NAWIGACJI
from dane.stale import KOLOR_P_WSTECZ
from dane.stale import KOLOR_TEKSTU
from dane.stale import KOLOR_TEKST_P_MENU
from dane.stale import KOLOR_TEKSTU_PRZYCISKI
from dane.stale import KOLOR_TLO
from dane.stale import KOLOR_WYNIK
from dane.stale import KOMPUTER
from dane.stale import OSX_BLAD
from dane.stale import OSY_BLAD
from dane.stale import OSY_BLAD_NAGLOWEK
from dane.stale import OSX_INFO_RUCH
from dane.stale import OSY_INFO_RUCH
from dane.stale import OSX_NAGLOWEK
from dane.stale import OSY_NAGLOWEK
from dane.stale import OSX_NAPIS_AI
from dane.stale import OSY_NAPIS_AI
from dane.stale import OSX_NAPIS_GRACZ
from dane.stale import OSY_NAPIS_GRACZ
from dane.stale import OSY_NAPIS_KTO
from dane.stale import OSX_NAPIS_KTO
from dane.stale import OSX_PKT
from dane.stale import OSY_PKT
from dane.stale import OSX_PLANSZA
from dane.stale import OSY_PLANSZA
from dane.stale import OSX_POLE_INF
from dane.stale import OSY_POLE_INF
from dane.stale import OSX_PRZEKAZ_WYNIK
from dane.stale import OSY_PRZEKAZ_WYNIK
from dane.stale import OSX_PRZYCISKOW1
from dane.stale import OSY_PRZYCISKOW1
from dane.stale import OSX_PRZYCISKOW2
from dane.stale import OSY_PRZYCISKOW2
from dane.stale import OSX_PRZYCISKOW3
from dane.stale import OSY_PRZYCISKOW3
from dane.stale import OSX_PRZYCISKOW4
from dane.stale import ROZ_CZCIONKI_RUCH
from dane.stale import ROZ_CZCIONKI_WYNIK
from dane.stale import ROZMIAR_TEKSTU1
from dane.stale import ROZMIAR_TEKSTU2
from dane.stale import ROZMIAR_PLANSZY
from dane.stale import WYS_PRZYCISKU1
from dane.stale import WYS_POLE_INF

''' Przyciski w GUI '''
p_reset = Przycisk(KOLOR_PRZYCISK_NAWIGACJI, KOLOR_TEKSTU_PRZYCISKI, OSX_PRZYCISKOW1, OSY_PRZYCISKOW1, DL_PRZYCISKU1,
                   WYS_PRZYCISKU1, 'Reset')
p_wyjscie = Przycisk(KOLOR_PRZYCISK_NAWIGACJI, KOLOR_TEKSTU_PRZYCISKI, OSX_PRZYCISKOW2, OSY_PRZYCISKOW1, DL_PRZYCISKU1,
                     WYS_PRZYCISKU1, 'Wyjdź')
p_menu = Przycisk(KOLOR_PRZYCISK_NAWIGACJI, KOLOR_TEKSTU_PRZYCISKI, OSX_PRZYCISKOW1, OSY_PRZYCISKOW2, DL_PRZYCISKU3,
                  WYS_PRZYCISKU1, 'Menu')
p_wstecz = Przycisk(KOLOR_P_WSTECZ, KOLOR_TEKSTU_PRZYCISKI, OSX_PRZYCISKOW1, OSY_PRZYCISKOW2, DL_PRZYCISKU3,
                    WYS_PRZYCISKU1,
                    'Wstecz')

p_gracz = Przycisk(KOLOR_TEKSTU, KOLOR_TEKST_P_MENU, OSX_PRZYCISKOW3, OSY_PRZYCISKOW3, DL_PRZYCISKU2, WYS_PRZYCISKU1,
                   'Gracz')
p_komputer = Przycisk(KOLOR_TEKSTU, KOLOR_TEKST_P_MENU, OSX_PRZYCISKOW4, OSY_PRZYCISKOW3, DL_PRZYCISKU2, WYS_PRZYCISKU1,
                      'Komputer')

''' Bloki w GUI '''
pole_informacyjne = Blok(KOLOR_POLE_INF, OSX_POLE_INF, OSY_POLE_INF, DL_POLE_INF, WYS_POLE_INF)
pole_menu = Blok(KOLOR_MENU, OSX_PLANSZA, OSY_PLANSZA, ROZMIAR_PLANSZY, ROZMIAR_PLANSZY)

''' Tekst wyświetlany w GUI '''
t_naglowek = Tekst(OSX_NAGLOWEK, OSY_NAGLOWEK, KOLOR_WYNIK, ROZMIAR_TEKSTU1, CZCIONKA, 'WYNIK:')
t_grasz = Tekst(OSX_NAPIS_GRACZ, OSY_NAPIS_GRACZ, KOLOR_GRACZA, ROZMIAR_TEKSTU1, CZCIONKA, 'GRACZ')
t_ai = Tekst(OSX_NAPIS_AI, OSY_NAPIS_AI, KOLOR_AI, ROZMIAR_TEKSTU1, CZCIONKA, 'AI')
t_kto_zaczyna = Tekst(OSX_NAPIS_KTO, OSY_NAPIS_KTO, KOLOR_TEKSTU, ROZMIAR_TEKSTU2, CZCIONKA, 'Kto ma zacząć rozgrywkę:')

""" Błędy wyświetlane podczas nieprawidłowego ruchu przez gracza """
t_blad_naglowek = Tekst(OSX_BLAD, OSY_BLAD_NAGLOWEK, KOLOR_TEKSTU, BLAD_ROZM, CZCIONKA, 'Błąd:')
blad_puste_pole = Tekst(OSX_BLAD, OSY_BLAD, KOLOR_BLEDU, BLAD_ROZM, CZCIONKA,
              'Wybrałeś pole na którym nie ma pionka.')
blad_zly_pionek = Tekst(OSX_BLAD, OSY_BLAD, KOLOR_BLEDU, BLAD_ROZM, CZCIONKA, 'Wybrałeś pionek przeciwnika.')
blad_zajete_pole = Tekst(OSX_BLAD, OSY_BLAD, KOLOR_BLEDU, BLAD_ROZM, CZCIONKA, 'To pole jest zajęte.')
blad_zle_pole = Tekst(OSX_BLAD, OSY_BLAD, KOLOR_BLEDU, BLAD_ROZM, CZCIONKA,
              'To pole nie sąsiaduje z wybranym pionkiem.')
brak_bledu = Tekst(OSX_BLAD, OSY_BLAD, KOLOR_BLEDU, BLAD_ROZM, CZCIONKA, 'Brak błędu.')


def przekaz_ture(kogo_ruch, wygrana):
    if not wygrana:
        if kogo_ruch == GRACZ:
            kto = " Gracz"
        elif kogo_ruch == KOMPUTER:
            kto = " Komputer"
    else:
        kto = " Koniec gry"
    return Tekst(OSX_INFO_RUCH, OSY_INFO_RUCH, KOLOR_KOGO_RUCH, ROZ_CZCIONKI_RUCH, CZCIONKA, 'Ruch: {}'.format(kto))


def przekaz_wynik(zwycięzca, okno):
    if zwycięzca == GRACZ:
        tekst = Tekst(OSX_PRZEKAZ_WYNIK, OSY_PRZEKAZ_WYNIK, KOLOR_TEKSTU, ROZ_CZCIONKI_WYNIK, CZCIONKA, 'Wygrał gracz!')
    elif zwycięzca == KOMPUTER:
        tekst = Tekst(OSX_PRZEKAZ_WYNIK, OSY_PRZEKAZ_WYNIK, KOLOR_TEKSTU, ROZ_CZCIONKI_WYNIK, CZCIONKA,
                      'Wygrał komputer!')
    tekst.napisz(okno)


def nadpisz(stan, punkt_ai, punkt_gracz, blad, kogo_ruch, wygrana, plansza, okno):
    okno.fill(KOLOR_TLO)
    przekaz_ture(kogo_ruch, wygrana).napisz(okno)
    p_reset.rysuj(okno)
    p_wyjscie.rysuj(okno)
    pole_informacyjne.rysuj(okno)

    t_stan = Tekst(OSX_PKT, OSY_PKT, KOLOR_WYNIK, ROZMIAR_TEKSTU1, CZCIONKA, '{} : {}'.format(punkt_gracz, punkt_ai))
    t_stan.napisz(okno)

    t_naglowek.napisz(okno)
    t_grasz.napisz(okno)
    t_ai.napisz(okno)
    t_blad_naglowek.napisz(okno)
    blad.napisz(okno)
    if not stan:
        rysuj_pole_gry(okno)
        rysuj_pionek(okno, KOLOR_GRACZA, KOLOR_AI, plansza)
        p_menu.rysuj(okno)
    else:
        pole_menu.rysuj(okno)
        t_kto_zaczyna.napisz(okno)
        p_wstecz.rysuj(okno)
        p_gracz.rysuj(okno)
        p_komputer.rysuj(okno)
        Assets.load(okno)
