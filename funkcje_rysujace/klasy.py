import pygame
from dane import stale


class Blok:
    ''' Klasa tworzy element graficzny w ksztalcie prostokąta '''

    def __init__(self, kolor, osx, osy, dlugosc, wysokosc):
        self.kolor = kolor
        self.osx = osx
        self.osy = osy
        self.dlugosc = dlugosc
        self.wysokosc = wysokosc

    def rysuj(self, okno):
        pygame.draw.rect(okno, self.kolor, (self.osx, self.osy, self.dlugosc, self.wysokosc), 0)


class Tekst:
    ''' Klasa wypisuje tekst w GUI '''

    def __init__(self, osx, osy, kolor, rozmiar, czcionka='', tekst=''):
        self.osx = osx
        self.osy = osy
        self.kolor = kolor
        self.rozmiar = rozmiar
        self.czcionka = czcionka
        self.tekst = tekst

    def napisz(self, okno):
        font = pygame.font.SysFont(self.czcionka, self.rozmiar)
        tekst = font.render(self.tekst, 1, self.kolor)
        okno.blit(tekst, (self.osx, self.osy))


class Przycisk:
    ''' Klasa tworzy przycisk, w którego wnętrzu zawiera się tekst '''

    def __init__(self, kolor, kolor_tekst, osx, osy, dlugosc, wysokosc, tekst=''):
        self.kolor = kolor
        self.kolor_tekst = kolor_tekst
        self.osx = osx
        self.osy = osy
        self.dlugosc = dlugosc
        self.wysokosc = wysokosc
        self.tekst = tekst

    def rysuj(self, screen, outline=None):
        if outline:
            pygame.draw.rect(screen, self.kolor, (self.osx - 2, self.osy - 2, self.dlugosc + 4, self.wysokosc + 4), 0)
        pygame.draw.rect(screen, self.kolor, (self.osx, self.osy, self.dlugosc, self.wysokosc), 0)

        if self.tekst:
            font = pygame.font.SysFont(stale.CZCIONKA, 60)
            tekst = font.render(self.tekst, 1, self.kolor_tekst)
            screen.blit(tekst, (self.osx + (self.dlugosc / 2 - tekst.get_width() / 2),
                                self.osy - (self.wysokosc / 2 - tekst.get_height() * 0.6)))

    def isOver(self, pos):
        if pos[0] > self.osx and pos[0] < self.osx + self.dlugosc:
            if pos[1] > self.osy and pos[1] < self.osy + self.wysokosc:
                return True
        return False
