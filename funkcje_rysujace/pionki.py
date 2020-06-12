import pygame
from stale.stale import *


def rysuj_pionek(okno, k_gracz, k_ai, pole_gry):
    for i in range(3):
        for j in range(3):
            środek = ((j * 300) + 150, (i * 300) + 150)
            if pole_gry[i][j] == GRACZ:
                pygame.draw.circle(okno, k_gracz, środek, 50)
            if pole_gry[i][j] == KOMPUTER:
                pygame.draw.circle(okno, k_ai, środek, 50)
