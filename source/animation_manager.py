import pygame

class AnimationManager():
    def __init__(self, sprites: list[pygame.surface.Surface], sprite_duration: int):
        self.sprites = sprites
        self.sprite_duration = sprite_duration
        self.current_sprite = 0
        self.current_sprite_duration = 0

    def tick(self):
        self.current_sprite_duration += 1
        if self.current_sprite_duration >= self.sprite_duration:
            self.current_sprite_duration = 0
            self.current_sprite += 1
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
        
        return self.sprites[self.current_sprite]

    def reset(self):
        self.current_sprite = 0
        self.current_sprite_duration = 0
