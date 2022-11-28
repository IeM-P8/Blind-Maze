# Libs publiques
import pygame

# Libs locales
import source.const as const
from source.animation_manager import AnimationManager
from source.sound_mixer import SoundMixer

class CharManager():
    """ A class for managing a character on a pygame surface
    """

    def __init__(self, fen: pygame.surface.Surface, parent):
        # Stockage des arguments
        self._fen = fen
        self._position_perso_unit = const.PLAYER_SPAWN
        self._parent = parent

        # Valeurs par défaut
        self.key = False
        self._clock = pygame.time.Clock()

        # Animations
        self._frames = {
            "up": [
                pygame.image.load(const.PATH_PERSO+f"up/{i}.png").convert_alpha()
                for i in range(1, 9)
            ],
            "down": [
                pygame.image.load(const.PATH_PERSO+f"down/{i}.png").convert_alpha()
                for i in range(1, 9)
            ],
            "left": [
                pygame.image.load(const.PATH_PERSO+f"left/{i}.png").convert_alpha()
                for i in range(1, 7)
            ],
            "right": [
                pygame.image.load(const.PATH_PERSO+f"right/{i}.png").convert_alpha()
                for i in range(1, 7)
            ],
            "idle": [
                pygame.image.load(const.PATH_PERSO+"perso.png").convert_alpha()
            ]
        }

        self._animations = {}

        for key in self._frames:
            self._animations[key] = AnimationManager(self._frames[key], 4)

        self._current_animation: AnimationManager = self._animations["idle"]

        # Bruit de pas
        self._sound_mixer = SoundMixer()
        self._sound_mixer.load("Footsteps.wav")

    def move(self, direction: tuple[int, int]):
        # On met l'anim correspondante
        if direction == const.DOWN:
            self.set_animation("down")
        elif direction == const.UP:
            self.set_animation("up")
        elif direction == const.LEFT:
            self.set_animation("left")
        elif direction == const.RIGHT:
            self.set_animation("right")

        # On joue le son de pas
        self._sound_mixer.play("Footsteps.wav")

        # On déplace le perso lentement
        for i in range(30):
            self._clock.tick(60)
            self._position_perso_unit = (
                self._position_perso_unit[0] + direction[0] / 30,
                self._position_perso_unit[1] + direction[1] / 30
            )
            self._parent.update()

        # On recentre le perso
        self._position_perso_unit = (
            int(self._position_perso_unit[0]+0.5), # On arrondi la position, pour
            int(self._position_perso_unit[1]+0.5)  # éviter les erreurs d'arrondi
        )

        # On reset l'anim
        self.set_animation("idle")

    def set_animation(self, animation: str):
        if animation in self._animations:
            self._current_animation = self._animations[animation]
        self._current_animation.reset()

    def get_position(self):
        return self._position_perso_unit
    
    def set_position(self, coords: tuple[int, int]):
        self._position_perso_unit = coords

    def blit(self):
        if(
            not const.DEBUG and
            (self._position_perso_unit[0] >= 1 or self._position_perso_unit[1] >= 1) and
            (self._position_perso_unit[0] <= const.MAP_WIDTH-2 or self._position_perso_unit[1] <= const.MAP_HEIGHT-2)
        ):
            return

        h_px_per_unit = self._fen.get_width() / (const.MAP_WIDTH + 2)
        v_px_per_unit = self._fen.get_height() / (const.MAP_HEIGHT + 2)

        editable_perso = self._current_animation.tick()
        editable_perso = pygame.transform.scale(editable_perso, (int(h_px_per_unit*const.PERSO_H_SCALE), int(v_px_per_unit*const.PERSO_V_SCALE)))

        pos_in_pixels = (
            int((self._position_perso_unit[0]+1 + (1-const.PERSO_H_SCALE)/2) * h_px_per_unit),
            int((self._position_perso_unit[1]+1 + (1-const.PERSO_V_SCALE)/2) * v_px_per_unit)
        )

        self._fen.blit(editable_perso, pos_in_pixels)

    def give_key(self):
        self.key = True

    def has_key(self):
        return self.key

    def kill(self):
        self._sound_mixer.play(const.NAME_DEATH_SOUND)
