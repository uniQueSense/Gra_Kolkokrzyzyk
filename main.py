import random
import sys
import pygame

from funkcje_rysujace.klasy import *
from funkcje_rysujace.pionki import *
from funkcje_rysujace.plansza import *
from obsluga_ruchow.poruszanie import *
from obsluga_ruchow.spr import *

pygame.init()

size = (1300, 900)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("* * * * Kółko i krzyżyk * * * *")

''' * * * KOLORY * * * '''
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)

''' Stała globalna '''
POLA_INDEKSY = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                [0, 3, 6], [1, 4, 7], [2, 5, 8],
                [0, 4, 8], [2, 4, 6]]

''' Zmienne globalne '''
kogo_ruch = 1
zwycięzca = 0
wygrana = False
plansza = [0, 0, 0, 0, 0, 0, 0, 0, 0]
ilość = 0  # zmienna potrzebna do wyliczenia ilości pionków na planszy
pole1 = -1
wartosc = False


def sprawdz_pola(uklad, zwycięzca=None):
    wartosc = None;
    # lista wielowymiarowa, której elementami są inne listy zagnieżdżone
    for lista in POLA_INDEKSY:
        kol = []  # lista pomocnicza
        for ind in lista:
            kol.append(plansza[ind])  # zapisz wartość odczytaną z POLE_GRY
        if (kol in uklad):  # jeżeli znalazłeś układ wygrywający lub blokujący
            # zwróć wygranego (1,2) lub indeks pola do zaznaczenia
            wartosc = zwycięzca if zwycięzca else lista[kol.index(0)]
    return wartosc


def kto_wygral():
    uklad_gracz = [[1, 1, 1]]
    uklad_komp = [[2, 2, 2]]
    zwycięzca = sprawdz_pola(uklad_gracz, 1)
    if not zwycięzca:
        zwycięzca = sprawdz_pola(uklad_komp, 2)
    return zwycięzca


def kogo_tura(kogo_ruch):
    if wygrana != 1:
        if kogo_ruch == 1:
            ktoo = " Gracz"
            wynik1 = Tekst(915, 250, yellow, 60, 'comicsans', 'Ruch:' + ktoo)
            return wynik1
        elif kogo_ruch == 2:
            ktoo = " Komputer"
            wynik1 = Tekst(915, 250, yellow, 60, 'comicsans', 'Ruch:' + ktoo)
            return wynik1
    else:
        ktoo = " Koniec gry"
        wynik1 = Tekst(915, 250, yellow, 60, 'comicsans', 'Ruch:' + ktoo)
        return wynik1


def ai(kogo_ruch, krok):
    pole = None
    win = [0, 2, 2], [2, 0, 2], [2, 2, 0]
    lose = [0, 1, 1], [1, 0, 1], [1, 1, 0]

    # priorytetowo sprawdzamy czy komputer moze wygrac
    pole1 = sprawdz_pola(win)
    if pole1 is not None:
        if krok >= 6:
            pole2 = random.randint(0, 8)
            kogo_ruch = sasiadujace(pole2, pole1, kogo_ruch, plansza)
            return kogo_ruch
        else:
            kogo_ruch, krok = postaw_znak(pole1, kogo_ruch, krok, plansza)
            return kogo_ruch, krok

    # priorytetowo sprawdzamy czy komputer moze wygrac
    pole1 = sprawdz_pola(lose)
    if pole1 is not None:
        if krok == 6:
            pole2 = random.randint(0, 8)
            kogo_ruch = sasiadujace(pole2, pole1, kogo_ruch, plansza)
            return kogo_ruch
        else:
            kogo_ruch, krok = postaw_znak(pole1, kogo_ruch, krok, plansza)
            return kogo_ruch, krok

    # jeśli komputer zaczyna pole jest losowane losowo

    if pole1 is None:
        pole1 = random.randint(0, 8)
        pole2 = random.randint(0, 8)
        if krok == 6:
            kogo_ruch = sasiadujace(pole1, pole2, kogo_ruch,plansza)
            return kogo_ruch
        else:
            kogo_ruch, krok = postaw_znak(pole1, kogo_ruch, krok, plansza)
            return kogo_ruch, krok


reset = Przycisk(red, green, 915, 840, 170, 45, 'Reset')
wyjście = Przycisk(red, green, 1115, 840, 170, 45, 'Wyjdź')
menu = Przycisk(red, green, 915, 780, 370, 45, 'Menu')
wstecz = Przycisk(red, green, 915, 780, 370, 45, 'Wstecz')
pole_informacyjne = Blok(white, 915, 400, 370, 300)
wynik = Tekst(1020, 25, white, 60, 'comicsans', 'Wynik:')
kto_ma_zaczynać = Tekst(10, 15, black, 50, 'comicsans', 'Kto ma zacząć rozgrywkę:')
pole_menu = Blok(white, 0, 0, 900, 900)
zaczyna_gracz = Przycisk(black, green, 10, 70, 250, 45, 'Gracz')
zaczyna_komputer = Przycisk(black, green, 270, 70, 250, 45, 'Komputer')
zaczyna_losowo = Przycisk(black, green, 530, 70, 250, 45, 'Losowo')
informacje = Tekst(10, 400, black, 32, "freesansbold.ttf", "tu ma byc opis")


def drukuj_wynik(zwycięzca):
    if zwycięzca == 1:
        tekst = Tekst(930, 415, black, 28, 'freesansbold.ttf', 'Wygrał gracz!')
    elif zwycięzca == 2:
        tekst = Tekst(930, 415, black, 28, 'freesansbold.ttf', 'Wygrał komputer!')
    tekst.write(screen)


