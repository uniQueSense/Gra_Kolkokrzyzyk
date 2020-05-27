import pygame
import sys
import random
import time
import os

pygame.init()

size = (1300, 900)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("* * * * Kółko i krzyżyk * * * *")

''' * * * KOLORY * * * '''
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
white = (255, 255, 255)
black =(0, 0, 0)
'''********************'''

''' Zmienne globalne '''
kogo_ruch = 1
zwycięzca = 0
WYGRANA = False
plansza = [0, 0, 0, 0, 0, 0, 0, 0, 0]
ilość = 0 # zmienna potrzebna do wyliczenia ilości pionków na planszy
pole1 = -1
wartosc = False
''' Stała globalna '''
POLA_INDEKSY = [[0,1,2], [3,4,5], [6,7,8],
                [0,3,6], [1,4,7], [2,5,8],
                [0,4,8], [2,4,6]]
'''---------------'''

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
    def __init__(self, osx, osy, kolor, rozmiar, trzcionka = '', tekst = ''):
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
    def __init__(self, kolor, osx, osy, długość, wysokość, tekst = ''):
        self.kolor = kolor
        self.osx = osx
        self.osy = osy
        self.długość = długość
        self.wysokość = wysokość
        self.tekst = tekst

    def draw(self, screen, outline = None):
        if outline:
            pygame.draw.rect(screen, self.kolor, (self.osx - 2, self.osy - 2, self.długość + 4, self.wysokość + 4), 0)
        pygame.draw.rect(screen, self.kolor, (self.osx, self.osy, self.długość, self.wysokość), 0)

        if self.tekst != '':
            font = pygame.font.SysFont('comicsans', 60)
            tekst = font.render(self.tekst, 1, green)
            screen.blit(tekst, (self.osx + (self.długość / 2 - tekst.get_width() / 2), self.osy - (self.wysokość / 2 - tekst.get_height() * 0.6 )))

    def isOver(self, pos):
        if pos[0] > self.osx and pos[0] < self.osx + self.długość:
            if pos[1] > self.osy and pos[1] < self.osy + self.wysokość:
                return True
        return False

# def wczytaj_plik(plikcsv):
#     """
#     Funkcja zwraca tuplę tupli zawierających dane pobrane z pliku csv
#     do zapisania w tabeli.
#     """
#     dane = []  # deklarujemy pustą listę
#     if os.path.isfile(plikcsv):  # sprawdzamy czy plik istnieje na dysku
#         with open(plikcsv, "r") as zawartosc:  # otwieramy plik do odczytu
#             for linia in zawartosc:
#                 linia = linia.replace("\n", "")  # usuwamy znaki końca linii
#                 linia = linia.replace("\r", "")  # usuwamy znaki końca linii
#                 linia = linia.decode("utf-8")  # odczytujemy znaki jako utf-8
#                 # dodajemy elementy do tupli a tuplę do listy
#                 dane.append(tuple(linia.split(",")))
#     else:
#         print("Plik z danymi", plikcsv, "nie istnieje!")
#     return tuple(dane)  # przekształcamy listę na tuplę i zwracamy ją
#
# wczytaj_plik('informacje_o_grze.txt')

def plansza_rysuj():
    for i in range(3):
        for j in range(3):
            kwadrat = pygame.Rect(j * 300, i * 300, 300, 300)
            pygame.draw.rect(screen, (50 * i, 50 * j, 100 + 20 * i + 30 * j), kwadrat)

def rysuj_pionek(kolor1, kolor2):
    for i in range(3):
        for j in range(3):
            sprawdź = j + 3 * i
            środek = ((j * 300) + 150, (i * 300) + 150)
            if plansza[sprawdź] == 1:
                pygame.draw.circle(screen, kolor1, środek, 50)
            if plansza[sprawdź] == 2:
                pygame.draw.circle(screen, kolor2, środek, 50)

def postaw_znak(pole, kogo_ruch, ilość):
    if plansza[pole] == 0:
        ilość = ilość + 1
        if kogo_ruch == 1:          # ruch gracza
            plansza[pole] = 1
            return 2, ilość
        elif kogo_ruch == 2:        # ruch komputera
            plansza[pole] = 2
            return 1, ilość
    if plansza[pole] == 1 or plansza[pole] == 2:
        print("powtórz")
        return kogo_ruch, ilość

