import pygame
import sys

from dane import kolory
from dane import stale
from funkcje_rysujace import assets
from funkcje_rysujace import napisy_przyciski
from funkcje_rysujace import obszar_gry
from obsluga_ruchow import poruszanie
from obsluga_ruchow import sprawdzanie_ruchow
from sztuczna_inteligencja import minimax


def zlicz_punkty(koniec, punkt_gracz, punkt_ai, wygrana, zwyciezca):
    if koniec and wygrana:
        if zwyciezca == stale.GRACZ:
            punkt_gracz += 1
        elif zwyciezca == stale.KOMPUTER:
            punkt_ai += 1
        koniec = False
    return punkt_ai, punkt_gracz, koniec


def obluga_przyciskow(event, ilosc, kogo_ruch, koniec, plansza, pos, wartosc, wygrana):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if napisy_przyciski.p_reset.isOver(pos) and wygrana:
            plansza = obszar_gry.stworz_tablice()
            ilosc = 0
            kogo_ruch = stale.GRACZ
            wygrana = False
            koniec = True
        if napisy_przyciski.p_wyjscie.isOver(pos):
            pygame.quit()
            sys.exit(0)
        if not wartosc and (not ilosc or wygrana):
            if napisy_przyciski.p_menu.isOver(pos):
                wartosc = True
        else:
            if napisy_przyciski.p_gracz.isOver(pos):
                kogo_ruch = stale.GRACZ
            if napisy_przyciski.p_komputer.isOver(pos):
                kogo_ruch = stale.KOMPUTER
            if napisy_przyciski.p_wstecz.isOver(pos):
                wartosc = False

            # Zmiana barwy po najechaniu na przyciski.
    if event.type == pygame.MOUSEMOTION:
        if napisy_przyciski.p_reset.isOver(pos):
            napisy_przyciski.p_reset.kolor = kolory.PRZYCISKI_KOLOR2
        else:
            napisy_przyciski.p_reset.kolor = kolory.PRZYCISKI_KOLOR1
        if napisy_przyciski.p_wyjscie.isOver(pos):
            napisy_przyciski.p_wyjscie.kolor = kolory.PRZYCISKI_KOLOR2
        else:
            napisy_przyciski.p_wyjscie.kolor = kolory.PRZYCISKI_KOLOR1
        if napisy_przyciski.p_menu.isOver(pos):
            napisy_przyciski.p_menu.kolor = kolory.PRZYCISKI_KOLOR2
        else:
            napisy_przyciski.p_menu.kolor = kolory.PRZYCISKI_KOLOR1
        if wartosc:
            if napisy_przyciski.p_wstecz.isOver(pos):
                napisy_przyciski.p_wstecz.kolor = kolory.PRZYCISKI_KOLOR2
            else:
                napisy_przyciski.p_wstecz.kolor = kolory.KOLOR_P_WSTECZ
            if napisy_przyciski.p_komputer.isOver(pos):
                napisy_przyciski.p_komputer.kolor = kolory.KOLOR1_WYBORU_GRACZA
            else:
                napisy_przyciski.p_komputer.kolor = kolory.KOLOR2_WYBORU_GRACZA
            if napisy_przyciski.p_gracz.isOver(pos):
                napisy_przyciski.p_gracz.kolor = kolory.KOLOR1_WYBORU_GRACZA
            else:
                napisy_przyciski.p_gracz.kolor = kolory.KOLOR2_WYBORU_GRACZA
    return ilosc, koniec, kogo_ruch, plansza, wartosc, wygrana


