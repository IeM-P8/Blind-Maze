# Libs publiques
import pygame.locals as pl

# Libs locales
import source.const as const
from source.char_manager import CharManager
from source.sound_mixer import SoundMixer

class BindManager():
    def __init__(self, char_mngr: CharManager, game_mngr):
        self.char_mngr = char_mngr
        self.game_mngr = game_mngr

        self.mixer = SoundMixer()
        
        for i in range(4):
            self.mixer.load(const.BASE_WALL_SOUND+f"{i}.wav")
    
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
            # TODO: Bruits de pas
            # TODO: Bruits de collision
            elif event.key == pl.K_z and pos[1] > 0:
                if cell.walls[0]:
                    self.mixer.play(const.BASE_WALL_SOUND+"0.wav")
                else:
                    self.char_mngr.move(const.UP)
            elif event.key == pl.K_d and pos[0] < const.MAP_WIDTH-1:
                if cell.walls[1]:
                    self.mixer.play(const.BASE_WALL_SOUND+"1.wav")
                else:
                    self.char_mngr.move(const.RIGHT)
            elif event.key == pl.K_s and pos[1] < const.MAP_HEIGHT-1:
                if cell.walls[2]:
                    self.mixer.play(const.BASE_WALL_SOUND+"2.wav")
                else:
                    self.char_mngr.move(const.DOWN)
            elif event.key == pl.K_q and pos[0] > 0:
                if cell.walls[3]:
                    self.mixer.play(const.BASE_WALL_SOUND+"3.wav")
                else:
                    self.char_mngr.move(const.LEFT)