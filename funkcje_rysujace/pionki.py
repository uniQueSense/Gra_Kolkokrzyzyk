import pygame
from stale.stale import GRACZ
from stale.stale import KOMPUTER
from stale.stale import POL_ROZMIARY_POLA
from stale.stale import ROZMIAR_POLA
from stale.stale import SREDNIAC_PIONKA
from stale.stale import WYMIAR_PLANSZY


def rysuj_pionek(okno, k_gracz, k_ai, pole_gry):
    """ Funkcja rysująca pionki w GUI """
    for i in range(WYMIAR_PLANSZY):
        for j in range(WYMIAR_PLANSZY):
            środek = ((j * ROZMIAR_POLA) + POL_ROZMIARY_POLA, (i * ROZMIAR_POLA) + POL_ROZMIARY_POLA)
            if pole_gry[i][j] == GRACZ:
                pygame.draw.circle(okno, k_gracz, środek, SREDNIAC_PIONKA)
            if pole_gry[i][j] == KOMPUTER:
                pygame.draw.circle(okno, k_ai, środek, SREDNIAC_PIONKA)
