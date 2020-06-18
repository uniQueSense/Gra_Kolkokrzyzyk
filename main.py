import pygame
import sys
import time

from funkcje_rysujace.napisy_przyciski import p_menu, blad5, blad4
from funkcje_rysujace.napisy_przyciski import przekaz_wynik
from funkcje_rysujace.napisy_przyciski import p_wstecz
from funkcje_rysujace.napisy_przyciski import p_reset
from funkcje_rysujace.napisy_przyciski import p_wyjscie
from funkcje_rysujace.napisy_przyciski import p_gracz
from funkcje_rysujace.napisy_przyciski import p_komputer
from funkcje_rysujace.napisy_przyciski import nadpisz
from obsluga_ruchow.poruszanie import postaw_znak
from obsluga_ruchow.poruszanie import porusz_znak
from obsluga_ruchow.sprawdzanie_ruchow import kto_wygral
from obsluga_ruchow.sprawdzanie_ruchow import stworz_tablice
from stale.stale import GRACZ
from stale.stale import GLEBOKOSC
from stale.stale import ILOSC_PIONKOW
from stale.stale import KOMPUTER
from stale.stale import KOLOR2_WYBORU_GRACZA
from stale.stale import KOLOR1_WYBORU_GRACZA
from stale.stale import KOLOR_P_WSTECZ
from stale.stale import PRZYCISKI_KOLOR1
from stale.stale import PRZYCISKI_KOLOR2
from stale.stale import ROZMIAR_POLA
from stale.stale import ROZMIAR_PLANSZY
from stale.stale import ROZMIAR
from sztuczna_inteligencja.minimax import minimax_ustawianie
from sztuczna_inteligencja.minimax import minimax_przemieszczanie
from sztuczna_inteligencja.minimax import sasiadujace


