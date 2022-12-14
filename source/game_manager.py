# Libs publiques
import pygame
import pygame.locals as pl
import time as t

# Libs locales
import source.const as const
import source.char_manager as char_manager
import source.bind_listener as bind_listener
import source.maze_gen as maze_gen
import source.case as case
import source.animation_manager as animate
import source.sound_mixer as sound_mixer

class GameManager():
    def __init__(self):
        #Initialisation
        pygame.init()
        pygame.display.set_caption("Blind Maze")
        self.fen = pygame.display.set_mode(const.RESOLUTION, pl.FULLSCREEN)
        pygame.key.set_repeat(500, 500)
        self._is_started = False

        self._clock = pygame.time.Clock()
        self.sprite_controls = pygame.image.load("ressources/images/commands.png").convert_alpha()
        self.sprite_controls = pygame.transform.scale(self.sprite_controls, (self.fen.get_width()//4, self.fen.get_height()//4))

        # Chargement des ressources
        self._border = pygame.image.load(const.PATH_CADRE).convert_alpha()
        self._door = pygame.image.load(const.PATH_DOOR_CLOSED).convert_alpha()

        # Managers de ressources
        self.perso_mngr = char_manager.CharManager(self.fen, self)
        self.bind_mngr = bind_listener.BindManager(self.perso_mngr, self)
        self.sound_mixer = sound_mixer.SoundMixer()

        self.sound_mixer.load(const.BASE_DOOR_SOUND+"DoorOpening.wav")
        self.sound_mixer.load(const.BASE_DOOR_SOUND+"DoorLocked.wav")
        self.sound_mixer.load("intro.wav")

        # Création du labyrinthe
        self.maze, self.key_cell, self.ennemies = maze_gen.maze_gen()

        # Gestion animations
        # Clé
        key_animations = []
        for i in range(1, 6):
            key_animations.append(pygame.image.load(f"{const.PATH_CLE}{i}.png"))

        self.key_animations = animate.AnimationManager(key_animations, 8)

        # Porte fin
        self.door_frames = []
        for i in range(1, 21):
            self.door_frames.append(pygame.image.load(f"{const.PATH_SORTIE}{i}.png"))

        self.door_animation = animate.AnimationManager(self.door_frames, 9)

        # Intro
        self.intro_frames = []
        for i in range(1, 21):
            self.intro_frames.append(pygame.image.load(f"{const.PATH_INTRO}{i}.png"))

        self.intro_animation = animate.AnimationManager(self.intro_frames, 5)

        # Mort
        self.death_frames = []
        for i in range(1, 22):
            self.death_frames.append(pygame.image.load(f"{const.PATH_DEATH}{i}.png"))

        self.death_animation = animate.AnimationManager(self.death_frames, 9)

    def loop(self):
        self.start_animation()
        # Lancement du jeu
        self._is_started = True
        # TODO: Musique de fond
        while self._is_started:
            self._clock.tick(60)
            
            # Gestion des évènements
            for event in pygame.event.get():
                self.bind_mngr.handle(event)

            # Mise à jour affichage
            self.update()
            
            # Check positions spéciale
            self.check_special_positions()

        # Fin du jeu
        pygame.quit()

    def start_animation(self):
        # Départ
        self.sound_mixer.play("intro.wav")

        for _ in range((len(self.intro_frames)-1) * 5):
            sprite = self.intro_animation.tick()
            full_size = pygame.transform.scale(sprite, (self.fen.get_height(), self.fen.get_height()))

            self.fen.fill((0, 0, 0))
            self.fen.blit(full_size, (self.fen.get_width()/2 - self.fen.get_height()/2, 0))
            pygame.display.flip()
            self._clock.tick(60)

        t.sleep(1)
        self.stop()

    def check_special_positions(self):
        # Ramassage de clé
        if self.perso_mngr.get_position() == (self.key_cell.x, self.key_cell.y) and self.key_cell.key:
            self.key_cell.key = False
            self.perso_mngr.give_key()
            self.sound_mixer.play(const.NAME_KEY_SOUND)

        # Enemis
        for ennemy in self.ennemies:
            if ennemy.ennemi :
                # Mort
                if self.perso_mngr.get_position() == (ennemy.x, ennemy.y) and ennemy.ennemi:
                    self.sound_mixer.play("Footsteps.wav")
                    for frame in range((len(self.death_frames)-1) * 9):
                        sprite = self.death_animation.tick()
                        full_size = pygame.transform.scale(sprite, (self.fen.get_height(), self.fen.get_height()))

                        self.fen.fill((0, 0, 0))
                        self.fen.blit(full_size, (self.fen.get_width()/2 - self.fen.get_height()/2, 0))
                        pygame.display.flip()
                        
                        if frame == 30 or frame == 60:
                            self.sound_mixer.play("Footsteps.wav")
                        elif frame == 150:
                            self.sound_mixer.play(const.NAME_DEATH_SOUND)
                        self._clock.tick(60)

                    self.stop()
                
                # Proche
                elif not pygame.mixer.get_busy():
                    if(
                        self.perso_mngr.get_position() == (ennemy.x + 1, ennemy.y) and
                        not ennemy.walls[1]
                    ):
                        self.sound_mixer.play(const.BASE_ENNEMY_SOUND+"3.wav")

                    elif(
                        self.perso_mngr.get_position() == (ennemy.x - 1, ennemy.y) and
                        not ennemy.walls[3]
                    ):
                        self.sound_mixer.play(const.BASE_ENNEMY_SOUND+"1.wav")

                    elif(
                        self.perso_mngr.get_position() == (ennemy.x, ennemy.y + 1) and
                        not ennemy.walls[2]
                    ):
                        self.sound_mixer.play(const.BASE_ENNEMY_SOUND+"0.wav")

                    elif(
                        self.perso_mngr.get_position() == (ennemy.x, ennemy.y - 1) and
                        not ennemy.walls[0]
                    ):
                        self.sound_mixer.play(const.BASE_ENNEMY_SOUND+"2.wav")
                        
        # Ouverture de porte
        if self.perso_mngr.get_position() == (0, 0) :
            if self.perso_mngr.has_key():
                # Victoire
                self.sound_mixer.play(const.BASE_DOOR_SOUND+"DoorOpening.wav")

                for frame in range(9 * len(self.door_frames)-1):
                    sprite = self.door_animation.tick()
                    full_size = pygame.transform.scale(sprite, (self.fen.get_height(), self.fen.get_height()))

                    self.fen.fill((0, 0, 0))
                    self.fen.blit(full_size, (self.fen.get_width()/2 - self.fen.get_height()/2, 0))
                    pygame.display.flip()

                    if frame in [20, 40, 60, 80, 100, 120]:
                        self.sound_mixer.play("Footsteps.wav")
                    self._clock.tick(40)

                t.sleep(2)
                self.stop()
            elif not pygame.mixer.get_busy():
                # Porte fermée
                self.sound_mixer.play(const.BASE_DOOR_SOUND+"DoorLocked.wav")

    def update(self):
        self.fen.fill((0, 0, 0))

        # TODO: Fond de map

        # Dessin du cadre
        h_px_per_unit = self.fen.get_width() // (const.MAP_WIDTH + 2)
        v_px_per_unit = self.fen.get_height() // (const.MAP_HEIGHT + 2)

        resized = pygame.transform.scale(self._border, (h_px_per_unit,v_px_per_unit ))
        rotated = pygame.transform.rotate(resized, 180)

        for i in range(const.MAP_WIDTH):
            self.fen.blit(rotated, (h_px_per_unit * (i + 1), 0))
            self.fen.blit(resized, (h_px_per_unit * (i + 1), v_px_per_unit * (const.MAP_HEIGHT + 1)))

        # Labyrinthe
        if const.DEBUG:
            self.draw_maze()

        # Halo début de map
        halo = pygame.image.load(const.PATH_CLE+"halo.png").convert_alpha()
        halo = pygame.transform.scale(halo, (h_px_per_unit, v_px_per_unit))
        self.fen.blit(halo, (const.MAP_WIDTH * h_px_per_unit, const.MAP_HEIGHT * v_px_per_unit))

        # Clé
        if self.key_cell.key:
            self.draw_key()
        
        # Porte
        self.fen.blit(self._door, (h_px_per_unit, v_px_per_unit))

        # Character
        self.perso_mngr.blit()

        # Contrôles
        self.draw_controls()

        # Affichage debug
        if const.DEBUG:
            ennemy: case.Case
            for ennemy in self.ennemies:
                if ennemy.ennemi:
                    pygame.draw.rect(self.fen, (255, 0, 255), ((ennemy.x+1) * h_px_per_unit +8, (ennemy.y+1) * v_px_per_unit +5, h_px_per_unit-10, v_px_per_unit-10))

        # Display
        pygame.display.flip()

    def draw_maze(self):
        cell: case.Case

        cell_width = self.fen.get_width() / (const.MAP_WIDTH + 2) # +2 pour le décors
        cell_height = self.fen.get_height() / (const.MAP_HEIGHT + 2)

        for line in self.maze:
            for cell in line:
                cell_origin = (
                    (cell.x + 1) * cell_width,
                    (cell.y + 1) * cell_height
                )

                if cell.walls[0]:
                    pygame.draw.line(
                        self.fen, const.COLOR_WALL,
                        cell_origin,
                        (cell_origin[0] + cell_width, cell_origin[1])
                    )

                if cell.walls[1]:
                    pygame.draw.line(
                        self.fen, const.COLOR_WALL,
                        (cell_origin[0] + cell_width, cell_origin[1]),
                        (cell_origin[0] + cell_width, cell_origin[1] + cell_height)
                    )

                if cell.walls[2]:
                    pygame.draw.line(
                        self.fen, const.COLOR_WALL,
                        (cell_origin[0] + cell_width, cell_origin[1] + cell_height),
                        (cell_origin[0], cell_origin[1] + cell_height)
                    )

                if cell.walls[3]:
                    pygame.draw.line(
                        self.fen, const.COLOR_WALL,
                        (cell_origin[0], cell_origin[1] + cell_height),
                        cell_origin
                    )

    def draw_key(self):
        # Tous ces calculs servent à centrer la clé sur la case
        sprite: pygame.surface.Surface = self.key_animations.tick()
        halo: pygame.surface.Surface = pygame.image.load(const.PATH_CLE+"halo.png")

        h_px_per_unit = self.fen.get_width() / (const.MAP_WIDTH + 2)
        v_px_per_unit = self.fen.get_height() / (const.MAP_HEIGHT + 2)

        key_x_in_cell = h_px_per_unit / 2 - sprite.get_width() / 2
        key_y_in_cell = v_px_per_unit / 2 - sprite.get_height() / 2

        cell_x = (self.key_cell.x + 1) * h_px_per_unit
        cell_y = (self.key_cell.y + 1) * v_px_per_unit

        x_cle = cell_x + key_x_in_cell
        y_cle = cell_y + key_y_in_cell

        x_halo = cell_x + h_px_per_unit / 1.5 - halo.get_width() / 2
        y_halo = cell_y + v_px_per_unit*1.25 - halo.get_height() / 2

        halo = pygame.transform.scale(halo, (2*h_px_per_unit, 2*v_px_per_unit))
        self.fen.blit(halo, (x_halo, y_halo))
        self.fen.blit(sprite, (x_cle, y_cle))

    def draw_controls(self):
        self.fen.blit(self.sprite_controls, (self.fen.get_width() - self.sprite_controls.get_width(), 0))

    def ariane(self):
        self.perso_mngr.set_position((const.MAP_WIDTH - 1, const.MAP_HEIGHT - 1))

    def get_maze(self):
        return [line[:] for line in self.maze]

    def stop(self):
        self._is_started = False
