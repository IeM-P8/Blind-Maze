class AnimationManager():
    def __init__(self, animations):
        self.animations = animations
        self.current_animation = None
        self.current_frame = 0
        self.frame_ticks = 0

    def update(self, ticks):
        if self.current_animation is not None:
            self.frame_ticks += ticks
            if self.frame_ticks > self.current_animation.frame_duration:
                self.frame_ticks = 0
                self.current_frame += 1
                if self.current_frame >= len(self.current_animation.frames):
                    self.current_frame = 0

    def play(self, animation_name):
        if self.current_animation is None or self.current_animation.name != animation_name:
            self.current_animation = self.animations[animation_name]
            self.current_frame = 0
            self.frame_ticks = 0

    def get_current_frame(self):
        if self.current_animation is not None:
            return self.current_animation.frames[self.current_frame]
        else:
            return None