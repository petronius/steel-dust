
class Screen(object):
    def __init__(self, game):
        self.game = game
        self.x_offset = 0
        self.y_offset = 0
        self.key_handler = None

    def clear(self):
        pass

    def on_draw(self):
        self.game.window.cam.apply()
