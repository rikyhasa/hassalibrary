import pygame
from pygame.locals import *
import random
import math

#lista.append(n)
#del paesi[2]
#paesi.index('roma')) #<------ti dice in che posto è
#min(lista)

###############inizializzazione
pygame.init()
screen = pygame.display.set_mode((800, 600))

clk = pygame.time.Clock()
fps = 30


##############classi
class erbivoro:
    """
    pos_x
    pos_y
    vel_x
    vel_y
    """
class carnivoro:
    """
    pos_x
    pos_y
    vel_x
    vel_y
    """


#############quantità di personaggi
n_cavaliere = 6
n_mago = 6


#############velocità
vel = [2, 2.5]

###############sfondo
##surf_back = pygame.image.load("Backgrounds/desert_02.jpg").convert()
##surf_back = pygame.transform.smoothscale(surf_back, (800, 600))
##screen.blit(surf_back, (0, 0))
sfondo = pygame.image.load("Grass.jpg")
# ricalca una sup. piccola(mattonella) su una grande
def tile_surface(surf_little, surf_big):       # surf_little e' la mattonella, surf_big l'area da ricoprire
    w_little = surf_little.get_width()         # prende la larghezza della mattonella
    h_little = surf_little.get_height()        # prende la altezza della mattonella
    w_big = surf_big.get_width()               # larghezza da ricoprire
    h_big = surf_big.get_height()              # altezza da ricoprire
    for y in range(0, h_big, h_little):        # incremento della y
        for x in range(0, w_big, w_little):    # incremento della x
            surf_big.blit(surf_little, (x, y)) # posizionia la mattonella sulle coordinate (x, y)

#########game over
game_over_surf = pygame.image.load("gameover2.png")
game_over_rect = game_over_surf.get_rect()
game_over_rect.center = ( 400, 300 )

###########spown maghi
lista_mago = []
lista_mago_rect = []
lista_mago_surface = []
i = 0
while i<n_mago:
    mago = erbivoro()
    mago.pos_x = random.randint(0,800)
    mago.pos_y = random.randint(0,600) 
    mago.vel_x = vel[0]
    mago.vel_y = vel[0]
    
    immage_mago = pygame.image.load("human_mage.png")
    rect_mago = immage_mago.get_rect()
    rect_mago.center = ( mago.pos_x, mago.pos_y )
    screen.blit(immage_mago, rect_mago)

    lista_mago.append(mago)
    lista_mago_rect.append( rect_mago )
    lista_mago_surface.append( immage_mago )
    
    i += 1

    pygame.display.flip()
##############spown cavaliere
lista_cavaliere = []
lista_cavaliere_rect = []
lista_cavaliere_surface = []
cont = 0
while cont<n_cavaliere:
    cavaliere = carnivoro()
    cavaliere.pos_x = random.randint(0,800)
    cavaliere.pos_y = random.randint(0,600)
    cavaliere.vel_x = vel[1]
    cavaliere.vel_y = vel[1]
    
    immage_cavaliere = pygame.image.load("human_warrior.png")
    rect_cavaliere = immage_cavaliere.get_rect()
    rect_cavaliere.center = ( cavaliere.pos_x, cavaliere.pos_y )
    screen.blit(immage_cavaliere, rect_cavaliere)
    
    lista_cavaliere.append( cavaliere )
    lista_cavaliere_rect.append( rect_cavaliere )
    lista_cavaliere_surface.append( immage_cavaliere )
    
    cont += 1
                                    
    pygame.display.flip()


###################def distanze
def distanze( elemento, lista ):

    #######controllo
    if len(lista_mago_surface)<=0:
        return 
    else:
        pass
    
    lista_dist = []
    i = 0
    while i<len(lista):
        dx = abs(elemento.pos_x - lista[i].pos_x)
        dy = abs(elemento.pos_y - lista[i].pos_y)
        if dx>400 and dy>300:
            Dx = 800-dx
            Dy = 600-dy
            dist = math.sqrt((Dx)**2+(Dy)**2)
    
        elif dx>400 and dy<300:
            Dx = 800-dx
            Dy = dy
            dist = math.sqrt((Dx)**2+(Dy)**2)
           
        elif dx<400 and dy>300:
            Dx = dx
            Dy = 600-dy
            dist = math.sqrt((Dx)**2+(Dy)**2)
    
        elif dx<400 and dy<300:
            dist = math.sqrt((dx)**2+(dy)**2)

        lista_dist.append(dist)
        i = i+1
    dist_min = min( lista_dist )  #la dist minore
    posiz_vicino = lista_dist.index(dist_min) #posiz. nella lista della dist min
    bersaglio = lista[posiz_vicino]
    lista_cose_importanti = [bersaglio,dist_min,posiz_vicino]
