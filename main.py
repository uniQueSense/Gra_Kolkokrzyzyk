import random
import sys
import time

from funkcje_rysujace.napisy_przyciski import *
from obsluga_ruchow.poruszanie import *
from sztuczna_inteligencja.minimax import *
from stale.stale import *

''' Zmienne globalne '''
kogo_ruch = GRACZ
zwycięzca = 0
ilosc = 0  # zlicza ruchy
wartosc = False
wygrana = False  # sprawdza czy wybrano pionek do przesuniecia
wybrano = False
koniec = True
plansza = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

punkt_gracz, punkt_ai = 0, 0
blad = 4  # 4 wyswietla brak bledu

pygame.init()

pygame.font.get_fonts()
okno = pygame.display.set_mode(ROZMIAR)
pygame.display.set_caption("* * * * Kółko i krzyżyk * * * *")


def kto_wygral(punkt_gracz, punkt_ai):
    zwycięzca = sprawdz_pola(plansza)
    if zwycięzca:
        if zwycięzca == GRACZ:
            punkt_gracz += 1
        if zwycięzca == KOMPUTER:
            punkt_ai += 1
        zwycięzca = sprawdz_pola(plansza)
        return zwycięzca
    return False


while True:
    pygame.display.update()
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        '''*********** obsługa przycisków *************'''
        if event.type == pygame.MOUSEBUTTONDOWN:
            if p_reset.isOver(pos):
                plansza = [[0, 0, 0],
                           [0, 0, 0],
                           [0, 0, 0]]
                ilosc = 0
                kogo_ruch = GRACZ
                wygrana = False
                koniec = True
            if p_wyjscie.isOver(pos):
                pygame.quit()
                sys.exit(0)
            if wartosc == False:
                if p_menu.isOver(pos):
                    wartosc = True
            elif wartosc == True:
                if p_gracz.isOver(pos):
                    kogo_ruch = GRACZ
                if p_komputer.isOver(pos):
                    kogo_ruch = KOMPUTER
                if p_wstecz.isOver(pos):
                    wartosc = False
        if event.type == pygame.MOUSEMOTION:
            if p_reset.isOver(pos):
                p_reset.kolor = ROSYBROWN
            else:
                p_reset.kolor = MARON
            if p_wyjscie.isOver(pos):
                p_wyjscie.kolor = ROSYBROWN
            else:
                p_wyjscie.kolor = MARON
            if p_menu.isOver(pos):
                p_menu.kolor = ROSYBROWN
            else:
                p_menu.kolor = MARON

            if wartosc == True:
                if p_wstecz.isOver(pos):
                    p_wstecz.kolor = ROSYBROWN
                else:
                    p_wstecz.kolor = BROWN
                if p_komputer.isOver(pos):
                    p_komputer.kolor = RED
                else:
                    p_komputer.kolor = BLUE
                if p_gracz.isOver(pos):
                    p_gracz.kolor = RED
                else:
                    p_gracz.kolor = BLUE

        '''*******************************************'''

        if ilosc < 6 and wartosc == False and wygrana == False:
            if kogo_ruch == GRACZ and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouseX, mouseY = event.pos
                if mouseX <= 900 and mouseY <= 900:
                    osy = (mouseY // 300)
                    osx = (mouseX // 300)
                    kogo_ruch, ilosc, blad = postaw_znak(osy, osx, kogo_ruch, ilosc, plansza)
            elif kogo_ruch == KOMPUTER:
                index = minimax_ustawianie(3, True, plansza)[0]
                osx = index[1]
                osy = index[0]
                time.sleep(1)
                kogo_ruch, ilosc, blad = postaw_znak(osy, osx, kogo_ruch, ilosc, plansza)
            zwycięzca = kto_wygral(punkt_gracz, punkt_ai)
            if zwycięzca:
                wygrana = True
            if koniec and wygrana:
                if zwycięzca == GRACZ:
                    punkt_gracz += 1
                elif zwycięzca == KOMPUTER:
                    punkt_ai += 1
                koniec = False

        elif ilosc == 6 and wartosc == False and wygrana == False:
            if kogo_ruch == GRACZ and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouseX, mouseY = event.pos
                if mouseX <= 900 and mouseY <= 900 and wybrano == False:
                    osy0 = (mouseY // 300)
                    osx0 = (mouseX // 300)
                    wybrano = True
                elif mouseX <= 900 and mouseY <= 900 and wybrano == True:
                    osy1 = (mouseY // 300)
                    osx1 = (mouseX // 300)
                    if sasiadujace(osx0, osy0, osx1, osy1):
                        kogo_ruch, blad = porusz_znak(osy0, osx0, osy1, osx1, kogo_ruch, plansza)
                        wybrano = False
                    else:
                        blad = 3
                        wybrano = False
            elif kogo_ruch == KOMPUTER:
                index0, index1, l = minimax_przemieszczanie(3, True, plansza)
                osx0, osy0 = index0[1], index0[0]
                osx1, osy1 = index1[1], index1[0]
                time.sleep(1)
                kogo_ruch, blad = porusz_znak(osy0, osx0, osy1, osx1, kogo_ruch, plansza)
            zwycięzca = kto_wygral(punkt_gracz, punkt_ai)
            if zwycięzca:
                wygrana = True

            if koniec and wygrana:
                if zwycięzca == GRACZ:
                    punkt_gracz += 1
                elif zwycięzca == KOMPUTER:
                    punkt_ai += 1
                koniec = False

    nadpisz(wartosc, punkt_ai ,punkt_gracz, blad, kogo_ruch, wygrana, plansza, okno)

    if wygrana:
        przekaz_wynik(zwycięzca, okno)

    pygame.display.flip()
