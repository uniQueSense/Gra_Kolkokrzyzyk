import pygame

class Blok:
    def __init__(self, kolor, osx, osy, długość, wysokość):
        self.kolor = kolor
        self.osx = osx
        self.osy = osy
        self.długość = długość
        self.wysokość = wysokość

    def rysuj(self, okno):
        pygame.draw.rect(okno, self.kolor, (self.osx, self.osy, self.długość, self.wysokość), 0)


class Tekst():
    def __init__(self, osx, osy, kolor, rozmiar, trzcionka='', tekst=''):
        self.osx = osx
        self.osy = osy
        self.kolor = kolor
        self.rozmiar = rozmiar
        self.trzcionka = trzcionka
        self.tekst = tekst

    def write(self, okno):
        font = pygame.font.SysFont(self.trzcionka, self.rozmiar)
        tekst = font.render(self.tekst, 1, self.kolor)
        okno.blit(tekst, (self.osx, self.osy))


class Przycisk():
    def __init__(self, kolor, kolor_text, osx, osy, długość, wysokość, tekst=''):
        self.kolor = kolor
        self.kolor_text = kolor_text
        self.osx = osx
        self.osy = osy
        self.długość = długość
        self.wysokość = wysokość
        self.tekst = tekst

    def draw(self, screen, outline=None):
        if outline:
            pygame.draw.rect(screen, self.kolor, (self.osx - 2, self.osy - 2, self.długość + 4, self.wysokość + 4), 0)
        pygame.draw.rect(screen, self.kolor, (self.osx, self.osy, self.długość, self.wysokość), 0)

        if self.tekst != '':
            font = pygame.font.SysFont('comicsans', 60)
            tekst = font.render(self.tekst, 1, self.kolor_text)
            screen.blit(tekst, (self.osx + (self.długość / 2 - tekst.get_width() / 2),
                                self.osy - (self.wysokość / 2 - tekst.get_height() * 0.6)))

    def isOver(self, pos):
        if pos[0] > self.osx and pos[0] < self.osx + self.długość:
            if pos[1] > self.osy and pos[1] < self.osy + self.wysokość:
                return True
        return False