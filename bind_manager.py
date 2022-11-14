# Libs publiques
import pygame.locals as pl
import const

# Libs locales
from char_manager import CharManager

class BindManager():
    def __init__(self, char_mngr: CharManager, game_mngr):
        self.char_mngr = char_mngr
        self.game_mngr = game_mngr
    
    def handle(self, event):
        # Alt+F4 et autres
        if event.type == pl.QUIT:
            self.game_mngr.stop()

        elif event.type == pl.KEYDOWN:
            #Echap pour quitter
            if event.key == pl.K_ESCAPE:
                self.game_mngr.stop()
            
            #Déplacements
            elif event.key == pl.K_z:
                self.char_mngr.move(const.UP)
            elif event.key == pl.K_s:
                self.char_mngr.move(const.DOWN)
            elif event.key == pl.K_q:
                self.char_mngr.move(const.LEFT)
            elif event.key == pl.K_d:
                self.char_mngr.move(const.RIGHT)