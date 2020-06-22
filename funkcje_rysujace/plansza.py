import pygame
from stale.stale import PUSTO
from stale.stale import ROZMIAR_POLA
from stale.stale import WYMIAR_PLANSZY


def rysuj_pole_gry(okno):
    """ Funkcja rysująca planszę do gry w GUI """
    for i in range(WYMIAR_PLANSZY):
        for j in range(WYMIAR_PLANSZY):
            kwadrat = pygame.Rect(j * ROZMIAR_POLA, i * ROZMIAR_POLA, ROZMIAR_POLA, ROZMIAR_POLA)
            pygame.draw.rect(okno, (50 * i, 50 * j, 100 + 20 * i + 30 * j), kwadrat)


def stworz_tablice():
    """ Tworzenie pustej tablicy  3x3. """
    return [[PUSTO for i in range(WYMIAR_PLANSZY)] for j in range(WYMIAR_PLANSZY)]
