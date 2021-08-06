import pyglet
from pyglet.window import key

import modules.screen
import modules.resources as resources

class MainMenu(modules.screen.Screen):
    def __init__(self, game):
        super(MainMenu, self).__init__(game)
        
    def handleNewGame(self):
        self.game.startPlaying()
                                             
    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE:
            self.game.startPlaying()
        else:
            pass
        
    def clear(self):
        pass
        
    def start(self):
        self.batch = pyglet.graphics.Batch()
        self.hello = pyglet.sprite.Sprite(img=resources.title, 
                                          x=0, 
                                          y=0, 
                                          batch=self.batch)
                                          
                                          
        
        
    def on_draw(self):
        self.game.window.clear()
        self.batch.draw()
