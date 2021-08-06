import pyglet

class Spiff(pyglet.sprite.Sprite):
    def __init__(self, img):
        super(Spiff, self).__init__(img)
        self.x, self.y = 200, 200