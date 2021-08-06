import pyglet
from pyglet.sprite import Sprite
from pyglet.window import key


class Player(Sprite):
	def __init__(self, screen, *args, **kwargs):
		super(Player, self).__init__(*args, **kwargs)
		self.screen_width = screen.width
		self.screen_height = screen.height
        
        self.key_handler = key.KeyStateHandler()
		
	@property
	def x(self):
		return self.screen_width/2
		
	def y(self):
		return self.screen_height/2
        
    def update(self, dt):
        if key_handler(key.LEFT):
            self.screen.x_offset += 100 * dt
        if key_handler(key.RIGHT):
            self.screen.x_offset -= 100*dt