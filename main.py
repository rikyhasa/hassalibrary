import pygame
import random
import time
LARGHEZZA_FINESTRA = 1000
LUNGHEZZA_FINESTRA = 800

LARGHEZZA_CAMPO = LARGHEZZA_FINESTRA
LUNGHEZZA_CAMPO = LUNGHEZZA_FINESTRA

N_ERBIVORI = 5
N_CARNIVORI= 5
V_ERBIVORI= 1
V_CARNIVORI= 1

FPS = 30

MAGE_ICON_URL = "human_mage.png"
WARRIOR_ICON_URL = "human_warrior.png"

class Erbivoro:

    # Il costruttore di una classe, è quella funzione che viene chiamata
    #   quando la classe viene inizializzata
    # Self è un parametro che devi mettere OBBLIGATORIAMENTE per TUTTI i metodi
    #   di una classe, ma che non deve essere passato quando lo chiami.
    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.rect = None

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

def visualizza_personaggio(url, personaggio):
    image = pygame.image.load(url)
    rect = image.get_rect()
    rect.center = (personaggio.pos_x, personaggio.pos_y)
    personaggio.rect = rect
    screen.blit(image, rect)

def muovi(personaggio):
    rect = personaggio.rect
    personaggio.pos_x = personaggio.pos_x + 1
    personaggio.pos_y = personaggio.pos_y
    rect.right = rect.right + 10
    pygame.display.flip()

# IL PROGRAMMA INIZIA AD ESEGUIRE DA QUI     
if __name__ == '__main__':

    pygame.init()
    screen = pygame.display.set_mode((LARGHEZZA_FINESTRA, LUNGHEZZA_FINESTRA))
    screen.fill((0, 50, 0))
    clk = pygame.time.Clock()

    ###### INIZIALIZZAZIONE
    erbivori = list()                               # creo la lista di erbivori
    for n in range(N_ERBIVORI):
        x = random.randint(0, LARGHEZZA_CAMPO)      # genero la x casualmente
        y = random.randint(0, LUNGHEZZA_CAMPO)      # genero la y casualmente

        e = Erbivoro(x, y)                          # creo erbivoro
        erbivori.append(e)                          # aggiungo erbivoro alla lista

    for erbivoro in erbivori:
        print(erbivoro)
        visualizza_personaggio(MAGE_ICON_URL, erbivoro)

    carnivori = list()                               
    for n in range(N_CARNIVORI):
        x = random.randint(0, LARGHEZZA_CAMPO)      
        y = random.randint(0, LUNGHEZZA_CAMPO)     

        e = Carnivoro(x, y)
        carnivori.append(e)                          

    for carnivoro in carnivori:
        print(carnivoro)
        visualizza_personaggio(WARRIOR_ICON_URL, carnivoro)

    running = True
    while running:                                  # ciclo infinito
        muovi(erbivori[3])
        for event in pygame.event.get():            # prendo gli eventi
            
            if event.type == pygame.QUIT:           # controllo che l'evento sia un qit
                running = False                     # So the user can close the program
                
        #screen.fill(0,0,0) # This fills the screen with black colour.
        pygame.display.flip() # This "flips" the display so that it shows something
    pygame.quit()
    

    

    
