import pygame
from pygame.locals import Rect

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
        h_px_per_unit = self._fen.get_width() / 10
        v_px_per_unit = self._fen.get_height() / 10

        pos_in_pixels = (self._position_perso_unit[0] * h_px_per_unit, self._position_perso_unit[1] * v_px_per_unit)
        self._fen.blit(self._perso, (*pos_in_pixels, self._fen.get_width(), self._fen.get_height()))

        return self