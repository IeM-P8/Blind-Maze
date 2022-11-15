# Libs publiques
import pygame
import pygame.locals as pl

# Libs locales
import source.const as const
import source.char_manager as char_manager
import source.bind_listener as bind_listener
import source.maze_gen as maze_gen
import source.case as case

class GameManager():
    def __init__(self):
        #Initialisation
        pygame.init()
        pygame.display.set_caption("Pygame Window")
        self.fen = pygame.display.set_mode(const.RESOLUTION, pl.FULLSCREEN)
        pygame.key.set_repeat(500, 500)
        self._is_started = False

        # Chargement des ressources
        self._fond = pygame.image.load(const.PATH_BACKGROUND).convert()
        self._perso = pygame.image.load(const.PATH_PERSO).convert_alpha()

        self.perso_mngr = char_manager.CharManager(self._perso, self.fen)
        self.bind_mngr = bind_listener.BindManager(self.perso_mngr, self)

        self.update()

    def loop(self):
        # Lancement du jeu
        self._is_started = True
        while(self._is_started):
            for event in pygame.event.get():
                self.bind_mngr.handle(event)
            self.update()
        pygame.quit()

    def update(self):
        # Background
        editable_background = self._fond.copy()
        editable_background = pygame.transform.scale(editable_background, (self.fen.get_width(), self.fen.get_height()))
        self.fen.blit(editable_background, (0, 0))

        # Character
        self.perso_mngr.blit()

        # Display
        pygame.display.flip()

    def stop(self):
        self._is_started = False