import pygame

def rysuj_pionek(okno, kolor1, kolor2, pole_gry):
    for i in range(3):
        for j in range(3):
            sprawdź = j + 3 * i
            środek = ((j * 300) + 150, (i * 300) + 150)
            if pole_gry[sprawdź] == 1:
                pygame.draw.circle(okno, kolor1, środek, 50)
            if pole_gry[sprawdź] == 2:
                pygame.draw.circle(okno, kolor2, środek, 50)