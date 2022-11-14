import pygame
import pygame.locals as pl
import char_manager

#Initialisation
pygame.init()
pygame.display.set_caption("Pygame Window")
fen = pygame.display.set_mode((1280, 720), pl.FULLSCREEN)

# Chargement des ressources
fond = pygame.image.load("fond.jpg").convert()
perso = pygame.image.load("perso.png").convert_alpha()

perso_mngr = char_manager.CharManager(perso, fen)

fen.blit(fond, (0, 0))
perso_mngr.blit()
pygame.display.flip()

# Lancement du jeu
is_started = True
while(is_started):
    fen.blit(fond, (0, 0, fen.get_width(), fen.get_height()))

    for event in pygame.event.get():
        # Alt+F4 et autres
        if event.type == pl.QUIT:
            is_started = False

        elif event.type == pl.KEYDOWN:
            #Echap pour quitter
            if event.key == pl.K_ESCAPE:
                is_started = False
            
            #Déplacements
            elif event.key == pl.K_z:
                perso_mngr.move(0,-10)
            elif event.key == pl.K_s:
                perso_mngr.move(0, 10)
            elif event.key == pl.K_q:
                perso_mngr.move(-10,0)
            elif event.key == pl.K_d:
                perso_mngr.move( 10,0)

    perso_mngr.blit()
    pygame.display.flip()