##    print ( 'lista_distanze:',lista_dist )
##    print ( 'posiz_vicino:',posiz_vicino )
##    print ( 'bersaglio',bersaglio )
##    print ( lista_cose_importanti )
##    print ( '' )
##    print ( '' )
    return lista_cose_importanti

##a = distanze(lista_mago[0],lista_cavaliere)               #<---queste 2 righe non servono ma aiutano a capire
##print ( '' )
##print ( '' )
##b = distanze(lista_mago[1],lista_cavaliere)
##print ( '' )
##print ( '' )
##c = distanze(lista_mago[2],lista_cavaliere)
##print ( '' )
##print ( '' )
##d = distanze(lista_mago[3],lista_cavaliere)
##print ( '' )
##print ( '' )
##e = distanze(lista_mago[4],lista_cavaliere)
##print ( '' )
##print ( '' )
##f = distanze(lista_cavaliere[0],lista_mago)
##print ( '' )
##print ( '' )
##g = distanze(lista_cavaliere[1],lista_mago)


########################def velocà mago
def velocità_mago( bersaglio,elemento,dist ):

    #######controllo
    if len(lista_mago_surface)<=0:
        return 
    else:
        pass
    
    dx = elemento.pos_x-bersaglio.pos_x
    dy = elemento.pos_y-bersaglio.pos_y
    #print ( 'dx/dy erbivoro',dx,dy )
    #vel x
    if dx<400 and dx>-400:
        vel_mago_x = elemento.vel_x*(dx/dist)
    if dx>=400:
        dx = -800+dx
        vel_mago_x = elemento.vel_x*(dx/dist)
    if dx<-400:
        dx = 800+dx 
        vel_mago_x = elemento.vel_x*(dx/dist)

    #vel y
    if dy<300 and dy>-300:
        vel_mago_y = elemento.vel_y*(dy/dist)
    if dy>=300:
        dy = -600+dy
        vel_mago_y = elemento.vel_y*(dy/dist)
    if dy<-300:
        dy = 600+dy
        vel_mago_y = elemento.vel_y*(dy/dist)
    lista_vel_mago = [vel_mago_x,vel_mago_y]
    #print ( 'dx/dy erbivoro',dx,dy )
    #print ( '' )
    #print ('lista_vel_mago',lista_vel_mago)
    return lista_vel_mago
#######################def velocità cavalieri
def velocità_cavaliere( bersaglio,elemento,dist ):

    #######controllo
    if len(lista_mago_surface)<=0:
        return 
    else:
        pass
    
    dx = elemento.pos_x-bersaglio.pos_x
    dy = elemento.pos_y-bersaglio.pos_y
    #print ( 'dx/dy carnivoro',dx,dy )
    #vel x
    if dx<400 and dx>-400:
        vel_carniv_x = elemento.vel_x*(dx/dist)*(-1)
    if dx>=400:
        dx = -800+dx
        vel_carniv_x = elemento.vel_x*(dx/dist)*(-1)
    if dx<-400:
        dx = 800+dx 
        vel_carniv_x = elemento.vel_x*(dx/dist)*(-1)

    #vel y
    if dy<300 and dy>-300:
        vel_carniv_y = elemento.vel_y*(dy/dist)*(-1)
    if dy>=300:
        dy = -600+dy
        vel_carniv_y = elemento.vel_y*(dy/dist)*(-1)
    if dy<-300:
        dy = 600+dy
        vel_carniv_y = elemento.vel_y*(dy/dist)*(-1)
    lista_vel_carniv = [vel_carniv_x,vel_carniv_y]
    #print ( 'dx/dy carnivoro',dx,dy )
    #print ( '' )
    #print ('lista_vel_carniv',lista_vel_carniv)
    return lista_vel_carniv


########################def blit cavalieri
def blittiamo_cavaliere(lista1, lista2):
    i = 0
    while i<len(lista1):
        screen.blit(lista1[i], lista2[i])
        i += 1
########################def blit mago
def blittiamo_mago(lista1, lista2):
    i = 0
    while i<len(lista1):
        screen.blit(lista1[i], lista2[i])
        i += 1      


