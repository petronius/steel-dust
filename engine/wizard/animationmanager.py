import engine.resources
import engine.settings
from pyglet import clock

class AnimationManager:
    def __init__(self, model):
        self.model = model
        self.state = "idle"
        self.animations = ("walk","cast1","cast2","cast3","idle","die","hit")
        self.expires_in = 0
    
    # Calling this function returns a new animation, and reset the time until the animation
    # manager returns to the "idle" state
    def start_new_anim(self, state):
        self.state = state
        anim, time = self.model.get_anim(self.state)
        if anim == None:
            anim = self.model.get_anim("idle")
        self.expires_in = time
        return anim
        
    def update(self):
        if self.expires_in > 0:
            print(f"FPS is {clock.get_fps()}")
            self.expires_in -= engine.settings.FRAMERATE
        if self.expires_in <= 0:
            self.state = "idle"
