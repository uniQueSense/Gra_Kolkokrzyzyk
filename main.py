import random
import sys

from funkcje_rysujace.klasy import *
from funkcje_rysujace.pionki import *
from funkcje_rysujace.plansza import *
from obsluga_ruchow.poruszanie import *
from obsluga_ruchow.spr import *
from sztuczna_inteligencja.minimax import *

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
GRACZ = -1
KOMPUTER = 1

''' Zmienne globalne '''
kogo_ruch = -1
zwycięzca = 0
wygrana = False
plansza = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]
ilość = 0
wartosc = False


def kto_wygral():
    zwycięzca = sprawdz_pola(plansza)
    if zwycięzca:
        zwycięzca = sprawdz_pola(plansza)
        return zwycięzca
    return False


def kogo_tura(kogo_ruch):
    if wygrana != 1:
        if kogo_ruch == GRACZ:
            ktoo = " Gracz"
            wynik1 = Tekst(915, 250, yellow, 60, 'comicsans', 'Ruch:' + ktoo)
            return wynik1
        elif kogo_ruch == KOMPUTER:
            ktoo = " Komputer"
            wynik1 = Tekst(915, 250, yellow, 60, 'comicsans', 'Ruch:' + ktoo)
            return wynik1
    else:
        ktoo = " Koniec gry"
        wynik1 = Tekst(915, 250, yellow, 60, 'comicsans', 'Ruch:' + ktoo)
        return wynik1

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
    if zwycięzca == -1:
        tekst = Tekst(930, 415, black, 28, 'freesansbold.ttf', 'Wygrał gracz!')
    elif zwycięzca == 1:
        tekst = Tekst(930, 415, black, 28, 'freesansbold.ttf', 'Wygrał komputer!')
    #else:
        #tekst = False
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

tt= 0
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
                plansza = [[0, 0, 0],
                           [0, 0, 0],
                           [0, 0, 0]]
                ilość = 0
                kogo_ruch = -1
                wygrana = False
            if wyjście.isOver(pos):
                pygame.quit()
                sys.exit(0)
            if wartosc == False:
                if menu.isOver(pos):
                    wartosc = True
            elif wartosc == True:
                if zaczyna_gracz.isOver(pos):
                    kogo_ruch = GRACZ
                if zaczyna_komputer.isOver(pos):
                    kogo_ruch = KOMPUTER
                if zaczyna_losowo.isOver(pos):
                    kogo_ruch = random.randint(-1, 1)
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
        if ilość < 6 and wartosc == False and wygrana == False:
            if kogo_ruch == GRACZ and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouseX, mouseY = event.pos
                if mouseX <= 900 and mouseY <= 900:
                    osy = (mouseY // 300)
                    osx = (mouseX // 300)
                    kogo_ruch, ilość = postaw_znak(osy, osx, kogo_ruch, ilość, plansza)
            elif kogo_ruch == KOMPUTER:
                index = minimax_ustawianie(8, True, plansza)[0]
                osx = index[1]
                osy = index[0]
                kogo_ruch, ilość = postaw_znak(osy, osx, kogo_ruch, ilość, plansza)
            zwycięzca = kto_wygral()
            if zwycięzca :
                wygrana = True
        elif ilość == 6 and wartosc==False and wygrana == False:
            if kogo_ruch == GRACZ and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouseX, mouseY = event.pos
                if mouseX <= 900 and mouseY <= 900 and tt == 0:
                    osy0 = (mouseY // 300)
                    osx0 = (mouseX // 300)
                    tt = 1
                else:
                    if mouseX <= 900 and mouseY <= 900 and plansza[(mouseY // 300)][(mouseX // 300)] == 0:
                        osy1 = (mouseY // 300)
                        osx1 = (mouseX // 300)
                        if sasiadujace(osx0, osy0, osx1, osy1):
                            kogo_ruch = porusz_znak(osy0, osx0, osy1, osx1, kogo_ruch, plansza)
                        tt = 0
                    else:
                        print("To samo pole")
            elif kogo_ruch == KOMPUTER:
                kogo_ruch = -1
            zwycięzca = kto_wygral()
            if zwycięzca:
                wygrana = True

    redraw(wartosc, kogo_ruch)
    if wygrana:
        drukuj_wynik(zwycięzca)

    pygame.display.flip()



