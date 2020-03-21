import pygame
import random
LARGHEZZA_FINESTRA = 1000
LUNGHEZZA_FINESTRA = 800

LARGHEZZA_CAMPO = 10
LUNGHEZZA_CAMPO = 10

N_ERBIVORI = 5
N_CARNIVORI= 5
V_ERBIVORI= 1
V_CARNIVORI= 1

class Erbivoro:

    # Il costruttore di una classe, è quella funzione che viene chiamata
    #   quando la classe viene inizializzata
    # Self è un parametro che devi mettere OBBLIGATORIAMENTE per TUTTI i metodi
    #   di una classe, ma che non deve essere passato quando lo chiami.
    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def __str__(self):
        return "Erbivoro @ (%s,%s)" % (str(self.pos_x), str(self.pos_y))

class Carnivoro:
    
    '''
        pos_x
        pos_y
    '''
    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def __str__(self):
        return "Carnivoro @ (%s,%s)" % (str(self.pos_x), str(self.pos_y))


     
if __name__ == '__main__':
    # da qui esegui il programma
    #pygame.init()
    #screen = pygame.display.set_mode((LARGHEZZA_FINESTRA, LUNGHEZZA_FINESTRA))

    ###### INIZIALIZZAZIONE
    erbivori = list()                               # creo la lista di erbivori
    for n in range(N_ERBIVORI):
        x = random.randint(0, LARGHEZZA_CAMPO)      # genero la x casualmente
        y = random.randint(0, LUNGHEZZA_CAMPO)      # genero la y casualmente

        e = Erbivoro(x, y)                          # creo erbivoro
        erbivori.append(e)                          # aggiungo erbivoro alla lista

    for e in erbivori:
        print(e)


    carnivori = list()                               
    for n in range(N_CARNIVORI):
        x = random.randint(0, LARGHEZZA_CAMPO)      
        y = random.randint(0, LUNGHEZZA_CAMPO)     

        e = Carnivoro(x, y)
        carnivori.append(e)                          

    for e in carnivori:
        print(e)

    # devi fare l'inizializzazione dei carnivori


# TO DO LIST
#   prox_volta: eridarietà
