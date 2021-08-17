from pyglet import clock
from PodSixNet.Connection import connection

import engine.resources
import engine.settings


class AnimationManager:

    def __init__(self, wizard, model):
        self.wizard = wizard
        self.model = model
        self.state = "idle"
        self.animations = ("walk", "cast1", "cast2", "cast3", "idle", "die", "hit")
        self.expires_in = 0

    # Calling this function returns a new animation, and reset the time until the animation
    # manager returns to the "idle" state
    def trigger_anim(self, state):
        self.broadcast_anim(state)
        return self.start_new_anim(state)

    def start_new_anim(self, state):
        self.state = state
        anim, time = self.model.get_anim(self.state)
        if anim == None:
            anim = self.model.get_anim("idle")
        self.expires_in = time
        return anim

    def broadcast_anim(self, state):
        if state == "idle":
            return
        try:
            connection.Send({
                "action": "animation",
                "state": state,
                "uuid": self.wizard.uuid
            })
        except AttributeError as e:
            print("Animation broadcast failed, is the connection not ready yet? %s" % e)

    def update(self):
        if self.expires_in > 0:
            #print(f"FPS is {clock.get_fps()}")
            self.expires_in -= engine.settings.FRAMERATE
        elif self.expires_in <= 0:
            self.state = "idle"


