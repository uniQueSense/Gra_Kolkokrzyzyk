import pygame

def rysuj_pole_gry(okno):
    for i in range(3):
        for j in range(3):
            kwadrat = pygame.Rect(j * 300, i * 300, 300, 300)
            pygame.draw.rect(okno, (50 * i, 50 * j, 100 + 20 * i + 30 * j), kwadrat)