def redraw(wartosc, kogo_ruch):
    screen.fill((0, 0, 0))
    kogo_tura(kogo_ruch).write(screen)
    reset.draw(screen)
    wynik.write(screen)
    wyjście.draw(screen)
    pole_informacyjne.rysuj(screen)
    if wartosc == False:
        rysuj_pole_gry(screen)
        rysuj_pionek(screen, blue, red, plansza)
        menu.draw(screen)
    else:
        pole_menu.rysuj(screen)
        kto_ma_zaczynać.write(screen)
        wstecz.draw(screen)
        zaczyna_gracz.draw(screen)
        zaczyna_komputer.draw(screen)
        zaczyna_losowo.draw(screen)
        informacje.write(screen)


while True:
    pygame.display.update()
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        '''*********** obsluga przycisków *************'''
        if event.type == pygame.MOUSEBUTTONDOWN:
            if reset.isOver(pos):
                plansza = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                ilość = 0
                kogo_ruch = 1
                wygrana = False

            if wyjście.isOver(pos):
                pygame.quit()
                sys.exit(0)

            if wartosc == False:
                if menu.isOver(pos):
                    wartosc = True

            elif wartosc == True:
                if zaczyna_gracz.isOver(pos):
                    kogo_ruch = 1
                if zaczyna_komputer.isOver(pos):
                    kogo_ruch = 2
                if zaczyna_losowo.isOver(pos):
                    kogo_ruch = random.randint(1, 2)
                if wstecz.isOver(pos):
                    wartosc = False
        if event.type == pygame.MOUSEMOTION:
            if reset.isOver(pos):
                reset.kolor = red
            else:
                reset.kolor = blue
            if wyjście.isOver(pos):
                wyjście.kolor = red
            else:
                wyjście.kolor = blue
            if menu.isOver(pos):
                menu.kolor = red
            else:
                menu.kolor = blue

            if wartosc == True:
                if wstecz.isOver(pos):
                    wstecz.kolor = white
                else:
                    wstecz.kolor = yellow

                if zaczyna_losowo.isOver(pos):
                    zaczyna_losowo.kolor = red
                else:
                    zaczyna_losowo.kolor = blue

                if zaczyna_komputer.isOver(pos):
                    zaczyna_komputer.kolor = red
                else:
                    zaczyna_komputer.kolor = blue

                if zaczyna_gracz.isOver(pos):
                    zaczyna_gracz.kolor = red
                else:
                    zaczyna_gracz.kolor = blue
        '''*******************************************'''

        if ilość < 6 and wartosc == False:  # po postawieniu 6 pionka nie możemy umieścić już więcej
            if wygrana == False:
                if kogo_ruch == 1:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:  # jeżeli naciśnięto pierwszy przycisk
                            mouseX, mouseY = event.pos  # rozpakowanie tupli
                            if mouseX <= 900 and mouseY <= 900:  # uniemożliwia kliknięcie obszaru poza planszą do gry
                                pole = ((mouseY // 300) * 3) + (mouseX // 300)  # wylicz indeks klikniętego pola
                                kogo_ruch, ilość = postaw_znak(pole, kogo_ruch, ilość, plansza)
                elif kogo_ruch == 2:
                    kogo_ruch , ilość= ai(kogo_ruch, ilość)
                    # if event.type == pygame.MOUSEBUTTONDOWN:
                    #     if event.button == 1:
                    #         mouseX, mouseY = event.pos
                    #         if mouseX <= 900 and mouseY <= 900:
                    #             pole = ((mouseY // 300) * 3) + (mouseX // 300)
                    #             kogo_ruch, ilość = postaw_znak(pole, kogo_ruch, ilość)
                zwycięzca = kto_wygral()
                if zwycięzca != None:
                    wygrana = True
        if ilość == 6 and wartosc == False:  # zmiana miejsca pionka na planszy
            if wygrana == False:
                if kogo_ruch == 1:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            mouseX, mouseY = event.pos
                            if mouseX <= 900 and mouseY <= 900:
                                if pole1 == -1:
                                    pole1 = ((mouseY // 300) * 3) + (mouseX // 300)
                                else:
                                    if ((mouseY // 300) * 3) + (mouseX // 300) != pole1:
                                        pole2 = ((mouseY // 300) * 3) + (mouseX // 300)
                                        kogo_ruch = sasiadujace(pole1, pole2, kogo_ruch, plansza)
                                        pole1 = -1
                                    else:
                                        print("To samo pole")
                elif kogo_ruch == 2:
                    kogo_ruch = ai(kogo_ruch, ilość)
                    # if event.type == pygame.MOUSEBUTTONDOWN:
                    #     if event.button == 1:
                    #         mouseX, mouseY = event.pos
                    #         if mouseX <= 900 and mouseY <= 900:
                    #             if pole1 == -1:
                    #                 pole1 = ((mouseY // 300) * 3) + (mouseX // 300)
                    #             else:
                    #                 if ((mouseY // 300) * 3) + (mouseX // 300) != pole1:
                    #                     pole2 = ((mouseY // 300) * 3) + (mouseX // 300)
                    #                     kogo_ruch = sasiadujace(pole1, pole2, kogo_ruch)
                    #                     pole1 = -1
                    #                 else:
                    #                     print("To samo pole")
                zwycięzca = kto_wygral()
                if zwycięzca != None:
                    wygrana = True

    redraw(wartosc, kogo_ruch)

    if wygrana:
        drukuj_wynik(zwycięzca)

    pygame.display.flip()



