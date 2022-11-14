# Libs publiques
import pygame
import pygame.locals as pl

# Libs locales
import char_manager
import bind_manager

class GameManager():
    def __init__(self):
        #Initialisation
        pygame.init()
        pygame.display.set_caption("Pygame Window")
        self.fen = pygame.display.set_mode((1280, 720), pl.FULLSCREEN)
        self.is_started = False

        # Chargement des ressources
        self.fond = pygame.image.load("fond.jpg").convert()
        self.perso = pygame.image.load("perso.png").convert_alpha()

        self.perso_mngr = char_manager.CharManager(self.perso, self.fen)
        self.bind_mngr = bind_manager.BindManager(self.perso_mngr, self)

        self.update()

    def loop(self):
        # Lancement du jeu
        self.is_started = True
        while(self.is_started):
            for event in pygame.event.get():
                self.bind_mngr.handle(event)
            self.update()
        pygame.quit()

    def update(self):
        self.fen.blit(self.fond, (0, 0, self.fen.get_width(), self.fen.get_height()))
        self.perso_mngr.blit()
        pygame.display.flip()

    def stop(self):
        self.is_started = False