def main():
    ''' Zmienne '''
    kogo_ruch = GRACZ
    zwyciezca = 0
    ilosc = 0  # zlicza ruchy
    wartosc = False
    wygrana = False
    wybrano = False  # sprawdza czy wybrano pionek do przesuniecia
    koniec = True
    plansza = stworz_tablice()
    punkt_gracz, punkt_ai = 0, 0
    blad = blad5

    pygame.init()

    pygame.font.get_fonts()
    okno = pygame.display.set_mode(ROZMIAR)
    pygame.display.set_caption("* * * * Kółko i krzyżyk * * * *")

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
                if not wartosc:
                    if p_menu.isOver(pos):
                        wartosc = True
                elif wartosc:
                    if p_gracz.isOver(pos):
                        kogo_ruch = GRACZ
                    if p_komputer.isOver(pos):
                        kogo_ruch = KOMPUTER
                    if p_wstecz.isOver(pos):
                        wartosc = False

                    ''' Zmiana barwy po najcheaniu na przyciski.'''
            if event.type == pygame.MOUSEMOTION:
                if p_reset.isOver(pos):
                    p_reset.kolor = PRZYCISKI_KOLOR2
                else:
                    p_reset.kolor = PRZYCISKI_KOLOR1
                if p_wyjscie.isOver(pos):
                    p_wyjscie.kolor = PRZYCISKI_KOLOR2
                else:
                    p_wyjscie.kolor = PRZYCISKI_KOLOR1
                if p_menu.isOver(pos):
                    p_menu.kolor = PRZYCISKI_KOLOR2
                else:
                    p_menu.kolor = PRZYCISKI_KOLOR1

                if wartosc:
                    if p_wstecz.isOver(pos):
                        p_wstecz.kolor = PRZYCISKI_KOLOR2
                    else:
                        p_wstecz.kolor = KOLOR_P_WSTECZ
                    if p_komputer.isOver(pos):
                        p_komputer.kolor = KOLOR1_WYBORU_GRACZA
                    else:
                        p_komputer.kolor = KOLOR2_WYBORU_GRACZA
                    if p_gracz.isOver(pos):
                        p_gracz.kolor = KOLOR1_WYBORU_GRACZA
                    else:
                        p_gracz.kolor = KOLOR2_WYBORU_GRACZA

            ''' Rozstawianie pionków po przez wciśnięcie myszki w danym polu,
                zmienna ilosc zlicza nam ile pionkow zostalo juz rozstawionych '''
            if ilosc != ILOSC_PIONKOW and not wartosc and not wygrana:

                ''' Obsługa ruchów GRACZA '''
                if kogo_ruch == GRACZ and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouseX, mouseY = event.pos
                    if mouseX <= ROZMIAR_PLANSZY and mouseY <= ROZMIAR_PLANSZY:
                        osy = (mouseY // ROZMIAR_POLA)
                        osx = (mouseX // ROZMIAR_POLA)
                        kogo_ruch, ilosc, blad = postaw_znak(osy, osx, kogo_ruch, ilosc, plansza)

                    ''' Obsługa róchów KOMPUTERA '''
                elif kogo_ruch == KOMPUTER:
                    index = minimax_ustawianie(GLEBOKOSC, True, plansza)[0]
                    osx = index[1]
                    osy = index[0]
                    time.sleep(1)
                    kogo_ruch, ilosc, blad = postaw_znak(osy, osx, kogo_ruch, ilosc, plansza)
                zwyciezca = kto_wygral(punkt_gracz, punkt_ai, plansza)
                if zwyciezca:
                    wygrana = True
                if koniec and wygrana:
                    if zwyciezca == GRACZ:
                        punkt_gracz += 1
                    elif zwyciezca == KOMPUTER:
                        punkt_ai += 1
                    koniec = False

                ''' Przemieszczanie rozstawionych pionków.'''
            elif ilosc == ILOSC_PIONKOW and not wartosc and not wygrana:
                ''' Obsługa ruchów GRACZA '''
                if kogo_ruch == GRACZ and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouseX, mouseY = event.pos
                    if mouseX <= ROZMIAR_PLANSZY and mouseY <= ROZMIAR_PLANSZY and not wybrano:
                        osy0 = (mouseY // ROZMIAR_POLA)
                        osx0 = (mouseX // ROZMIAR_POLA)
                        wybrano = True
                    elif mouseX <= ROZMIAR_PLANSZY and mouseY <= ROZMIAR_PLANSZY and wybrano:
                        osy1 = (mouseY // ROZMIAR_POLA)
                        osx1 = (mouseX // ROZMIAR_POLA)
                        if sasiadujace(osx0, osy0, osx1, osy1):
                            kogo_ruch, blad = porusz_znak(osy0, osx0, osy1, osx1, kogo_ruch, plansza)
                            wybrano = False
                        else:
                            blad = blad4
                            wybrano = False

                            ''' Obsługa róchów KOMPUTERA '''
                elif kogo_ruch == KOMPUTER:
                    index0, index1, l = minimax_przemieszczanie(GLEBOKOSC, True, plansza)
                    osx0, osy0 = index0[1], index0[0]
                    osx1, osy1 = index1[1], index1[0]
                    time.sleep(1)
                    kogo_ruch, blad = porusz_znak(osy0, osx0, osy1, osx1, kogo_ruch, plansza)

                zwyciezca = kto_wygral(punkt_gracz, punkt_ai, plansza)
                if zwyciezca:
                    wygrana = True

                    ''' Dodawanie punktów GRACZA lub KOMPUTERA'''
                if koniec and wygrana:
                    if zwyciezca == GRACZ:
                        punkt_gracz += 1
                    elif zwyciezca == KOMPUTER:
                        punkt_ai += 1
                    koniec = False

        ''' Funkcja ta wyświetla interfejs i oprawę graficzną gry. '''
        nadpisz(wartosc, punkt_ai, punkt_gracz, blad, kogo_ruch, wygrana, plansza, okno)

        ''' Wypisuje zwycięzce. '''
        if wygrana:
            przekaz_wynik(zwyciezca, okno)

        pygame.display.flip()


if __name__ == '__main__':
    main()
