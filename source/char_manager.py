# Libs publiques
import pygame

# Libs locales
import source.const as const
from source.animation_manager import AnimationManager

class CharManager():
    """ A class for managing a character on a pygame surface
    """

    def __init__(self, fen: pygame.surface.Surface):
        # Stockage des arguments
        self._fen = fen
        self._position_perso_unit = const.PLAYER_SPAWN

        # Valeurs par défaut
        self.key = False

        # Animations
        self._frames = {
            "up": [
                pygame.image.load(const.PATH_PERSO+f"up/{i}.png").convert_alpha()
                for i in range(1, 5)
            ],
            #"down": [
                # pygame.image.load(const.PATH_PERSO+f"down/{i}.png").convert_alpha()
                # for i in range(1, 5)
            # ],
            #"left": [
                # pygame.image.load(const.PATH_PERSO+f"left/{i}.png").convert_alpha()
                # for i in range(1, 5)
            # ],
            #"right": [
                # pygame.image.load(const.PATH_PERSO+f"right/{i}.png").convert_alpha()
                # for i in range(1, 5)
            # ],
            "idle": [
                pygame.image.load(const.PATH_PERSO+"perso.png").convert_alpha()
            ]
        }

        self._animations = {}

        for key in self._frames:
            self._animations[key] = AnimationManager(self._frames[key], 5)

        self._current_animation: AnimationManager = self._animations["idle"]

    def move(self, amount: tuple[int, int]):
        self._position_perso_unit = tuple((self._position_perso_unit[0] + amount[0], self._position_perso_unit[1] + amount[1]))

        # TODO: Animation de déplacement

    def get_position(self):
        return self._position_perso_unit
    
    def set_postion(self, coords: tuple[int, int]):
        self._position_perso_unit = coords

    def blit(self):
        h_px_per_unit = self._fen.get_width() / (const.MAP_WIDTH + 2)
        v_px_per_unit = self._fen.get_height() / (const.MAP_HEIGHT + 2)

        editable_perso = self._current_animation.tick()
        editable_perso = pygame.transform.scale(editable_perso, (int(h_px_per_unit*const.PERSO_H_SCALE), int(v_px_per_unit*const.PERSO_V_SCALE)))

        pos_in_pixels = (
            (self._position_perso_unit[0]+1 + (1-const.PERSO_H_SCALE)/2) * h_px_per_unit,
            (self._position_perso_unit[1]+1 + (1-const.PERSO_V_SCALE)/2) * v_px_per_unit
        )

        self._fen.blit(editable_perso, pos_in_pixels)

    def give_key(self):
        self.key = True

    def has_key(self):
        return self.key

    def set_animation(self, animation: str):
        if animation in self._animations:
            self._current_animation = self._animations[animation]
