import pygame
import time as t

from source.const import PATH_SOUNDS

class SoundMixer:
    def __init__(self):
        self.d_sounds: dict[str, pygame.mixer.Sound] = {}

    def play(self, name: str):
        if not name in self.d_sounds:
            self.load(name)
        self.d_sounds[name].play()

    def load(self, name: str):
        if not name in self.d_sounds:
            self.d_sounds[name] = pygame.mixer.Sound(PATH_SOUNDS + name)

    def chain(self, names: list[str]):
        for name in names:
            self.load(name)
        for name in names:
            self.play(name)
            t.sleep(self.d_sounds[name].get_length())

    def stop(self):
        pygame.mixer.stop()