def porusz_znak(pole1, pole2, kogo_ruch):
    if kogo_ruch == 1:
        if plansza[pole1] == 1:
            if plansza[pole2] == 0:
                plansza[pole1] = 0
                plansza[pole2] = 1
                return 2
            else:
                print('tu stoi pionek')
                return kogo_ruch
        else:
            if plansza[pole1] == 2:
                print("wybrales pionek gracza 2")
            else:
                print("na tym polu nie ma pionków1")
            return kogo_ruch
    elif kogo_ruch == 2:
        if plansza[pole1] == 2:
            if plansza[pole2] == 0:
                plansza[pole1] = 0
                plansza[pole2] = 2
                return 1
            else:
                print('tu stoi pionek')
                return kogo_ruch
        else:
            if plansza[pole1] == 2:
                print("wybrales pionek gracza 1")
            else:
                print("na tym polu nie ma pionków2")
            return kogo_ruch

def sprawdz_pola(uklad, zwycięzca = None):
    wartosc = None;
    # lista wielowymiarowa, której elementami są inne listy zagnieżdżone
    for lista in POLA_INDEKSY:
        kol = [] # lista pomocnicza
        for ind in lista:
            kol.append(plansza[ind]) # zapisz wartość odczytaną z POLE_GRY
        if (kol in uklad): # jeżeli znalazłeś układ wygrywający lub blokujący
            # zwróć wygranego (1,2) lub indeks pola do zaznaczenia
            wartosc = zwycięzca if zwycięzca else lista[kol.index(0)]
    return wartosc

def kto_wygral():
    uklad_gracz = [[1, 1, 1]]
    uklad_komp = [[2, 2, 2]]
    zwycięzca = sprawdz_pola(uklad_gracz, 1)
    if not zwycięzca:
        zwycięzca = sprawdz_pola(uklad_komp, 2)
    return zwycięzca

def kogo_tura():
    if WYGRANA != 1:
        if kogo_ruch == 1:
            ktoo = " Gracz"
            wynik1 = Tekst(915, 250, yellow, 60, 'comicsans', 'Ruch:' + ktoo)
            return wynik1
        elif kogo_ruch == 2:
            ktoo = " Komputer"
            wynik1 = Tekst(915, 250, yellow, 60, 'comicsans', 'Ruch:' + ktoo)
            return wynik1
    else:
        ktoo = " Koniec gry"
        wynik1 = Tekst(915, 250, yellow, 60, 'comicsans', 'Ruch:' + ktoo)
        return wynik1

reset = Przycisk(red, 915, 840, 170, 45, 'Reset')
wyjście = Przycisk(red, 1115, 840, 170, 45, 'Wyjdź')
menu = Przycisk(red, 915, 780, 370, 45, 'Menu')
wstecz = Przycisk(red, 915, 780, 370, 45, 'Wstecz')
pole_informacyjne = Blok(white, 915, 400, 370, 300)
wynik = Tekst(1020, 25, white, 60, 'comicsans', 'Wynik:')
kto_ma_zaczynać = Tekst(10, 15, black, 50, 'comicsans', 'Kto ma zacząć rozgrywkę:')
pole_menu = Blok(white, 0, 0, 900, 900)
zaczyna_gracz = Przycisk(black, 10, 70, 250, 45, 'Gracz')
zaczyna_komputer = Przycisk(black, 270, 70, 250, 45, 'Komputer')
zaczyna_losowo = Przycisk(black, 530, 70, 250, 45, 'Losowo')
informacje = Tekst(10, 400, black, 32, "comicsans", 'fff')

def drukuj_wynik(zwycięzca):
    if zwycięzca == 1:
        tekst = Tekst(930, 415, black, 28, 'freesansbold.ttf', 'Wygrał gracz!')
    elif zwycięzca == 2:
        tekst = Tekst(930, 415, black, 28, 'freesansbold.ttf', 'Wygrał komputer!')
    tekst.write(screen)


def redraw(wartosc):
    screen.fill((0, 0, 0))
    kogo_tura().write(screen)
    reset.draw(screen)
    wynik.write(screen)
    wyjście.draw(screen)
    pole_informacyjne.rysuj(screen)
    if wartosc == False:
        plansza_rysuj()
        rysuj_pionek(blue, red)
        menu.draw(screen)
    else:
        pole_menu.rysuj(screen)
        kto_ma_zaczynać.write(screen)
        wstecz.draw(screen)
        zaczyna_gracz.draw(screen)
        zaczyna_komputer.draw(screen)
        zaczyna_losowo.draw(screen)
        informacje.write(screen)

