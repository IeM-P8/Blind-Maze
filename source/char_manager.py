# Libs publiques
import pygame

# Libs locales
import source.const as const

class CharManager():
    """ A class for managing a character on a pygame surface
    """

    def __init__(self, perso: pygame.surface.Surface, fen: pygame.surface.Surface):
        # Stockage des arguments
        self._perso = perso
        self._fen = fen
        self._position_perso_unit = const.PLAYER_SPAWN

        # Valeurs par défaut
        self.key = False

    def move(self, amount: tuple[int, int]):
        self._position_perso_unit = tuple((self._position_perso_unit[0] + amount[0], self._position_perso_unit[1] + amount[1]))

    def get_position(self):
        return self._position_perso_unit
    
    def set_postion(self, coords: tuple[int, int]):
        self._position_perso_unit = coords

    def blit(self):
        h_px_per_unit = self._fen.get_width() / (const.MAP_WIDTH + 2)
        v_px_per_unit = self._fen.get_height() / (const.MAP_HEIGHT + 2)

        editable_perso = self._perso.copy()
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