import pygame
from pygame.locals import Rect

class CharManager():
    """ A class for managing a character on a pygame surface
    """
    _perso: pygame.surface.Surface
    _fen: pygame.surface.Surface
    _position_perso: Rect

    def __init__(self, perso: pygame.surface.Surface, fen: pygame.surface.Surface):
        self._perso = perso
        self._fen = fen
        self._position_perso = Rect(600,300, perso.get_width(), perso.get_height())

    def set_perso(self, perso: pygame.surface.Surface):
        self._perso = perso

    def move(self, x, y):
        self._position_perso = self._position_perso.move(x, y)

    def get_position(self):
        return self._position_perso
    
    def set_postion(self, x, y):
        self._position_perso = Rect(x, y, self._perso.get_width(), self._perso.get_height())

    def blit(self):
        self._fen.blit(self._perso, self._position_perso)