def pierwszy_etap_gry(blad, event, ilosc, kogo_ruch, plansza, punkt_gracz, punkt_ai, wygrana):
    # Obsługa ruchów GRACZA
    if kogo_ruch == stale.GRACZ and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        mouseX, mouseY = event.pos
        if mouseX <= stale.ROZMIAR_PLANSZY and mouseY <= stale.ROZMIAR_PLANSZY:
            osy = (mouseY // stale.ROZMIAR_POLA)
            osx = (mouseX // stale.ROZMIAR_POLA)
            kogo_ruch, ilosc, blad = poruszanie.postaw_znak(osy, osx, kogo_ruch, ilosc, plansza)

        # Obsługa ruchów KOMPUTERA
    elif kogo_ruch == stale.KOMPUTER:
        osy, osx = minimax.minimax_ustawianie(stale.GLEBOKOSC, True, plansza)[0]
        kogo_ruch, ilosc, blad = poruszanie.postaw_znak(osy, osx, kogo_ruch, ilosc, plansza)
    zwyciezca = sprawdzanie_ruchow.kto_wygral(punkt_gracz, punkt_ai, plansza)
    if zwyciezca:
        wygrana = True
    return blad, ilosc, kogo_ruch, plansza, punkt_gracz, punkt_ai, wygrana, zwyciezca


def drugi_etap_gry(blad, event, kogo_ruch, plansza, punkt_gracz, punkt_ai, wybrano, wygrana, osy0, osx0):
    # Obsługa ruchów GRACZA
    if kogo_ruch == stale.GRACZ:
        if not wybrano:
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouseX, mouseY = event.pos
                if mouseX <= stale.ROZMIAR_PLANSZY and mouseY <= stale.ROZMIAR_PLANSZY:
                    temp_osy0 = (mouseY // stale.ROZMIAR_POLA)
                    temp_osx0 = (mouseX // stale.ROZMIAR_POLA)
                if plansza[temp_osy0][temp_osx0] == stale.GRACZ:
                    osx0 = temp_osx0
                    osy0 = temp_osy0
                    wybrano = True
        else:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouseX, mouseY = event.pos
                if mouseX <= stale.ROZMIAR_PLANSZY and mouseY <= stale.ROZMIAR_PLANSZY:
                    osy1 = (mouseY // stale.ROZMIAR_POLA)
                    osx1 = (mouseX // stale.ROZMIAR_POLA)
                if sprawdzanie_ruchow.sasiadujace(osx0, osy0, osx1, osy1):
                    kogo_ruch, blad = poruszanie.porusz_znak(osy0, osx0, osy1, osx1, kogo_ruch, plansza)
                else:
                    blad = napisy_przyciski.blad_zle_pole
                wybrano = False

    elif kogo_ruch == stale.KOMPUTER:  # Obsługa ruchów KOMPUTERA
        index0, index1, _ = minimax.minimax_przemieszczanie(stale.GLEBOKOSC, True, plansza)
        osx0, osy0 = index0[1], index0[0]
        osx1, osy1 = index1[1], index1[0]
        kogo_ruch, blad = poruszanie.porusz_znak(osy0, osx0, osy1, osx1, kogo_ruch, plansza)
    zwyciezca = sprawdzanie_ruchow.kto_wygral(punkt_gracz, punkt_ai, plansza)
    if zwyciezca:
        wygrana = True
    return blad, kogo_ruch, plansza, punkt_gracz, punkt_ai, zwyciezca, wygrana, wybrano, osx0, osy0


def main():
    # Zmienne
    osx0 = -1
    osy0 = -1
    kogo_ruch = stale.GRACZ
    zwyciezca = 0
    ilosc = 0  # zlicza ruchy, kontroluje ilosc pionków w grze
    wartosc = False  # zmienna sprawdzająca czy menu zostało otwarte
    wygrana = False
    wybrano = False  # sprawdza czy wybrano pionek do przesuniecia
    koniec = True
    plansza = obszar_gry.stworz_tablice()
    punkt_gracz, punkt_ai = 0, 0  # zmienna zliczajaca punkty gracza / komputera
    blad = napisy_przyciski.brak_bledu  # zmienna przechowujaca blad
    pygame.init()

    pygame.font.get_fonts()
    okno = pygame.display.set_mode(stale.ROZMIAR)
    pygame.display.set_caption("* * * * Kółko i krzyżyk * * * *")
    assets.Assets.load()

    while True:
        pygame.display.update()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            ilosc, koniec, kogo_ruch, plansza, wartosc, wygrana = obluga_przyciskow(event, ilosc, kogo_ruch, koniec,
                                                                                    plansza, pos, wartosc, wygrana)

            # Rozstawianie pionków po przez wciśnięcie myszki w danym polu,
            # zmienna ilosc zlicza nam ile pionkow zostalo juz rozstawionych
            if ilosc != stale.ILOSC_PIONKOW and not wartosc and not wygrana:
                blad, ilosc, kogo_ruch, plansza, punkt_gracz, punkt_ai, wygrana, zwyciezca = pierwszy_etap_gry(blad,
                                                                                                               event,
                                                                                                               ilosc,
                                                                                                               kogo_ruch,
                                                                                                               plansza,
                                                                                                               punkt_gracz,
                                                                                                               punkt_ai,
                                                                                                               wygrana)
                punkt_ai, punkt_gracz, koniec = zlicz_punkty(koniec, punkt_gracz, punkt_ai, wygrana, zwyciezca)

                # Przemieszczanie rozstawionych pionków.
            elif ilosc == stale.ILOSC_PIONKOW and not wartosc and not wygrana:
                blad, kogo_ruch, plansza, punkt_gracz, punkt_ai, zwyciezca, wygrana, wybrano, osx0, osy0 = drugi_etap_gry(
                    blad, event, kogo_ruch, plansza, punkt_gracz, punkt_ai, wybrano, wygrana, osx0, osy0)
                punkt_ai, punkt_gracz, koniec = zlicz_punkty(koniec, punkt_gracz, punkt_ai, wygrana, zwyciezca)

        # Funkcja ta wyświetla interfejs i oprawę graficzną gry.
        napisy_przyciski.nadpisz(wartosc, punkt_ai, punkt_gracz, blad, kogo_ruch, wygrana, plansza, okno)

        # Wypisuje zwycięzce.
        if wygrana:
            napisy_przyciski.przekaz_wynik(zwyciezca, okno)

        pygame.display.flip()


if __name__ == '__main__':
    main()
