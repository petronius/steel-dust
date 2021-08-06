import pyglet

class Screen(object):
    def __init__(self, game):
        self.game = game
        self.x_offset = 0
        self.y_offset = 0
        
    def clear(self):
        pass
        
    def on_draw(self):
        self.game.window.cam.apply()