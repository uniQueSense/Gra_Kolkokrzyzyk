import pygame
from dane import stale


def rysuj_pionek(okno, k_gracz, k_ai, pole_gry):  # Funkcja rysująca pionki w GUI
    for i in range(stale.WYMIAR_PLANSZY):
        for j in range(stale.WYMIAR_PLANSZY):
            środek = (
                (j * stale.ROZMIAR_POLA) + stale.POL_ROZMIARY_POLA, (i * stale.ROZMIAR_POLA) + stale.POL_ROZMIARY_POLA)
            if pole_gry[i][j] == stale.GRACZ:
                pygame.draw.circle(okno, k_gracz, środek, stale.SREDNICA_PIONKA)
            if pole_gry[i][j] == stale.KOMPUTER:
                pygame.draw.circle(okno, k_ai, środek, stale.SREDNICA_PIONKA)