while True:
    pygame.display.update()
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        '''*********** obsluga przycisków *************'''
        if event.type == pygame.MOUSEBUTTONDOWN:
            if reset.isOver(pos):
                plansza = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                ilość = 0
                kogo_ruch = 1
                WYGRANA = False

            if wyjście.isOver(pos):
                pygame.quit()
                sys.exit(0)

            if wartosc == False:
                if menu.isOver(pos):
                    wartosc = True

            elif wartosc == True:
                if zaczyna_gracz.isOver(pos):
                    kogo_ruch = 1
                if zaczyna_komputer.isOver(pos):
                    kogo_ruch = 2
                if zaczyna_losowo.isOver(pos):
                    kogo_ruch = random.randint(1, 2)
                if wstecz.isOver(pos):
                    wartosc = False
        if event.type == pygame.MOUSEMOTION:
            if reset.isOver(pos):
                reset.kolor = red
            else:
                reset.kolor = blue
            if wyjście.isOver(pos):
                wyjście.kolor = red
            else:
                wyjście.kolor = blue
            if menu.isOver(pos):
                menu.kolor = red
            else:
                menu.kolor = blue

            if wartosc == True:
                if wstecz.isOver(pos):
                    wstecz.kolor = white
                else:
                    wstecz.kolor = yellow

                if zaczyna_losowo.isOver(pos):
                    zaczyna_losowo.kolor = red
                else:
                    zaczyna_losowo.kolor = blue

                if zaczyna_komputer.isOver(pos):
                    zaczyna_komputer.kolor = red
                else:
                    zaczyna_komputer.kolor = blue

                if zaczyna_gracz.isOver(pos):
                    zaczyna_gracz.kolor = red
                else:
                    zaczyna_gracz.kolor = blue
        '''*******************************************'''

        if ilość < 6 and wartosc == False: # po postawieniu 6 pionka nie możemy umieścić już więcej
            if WYGRANA == False:
                if kogo_ruch == 1:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:  # jeżeli naciśnięto pierwszy przycisk
                            mouseX, mouseY = event.pos  # rozpakowanie tupli
                            if mouseX <= 900 and mouseY <= 900: # uniemożliwia kliknięcie obszaru poza planszą do gry
                                pole = ((mouseY // 300) * 3) + (mouseX // 300)  # wylicz indeks klikniętego pola
                                kogo_ruch, ilość = postaw_znak(pole, kogo_ruch, ilość)
                elif kogo_ruch == 2:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            mouseX, mouseY = event.pos
                            if mouseX <= 900 and mouseY <= 900:
                                pole = ((mouseY // 300) * 3) + (mouseX // 300)
                                kogo_ruch, ilość = postaw_znak(pole, kogo_ruch, ilość)
                zwycięzca = kto_wygral()
                if zwycięzca != None:
                    WYGRANA = True
        if ilość == 6 and wartosc == False: # zmiana miejsca pionka na planszy
            if WYGRANA == False:
                if kogo_ruch == 1:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            mouseX, mouseY = event.pos
                            if mouseX <= 900 and mouseY <= 900:
                                if pole1 == -1:
                                    pole1 = ((mouseY // 300) * 3) + (mouseX // 300)
                                else:
                                    if ((mouseY // 300) * 3) + (mouseX // 300) != pole1:
                                        pole2 = ((mouseY // 300) * 3) + (mouseX // 300)
                                        kogo_ruch = porusz_znak(pole1, pole2, kogo_ruch)
                                        pole1 = -1
                                    else:
                                        print("To samo pole")
                elif kogo_ruch == 2:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            mouseX, mouseY = event.pos
                            if mouseX <= 900 and mouseY <= 900:
                                if pole1 == -1:
                                    pole1 = ((mouseY // 300) * 3) + (mouseX // 300)
                                else:
                                    if ((mouseY // 300) * 3) + (mouseX // 300) != pole1:
                                        pole2 = ((mouseY // 300) * 3) + (mouseX // 300)
                                        kogo_ruch = porusz_znak(pole1, pole2, kogo_ruch)
                                        pole1 = -1
                                    else:
                                        print("To samo pole")
                zwycięzca = kto_wygral()
                if zwycięzca != None:
                    WYGRANA = True

    redraw(wartosc)

    if WYGRANA:
        drukuj_wynik(zwycięzca)

    pygame.display.flip()
