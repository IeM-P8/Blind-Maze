# Libs publiques
import pygame.locals as pl
import source.const as const

# Libs locales
from source.char_manager import CharManager

class BindManager():
    def __init__(self, char_mngr: CharManager, game_mngr):
        self.char_mngr = char_mngr
        self.game_mngr = game_mngr
    
    def handle(self, event):
        # Préparation des valeurs utiles
        pos = self.char_mngr.get_position()
        cell = self.game_mngr.get_maze()[pos[1]][pos[0]]

        # Alt+F4 et autres
        if event.type == pl.QUIT:
            self.game_mngr.stop()

        elif event.type == pl.KEYDOWN:
            #Echap pour quitter
            if event.key == pl.K_ESCAPE:
                self.game_mngr.stop()
            
            #Déplacements
            elif event.key == pl.K_z:
                if pos[1] > 0 and not cell.walls[0]:
                    self.char_mngr.move(const.UP)
            elif event.key == pl.K_d:
                if pos[0] < const.MAP_WIDTH - 1 and not cell.walls[1]:
                    self.char_mngr.move(const.RIGHT)
            elif event.key == pl.K_s:
                if pos[1] < const.MAP_HEIGHT - 1  and not cell.walls[2]:
                    self.char_mngr.move(const.DOWN)
            elif event.key == pl.K_q:
                if pos[0] > 0 and not cell.walls[3]:
                    self.char_mngr.move(const.LEFT)