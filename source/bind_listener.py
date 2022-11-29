# Libs publiques
import pygame
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
        maze = self.game_mngr.get_maze()
        cell = maze[pos[1]][pos[0]]

        # Alt+F4 et autres
        if event.type == pl.QUIT:
            self.game_mngr.stop()

        elif event.type == pl.KEYDOWN:
            #Echap pour quitter
            if event.key == pl.K_ESCAPE:
                self.game_mngr.stop()
            
            #Déplacements
            elif event.key == pl.K_z:
                if cell.walls[0] or pos[1] <= 0:
                    self.mixer.play(const.BASE_WALL_SOUND+"0.wav")
                else:
                    self.char_mngr.move(const.UP)
            elif event.key == pl.K_d:
                if cell.walls[1] or pos[0] >= const.MAP_WIDTH:
                    self.mixer.play(const.BASE_WALL_SOUND+"1.wav")
                else:
                    self.char_mngr.move(const.RIGHT)
            elif event.key == pl.K_s:
                if cell.walls[2] or pos[1] >= const.MAP_HEIGHT:
                    self.mixer.play(const.BASE_WALL_SOUND+"2.wav")
                else:
                    self.char_mngr.move(const.DOWN)
            elif event.key == pl.K_q:
                if cell.walls[3] or pos[0] < 0:
                    self.mixer.play(const.BASE_WALL_SOUND+"3.wav")
                else:
                    self.char_mngr.move(const.LEFT)

            # Aide pour les nuls
            elif event.key == pl.K_r:
                self.game_mngr.ariane()

            # Attaque
            elif event.key == pl.K_UP:
                if(
                    pos[1] > 0 and
                    maze[pos[1]-1][pos[0]].ennemi and
                    not cell.walls[0]
                ):
                    maze[pos[1]-1][pos[0]].ennemi = False
                    pygame.mixer.stop()
                    self.mixer.play(const.BASE_ENNEMY_SOUND+"mort0.wav")
                    self.mixer.play(const.BASE_SWORD_SOUND+"Hit0.wav")
                else :
                    self.mixer.play(const.BASE_SWORD_SOUND+"SwordMiss.wav")

            elif event.key == pl.K_RIGHT:
                if(
                    pos[0] < const.MAP_WIDTH-1 and
                    maze[pos[1]][pos[0]+1].ennemi and
                    not cell.walls[1]
                ):
                    maze[pos[1]][pos[0]+1].ennemi = False
                    pygame.mixer.stop()
                    self.mixer.play(const.BASE_ENNEMY_SOUND+"mort1.wav")
                    self.mixer.play(const.BASE_SWORD_SOUND+"Hit1.wav")
                else :
                    self.mixer.play(const.BASE_SWORD_SOUND+"SwordMiss.wav")

            elif event.key == pl.K_DOWN:
                if(
                    pos[1] < const.MAP_HEIGHT-1 and
                    maze[pos[1]+1][pos[0]].ennemi and
                    not cell.walls[2]
                ):
                    maze[pos[1]+1][pos[0]].ennemi = False
                    pygame.mixer.stop()
                    self.mixer.play(const.BASE_ENNEMY_SOUND+"mort2.wav")
                    self.mixer.play(const.BASE_SWORD_SOUND+"Hit2.wav")
                else :
                    self.mixer.play(const.BASE_SWORD_SOUND+"SwordMiss.wav")

            elif event.key == pl.K_LEFT:
                if(
                    pos[0] > 0 and
                    maze[pos[1]][pos[0]-1].ennemi and
                    not cell.walls[3]
                ):
                    maze[pos[1]][pos[0]-1].ennemi = False
                    pygame.mixer.stop()
                    self.mixer.play(const.BASE_ENNEMY_SOUND+"mort3.wav")
                    self.mixer.play(const.BASE_SWORD_SOUND+"Hit3.wav")
                else :
                    self.mixer.play(const.BASE_SWORD_SOUND+"SwordMiss.wav")
