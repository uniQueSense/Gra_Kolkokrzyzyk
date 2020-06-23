import pygame
from dane import stale


def rysuj_pole_gry(okno):  # Funkcja rysująca planszę do gry w GUI
    for i in range(stale.WYMIAR_PLANSZY):
        for j in range(stale.WYMIAR_PLANSZY):
            kwadrat = pygame.Rect(j * stale.ROZMIAR_POLA, i * stale.ROZMIAR_POLA, stale.ROZMIAR_POLA,
                                  stale.ROZMIAR_POLA)
            pygame.draw.rect(okno, (50 * i, 50 * j, 100 + 20 * i + 30 * j), kwadrat)


def stworz_tablice():  # Tworzenie pustej tablicy  3x3. 
    return [[stale.PUSTO for i in range(stale.WYMIAR_PLANSZY)] for j in range(stale.WYMIAR_PLANSZY)]
