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
    # TODO: Détection idle
    def __init__(self):
        #Initialisation
        pygame.init()
        pygame.display.set_caption("Pygame Window")
        self.fen = pygame.display.set_mode(const.RESOLUTION, pl.FULLSCREEN)
        pygame.key.set_repeat(500, 500)
        self._is_started = False

        self.clock = pygame.time.Clock()

        # Chargement des ressources
        self._fond = pygame.image.load(const.PATH_BACKGROUND).convert()

        # Managers de ressources
        self.perso_mngr = char_manager.CharManager(self.fen)
        self.bind_mngr = bind_listener.BindManager(self.perso_mngr, self)
        self.sound_mixer = sound_mixer.SoundMixer()

        self.sound_mixer.load(const.BASE_OPEN_SOUND+"DoorOpening.wav")

        # Création du labyrinthe
        self.maze, self.key_cell = maze_gen.maze_gen()

        # Gestion animations
        key_animations = []

        for i in range(1, 6):
            key_animations.append(pygame.image.load(f"{const.PATH_CLE}{i}.png"))

        self.key_animations = animate.AnimationManager(key_animations, 8)

    def loop(self):
        # Lancement du jeu
        self._is_started = True
        # TODO: Animation début
        # TODO: Musique de fond
        while self._is_started:
            # Gestion des évènements
            for event in pygame.event.get():
                self.bind_mngr.handle(event)
            
            # Check positions spéciale
            self.check_special_positions()

            # Mise à jour affichage
            self.update()
            self.clock.tick(60)

        # Fin du jeu
        # TODO: Animation fin
        self.sound_mixer.chain([const.BASE_OPEN_SOUND+"DoorOpening.wav"])
        pygame.quit()

    def check_special_positions(self):
        # Ramassage de clé
        if self.perso_mngr.get_position() == (self.key_cell.x, self.key_cell.y):
            self.key_cell.key = False
            self.perso_mngr.give_key()
            self.sound_mixer.play(const.NAME_KEY_SOUND)

        # Ouverture de porte
        # TODO: Vraie gestion de porte
        # TODO: Vraie gestion de victoire
        if self.perso_mngr.get_position() == (0, 0) and self.perso_mngr.has_key():
            print("Gagné !")
            self.stop()

    def update(self):
        # # Background
        # editable_background = self._fond.copy()
        # editable_background = pygame.transform.scale(editable_background, (self.fen.get_width(), self.fen.get_height()))
        # self.fen.blit(editable_background, (0, 0))
        self.fen.fill((0, 0, 0))

        # Labyrinthe
        self.draw_maze()

        # Character
        self.perso_mngr.blit()

        # Clé
        # TODO: Aura de la clé
        if self.key_cell.key:
            self.draw_key()

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

        h_px_per_unit = self.fen.get_width() / (const.MAP_WIDTH + 2)
        v_px_per_unit = self.fen.get_height() / (const.MAP_HEIGHT + 2)

        key_x_in_cell = h_px_per_unit / 2 - sprite.get_width() / 2
        key_y_in_cell = v_px_per_unit / 2 - sprite.get_height() / 2

        x_cle = (self.key_cell.x + 1) * h_px_per_unit + key_x_in_cell
        y_cle = (self.key_cell.y + 1) * v_px_per_unit + key_y_in_cell

        self.fen.blit(sprite, (x_cle, y_cle))

    def get_maze(self):
        return [line[:] for line in self.maze]

    def stop(self):
        self._is_started = False
