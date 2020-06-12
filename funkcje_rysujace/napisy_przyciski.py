from funkcje_rysujace.klasy import *
from funkcje_rysujace.plansza import *
from funkcje_rysujace.pionki import *
from stale.stale import *

p_reset = Przycisk(RED, WHITE, 915, 840, 170, 45, 'Reset')
p_wyjscie = Przycisk(RED, WHITE, 1115, 840, 170, 45, 'Wyjdź')
p_menu = Przycisk(RED, WHITE, 915, 780, 370, 45, 'Menu')
p_wstecz = Przycisk(BROWN, WHITE, 915, 780, 370, 45, 'Wstecz')

p_gracz = Przycisk(BLACK, GREEN, 160, 120, 250, 45, 'Gracz')
p_komputer = Przycisk(BLACK, GREEN, 490, 120, 250, 45, 'Komputer')

pole_informacyjne = Blok(BURLYWOOD, 915, 450, 370, 100)
pole_menu = Blok(PERU, 0, 0, 900, 900)

t_naglowek = Tekst(1045, 60, WHITE, 40, CZCIONKA, 'WYNIK:')
t_grasz = Tekst(930, 100, LIME, 40, CZCIONKA, 'GRACZ')
t_ai = Tekst(1190, 100, RED, 40, CZCIONKA, 'AI')
t_kto_zaczyna = Tekst(230, 60, BLACK, 50, CZCIONKA, 'Kto ma zacząć rozgrywkę:')

t_blad_naglowek = Tekst(925, 510, BLACK, BLAD_ROZM, CZCIONKA, 'Błąd:')

t_blad = []
t_blad.append(Tekst(925, 525, BLACK, BLAD_ROZM, CZCIONKA, 'Wybrałeś pole na którym nie ma pionka.'))
t_blad.append(Tekst(925, 525, BLACK, BLAD_ROZM, CZCIONKA, 'Wybrałeś pionek przeciwnika.'))
t_blad.append(Tekst(925, 525, BLACK, BLAD_ROZM, CZCIONKA, 'To pole jest zajęte.'))
t_blad.append(Tekst(925, 525, BLACK, BLAD_ROZM, CZCIONKA, 'To pole nie sąsiaduje z wybranym pionkiem.'))
t_blad.append(Tekst(925, 525, BLACK, BLAD_ROZM, CZCIONKA, 'Brak błędu.'))

t_opis = []
t_opis.append(Tekst(10, 400, BLACK, OPIS_ROZM, CZCIONKA, 'Witaj w grze Kółko i krzyżyk!'))
t_opis.append(Tekst(10, 430, BLACK, OPIS_ROZM, CZCIONKA, 'Zasady gry:'))
t_opis.append(Tekst(10, 460, BLACK, OPIS_ROZM, CZCIONKA, '1. Gra jest toczona pomiędzy graczem a komputerem.'))
t_opis.append(
    Tekst(10, 490, BLACK, OPIS_ROZM, CZCIONKA, '2. Gracz oraz przeciwnik rozstawiają na planszy po trzy swoje '
                                               'pionki.'))
t_opis.append(Tekst(10, 520, BLACK, OPIS_ROZM, CZCIONKA, '3. Po rozstawieniu w systemie turowym,'))
t_opis.append(Tekst(10, 550, BLACK, OPIS_ROZM, CZCIONKA, '    każdy z grających wybiera pionek'))
t_opis.append(Tekst(10, 580, BLACK, OPIS_ROZM, CZCIONKA, '    oraz pole puste,na które chce przenieść pionek.'))
t_opis.append(Tekst(10, 610, BLACK, OPIS_ROZM, CZCIONKA, '4. Gra toczy się do momentu, w którym jeden z graczy'))
t_opis.append(Tekst(10, 640, BLACK, OPIS_ROZM, CZCIONKA, '    ustawi w jednym rzędzie swoje 3 pionki.'))


def przekaz_ture(kogo_ruch, wygrana):
    if wygrana != 1:
        if kogo_ruch == GRACZ:
            kto = " Gracz"
            return Tekst(915, 350, GOLD, 50, CZCIONKA, 'Ruch: {}'.format(kto))
        elif kogo_ruch == KOMPUTER:
            kto = " Komputer"
            return Tekst(915, 350, GOLD, 50, CZCIONKA, 'Ruch: {}'.format(kto))
    else:
        kto = " Koniec gry"
        return Tekst(915, 350, GOLD, 50, CZCIONKA, 'Ruch: {}'.format(kto))


def przekaz_wynik(zwycięzca, okno):
    if zwycięzca == GRACZ:
        tekst = Tekst(925, 470, BLACK, 28, CZCIONKA, 'Wygrał gracz!')
    elif zwycięzca == KOMPUTER:
        tekst = Tekst(925, 470, BLACK, 28, CZCIONKA, 'Wygrał komputer!')
    tekst.napisz(okno)


def nadpisz(stan, punkt_ai ,punkt_gracz, blad, kogo_ruch, wygrana, plansza, okno):
    okno.fill(SADDLEBROWN)
    przekaz_ture(kogo_ruch, wygrana).napisz(okno)
    p_reset.rysuj(okno)
    p_wyjscie.rysuj(okno)
    pole_informacyjne.rysuj(okno)

    t_stan = Tekst(1070, 100, WHITE, 40, CZCIONKA, '{} : {}'.format(punkt_gracz, punkt_ai))
    t_stan.napisz(okno)

    t_naglowek.napisz(okno)
    t_grasz.napisz(okno)
    t_ai.napisz(okno)
    t_blad_naglowek.napisz(okno)

    if stan == False:
        rysuj_pole_gry(okno)
        rysuj_pionek(okno, LIME, RED, plansza)
        p_menu.rysuj(okno)
    else:
        pole_menu.rysuj(okno)
        t_kto_zaczyna.napisz(okno)
        p_wstecz.rysuj(okno)
        p_gracz.rysuj(okno)
        p_komputer.rysuj(okno)

        for i in range(9):
            t_opis[i].napisz(okno)

    t_blad[blad].napisz(okno)
