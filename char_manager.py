# Libs publiques
import pygame
from pygame.locals import Rect

# Libs locales
import const

class CharManager():
    """ A class for managing a character on a pygame surface
    """

    def __init__(self, perso: pygame.surface.Surface, fen: pygame.surface.Surface):
        self._perso = perso
        self._fen = fen
        self._position_perso_unit = (0,0)

    def set_perso(self, perso: pygame.surface.Surface):
        self._perso = perso

        return self

    def move(self, amount: tuple[int, int]):
        self._position_perso_unit = tuple((self._position_perso_unit[0] + amount[0], self._position_perso_unit[1] + amount[1]))

        return self

    def get_position(self):
        return self._position_perso_unit
    
    def set_postion(self, coords: tuple[int, int]):
        self._position_perso_unit = coords

        return self

    def blit(self):
        h_px_per_unit = self._fen.get_width() / const.MAP_WIDTH
        v_px_per_unit = self._fen.get_height() / const.MAP_HEIGHT

        editable_perso = self._perso.copy()
        editable_perso = pygame.transform.scale(editable_perso, (int(h_px_per_unit*const.PERSO_H_SCALE), int(v_px_per_unit*const.PERSO_V_SCALE)))

        pos_in_pixels = ((self._position_perso_unit[0] + (1-const.PERSO_H_SCALE)/2) * h_px_per_unit, (self._position_perso_unit[1] + (1-const.PERSO_V_SCALE)/2) * v_px_per_unit)

        self._fen.blit(editable_perso, pos_in_pixels)

        return self