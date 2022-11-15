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

        self.clock = pygame.time.Clock()

        # Chargement des ressources
        self._fond = pygame.image.load(const.PATH_BACKGROUND).convert()
        self._perso = pygame.image.load(const.PATH_PERSO).convert_alpha()

        self.perso_mngr = char_manager.CharManager(self._perso, self.fen)
        self.bind_mngr = bind_listener.BindManager(self.perso_mngr, self)

        # Création du labyrinthe
        self.maze = maze_gen.maze_gen()

        # Gestion animations
        self.key_animations = []

        for i in range(1, 6):
            self.key_animations.append(pygame.image.load(f"{const.PATH_CLE}{i}.png"))

        self.update()

    def loop(self):
        # Lancement du jeu
        self._is_started = True
        while self._is_started:
            # Gestion des évènements
            for event in pygame.event.get():
                self.bind_mngr.handle(event)
            self.update()
        pygame.quit()

    def update(self):
        # Background
        editable_background = self._fond.copy()
        editable_background = pygame.transform.scale(editable_background, (self.fen.get_width(), self.fen.get_height()))
        self.fen.blit(editable_background, (0, 0))

        # Labyrinthe
        self.draw_maze()

        # Clé
        for actual_frame in range(5):
            self.fen.blit(self.key_animations[actual_frame], (self.fen.get_width() / 2 - 50, self.fen.get_height() / 2 - 50))
            self.clock.tick(30)
            pygame.display.flip()

        # Character
        self.perso_mngr.blit()

        # Display
        pygame.display.flip()

    def draw_maze(self):
        cell: case.Case

        cell_width = self.fen.get_width() / const.MAP_WIDTH
        cell_height = self.fen.get_height() / const.MAP_HEIGHT

        for line in self.maze:
            for cell in line:
                if cell.walls[0]:
                    pygame.draw.line(self.fen, const.COLOR_WALL, (cell.x * cell_width, cell.y * cell_height), ((cell.x + 1) * cell_width, cell.y * cell_height))
                if cell.walls[1]:
                    pygame.draw.line(self.fen, const.COLOR_WALL, ((cell.x + 1) * cell_width-1, cell.y * cell_height), ((cell.x + 1) * cell_width-1, (cell.y + 1) * cell_height))
                if cell.walls[2]:
                    pygame.draw.line(self.fen, const.COLOR_WALL, ((cell.x + 1) * cell_width, (cell.y + 1) * cell_height-1), (cell.x * cell_width, (cell.y + 1) * cell_height-1))
                if cell.walls[3]:
                    pygame.draw.line(self.fen, const.COLOR_WALL, (cell.x * cell_width, (cell.y + 1) * cell_height), (cell.x * cell_width, cell.y * cell_height))
                
    def stop(self):
        self._is_started = False