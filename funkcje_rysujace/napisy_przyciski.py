from dane import kolory
from dane import stale
from funkcje_rysujace import klasy
from funkcje_rysujace import pionki
from funkcje_rysujace import obszar_gry

# Przyciski w GUI
p_reset = klasy.Przycisk(kolory.KOLOR_PRZYCISK_NAWIGACJI, kolory.KOLOR_TEKSTU_PRZYCISKI, stale.OSX_PRZYCISKOW1,
                         stale.OSY_PRZYCISKOW1, stale.DL_PRZYCISKU1, stale.WYS_PRZYCISKU1, 'Reset')
p_wyjscie = klasy.Przycisk(kolory.KOLOR_PRZYCISK_NAWIGACJI, kolory.KOLOR_TEKSTU_PRZYCISKI, stale.OSX_PRZYCISKOW2,
                           stale.OSY_PRZYCISKOW1, stale.DL_PRZYCISKU1, stale.WYS_PRZYCISKU1, 'Wyjdź')
p_menu = klasy.Przycisk(kolory.KOLOR_PRZYCISK_NAWIGACJI, kolory.KOLOR_TEKSTU_PRZYCISKI, stale.OSX_PRZYCISKOW1,
                        stale.OSY_PRZYCISKOW2, stale.DL_PRZYCISKU3, stale.WYS_PRZYCISKU1, 'Menu')
p_wstecz = klasy.Przycisk(kolory.KOLOR_P_WSTECZ, kolory.KOLOR_TEKSTU_PRZYCISKI, stale.OSX_PRZYCISKOW1,
                          stale.OSY_PRZYCISKOW2, stale.DL_PRZYCISKU3, stale.WYS_PRZYCISKU1, 'Wstecz')
p_gracz = klasy.Przycisk(kolory.KOLOR_TEKSTU, kolory.KOLOR_TEKST_P_MENU, stale.OSX_PRZYCISKOW3, stale.OSY_PRZYCISKOW3,
                         stale.DL_PRZYCISKU2, stale.WYS_PRZYCISKU1,
                         'Gracz')
p_komputer = klasy.Przycisk(kolory.KOLOR_TEKSTU, kolory.KOLOR_TEKST_P_MENU, stale.OSX_PRZYCISKOW4,
                            stale.OSY_PRZYCISKOW3,
                            stale.DL_PRZYCISKU2, stale.WYS_PRZYCISKU1,
                            'Komputer')

# Bloki w GUI
pole_informacyjne = klasy.Blok(kolory.KOLOR_POLE_INF, stale.OSX_POLE_INF, stale.OSY_POLE_INF, stale.DL_POLE_INF,
                               stale.WYS_POLE_INF)
pole_menu = klasy.Blok(kolory.KOLOR_MENU, stale.OSX_PLANSZA, stale.OSY_PLANSZA, stale.ROZMIAR_PLANSZY,
                       stale.ROZMIAR_PLANSZY)

# Tekst wyświetlany w GUI
t_naglowek = klasy.Tekst(stale.OSX_NAGLOWEK, stale.OSY_NAGLOWEK, kolory.KOLOR_WYNIK, stale.ROZMIAR_TEKSTU1,
                         stale.CZCIONKA,
                         'WYNIK:')
t_grasz = klasy.Tekst(stale.OSX_NAPIS_GRACZ, stale.OSY_NAPIS_GRACZ, kolory.KOLOR_GRACZA, stale.ROZMIAR_TEKSTU1,
                      stale.CZCIONKA, 'GRACZ')
t_ai = klasy.Tekst(stale.OSX_NAPIS_AI, stale.OSY_NAPIS_AI, kolory.KOLOR_AI, stale.ROZMIAR_TEKSTU1, stale.CZCIONKA, 'AI')
t_kto_zaczyna = klasy.Tekst(stale.OSX_NAPIS_KTO, stale.OSY_NAPIS_KTO, kolory.KOLOR_TEKSTU, stale.ROZMIAR_TEKSTU2,
                            stale.CZCIONKA, 'Kto ma zacząć rozgrywkę:')