##############ciclo princ.
done = False
while not done:
    # sottociclo degli eventi
    for ev in pygame.event.get():
        if ev.type == QUIT:
            done = True

    #########sottociclo distanze e movimento
    ####mago
    i = 0
    while i<len(lista_mago):

        #######controllo
        if len(lista_mago_surface)<=0:
            break
        else:
            pass
        
        bersaglio_e_dist_min = distanze(lista_mago[i],lista_cavaliere)
        lista_vel = velocità_mago( bersaglio_e_dist_min[0],lista_mago[i],bersaglio_e_dist_min[1] )
        lista_mago[i].pos_x += lista_vel[0]
        lista_mago[i].pos_y += lista_vel[1]
        lista_mago_rect[i].centerx = lista_mago[i].pos_x
        lista_mago_rect[i].centery = lista_mago[i].pos_y

        #print ( 'mago',lista_mago_rect[i].centerx,lista_mago_rect[i].centery )
        #print ( 'vel',lista_vel[0],lista_vel[1] )

        i += 1
    ####cavaliere

    i = 0
    while i<len(lista_cavaliere):
        
        #######controllo
        if len(lista_mago_surface)<=0:
            break 
        else:
            pass
        
        bersaglio_e_dist_min = distanze(lista_cavaliere[i],lista_mago)
        lista_vel = velocità_cavaliere( bersaglio_e_dist_min[0],lista_cavaliere[i],bersaglio_e_dist_min[1] )
        lista_cavaliere[i].pos_x += lista_vel[0]
        lista_cavaliere[i].pos_y += lista_vel[1]
        lista_cavaliere_rect[i].centerx = lista_cavaliere[i].pos_x
        lista_cavaliere_rect[i].centery = lista_cavaliere[i].pos_y

        #print ( 'cav',lista_cavaliere_rect[i].centerx,lista_cavaliere_rect[i].centery )
        #print ( 'vel',lista_vel[0],lista_vel[1] )
        
        i += 1

    ###########collisioni
    i = 0
    while i < len(lista_cavaliere_rect):

        ######controllo
        if len(lista_mago_surface)<=0:
            done = True
            break
        else:
            pass
        
        bersaglio_distanza_index = distanze(lista_cavaliere[i],lista_mago)
        if bersaglio_distanza_index[1] < 1.5:
            print ( 'PRESO' )
            del lista_mago[bersaglio_distanza_index[2]]
            del lista_mago_rect[bersaglio_distanza_index[2]]
            del lista_mago_surface[bersaglio_distanza_index[2]]
        else:
            pass
        i += 1
    
    ##########mondo infinito
    ####mago ------------- screen.get_width()-------screen.get_height()
    i = 0
    while i<len(lista_mago_rect):
        #print ( 'mago',lista_mago_rect[i].centerx,lista_mago_rect[i].centery )
        if lista_mago_rect[i].centerx > screen.get_width():
            lista_mago_rect[i].centerx -= screen.get_width()
        if lista_mago_rect[i].centery > screen.get_height():
            lista_mago_rect[i].centery -= screen.get_height()
        if lista_mago_rect[i].centerx < 0:
            lista_mago_rect[i].centerx += screen.get_width()
        if lista_mago_rect[i].centery < 0:
            lista_mago_rect[i].centery += screen.get_height()
        i += 1
    ####cavaliere
    i = 0
    while i<len(lista_cavaliere_rect):
        #print ( 'cav',lista_cavaliere_rect[i].centerx,lista_cavaliere_rect[i].centery )
        if lista_cavaliere_rect[i].centerx > screen.get_width():
            lista_cavaliere_rect[i].centerx -= screen.get_width()
        if lista_cavaliere_rect[i].centery > screen.get_height():
            lista_cavaliere_rect[i].centery -= screen.get_height()
        if lista_cavaliere_rect[i].centerx < 0:
            lista_cavaliere_rect[i].centerx += screen.get_width()
        if lista_cavaliere_rect[i].centery < 0:
            lista_cavaliere_rect[i].centery += screen.get_height()
        i += 1

    
    #schermo
    tile_surface(sfondo,screen)
    #blitto cavaliere e maghi
    blittiamo_cavaliere(lista_cavaliere_surface, lista_cavaliere_rect)
    blittiamo_mago(lista_mago_surface, lista_mago_rect)
    #temporizzo
    clk.tick(fps)
    #aggiorno schermo
    pygame.display.flip()

#########ciclo secondario
done = False
while not done:
    # sottociclo degli eventi
    for ev in pygame.event.get():
        if ev.type == QUIT:
            done = True

    tile_surface(sfondo,screen)
    screen.blit(game_over_surf,game_over_rect)
    clk.tick(fps)
    pygame.display.flip()

pygame.quit()