# Błędy wyświetlane podczas nieprawidłowego ruchu przez gracza
t_blad_naglowek = klasy.Tekst(stale.OSX_BLAD, stale.OSY_BLAD_NAGLOWEK, kolory.KOLOR_TEKSTU, stale.BLAD_ROZM,
                              stale.CZCIONKA,
                              'Błąd:')
blad_puste_pole = klasy.Tekst(stale.OSX_BLAD, stale.OSY_BLAD, kolory.KOLOR_BLEDU, stale.BLAD_ROZM, stale.CZCIONKA,
                              'Wybrałeś pole na którym nie ma pionka.')
blad_zly_pionek = klasy.Tekst(stale.OSX_BLAD, stale.OSY_BLAD, kolory.KOLOR_BLEDU, stale.BLAD_ROZM, stale.CZCIONKA,
                              'Wybrałeś pionek przeciwnika.')
blad_zajete_pole = klasy.Tekst(stale.OSX_BLAD, stale.OSY_BLAD, kolory.KOLOR_BLEDU, stale.BLAD_ROZM, stale.CZCIONKA,
                               'To pole jest zajęte.')
blad_zle_pole = klasy.Tekst(stale.OSX_BLAD, stale.OSY_BLAD, kolory.KOLOR_BLEDU, stale.BLAD_ROZM, stale.CZCIONKA,
                            'To pole nie sąsiaduje z wybranym pionkiem.')
brak_bledu = klasy.Tekst(stale.OSX_BLAD, stale.OSY_BLAD, kolory.KOLOR_BLEDU, stale.BLAD_ROZM, stale.CZCIONKA,
                         'Brak błędu.')


def przekaz_ture(kogo_ruch, wygrana):
    if not wygrana:
        if kogo_ruch == stale.GRACZ:
            kto = " Gracz"
        elif kogo_ruch == stale.KOMPUTER:
            kto = " Komputer"
    else:
        kto = " Koniec gry"
    return klasy.Tekst(stale.OSX_INFO_RUCH, stale.OSY_INFO_RUCH, kolory.KOLOR_KOGO_RUCH, stale.ROZ_CZCIONKI_RUCH,
                       stale.CZCIONKA, 'Ruch: {}'.format(kto))


def przekaz_wynik(zwycięzca, okno):
    if zwycięzca == stale.GRACZ:
        tekst = klasy.Tekst(stale.OSX_PRZEKAZ_WYNIK, stale.OSY_PRZEKAZ_WYNIK, kolory.KOLOR_TEKSTU,
                            stale.ROZ_CZCIONKI_WYNIK,
                            stale.CZCIONKA, 'Wygrał gracz!')
    elif zwycięzca == stale.KOMPUTER:
        tekst = klasy.Tekst(stale.OSX_PRZEKAZ_WYNIK, stale.OSY_PRZEKAZ_WYNIK, kolory.KOLOR_TEKSTU,
                            stale.ROZ_CZCIONKI_WYNIK,
                            stale.CZCIONKA, 'Wygrał komputer!')
    tekst.napisz(okno)


def nadpisz(stan, punkt_ai, punkt_gracz, blad, kogo_ruch, wygrana, plansza, okno):
    okno.fill(kolory.KOLOR_TLO)
    przekaz_ture(kogo_ruch, wygrana).napisz(okno)
    p_reset.rysuj(okno)
    p_wyjscie.rysuj(okno)
    pole_informacyjne.rysuj(okno)

    t_stan = klasy.Tekst(stale.OSX_PKT, stale.OSY_PKT, kolory.KOLOR_WYNIK, stale.ROZMIAR_TEKSTU1, stale.CZCIONKA,
                         '{} : {}'.format(punkt_gracz, punkt_ai))
    t_stan.napisz(okno)

    t_naglowek.napisz(okno)
    t_grasz.napisz(okno)
    t_ai.napisz(okno)
    t_blad_naglowek.napisz(okno)
    blad.napisz(okno)
    if not stan:
        obszar_gry.rysuj_pole_gry(okno)
        pionki.rysuj_pionek(okno, kolory.KOLOR_GRACZA, kolory.KOLOR_AI, plansza)
        p_menu.rysuj(okno)
    else:
        pole_menu.rysuj(okno)
        t_kto_zaczyna.napisz(okno)
        p_wstecz.rysuj(okno)
        p_gracz.rysuj(okno)
        p_komputer.rysuj(okno)
