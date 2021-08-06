from random import choice

import pyglet

import engine.screen
import engine.resources
import engine.settings
import engine.wizard


class StartingLevel(engine.screen.Screen):
    def __init__(self, game, wizard_name):
        super(StartingLevel, self).__init__(game)
        self.game = game
        self.map_width, self.map_height = engine.settings.MAP_WIDTH, engine.settings.MAP_HEIGHT
        self.foreground = pyglet.graphics.OrderedGroup(1)
        self.background = pyglet.graphics.OrderedGroup(0)
        self.wizard_name = wizard_name

    def on_key_press(self, symbol, modifiers):
        pass

    def start(self):
        self.batch = pyglet.graphics.Batch()
        self.terrain = []
        poly_vertices = (50, 500, 250, 400, -50, -100)
        self.test_poly = self.batch.add(3, pyglet.gl.GL_TRIANGLES, self.foreground,
                                         ('v2f/stream', poly_vertices),
                                        ('c3B', (50, 50, 255, 50, 50, 255,
                                                 50, 50, 255))
                                        )
        self.test_wizard = engine.wizard.Wizard(choice(engine.wizard.namelist.names), choice(engine.wizard.namelist.colors), self.batch)
        self.test_wizard.x, self.test_wizard.y = 200, 200
        print ("GO")

    def on_draw(self):
        super(StartingLevel, self).on_draw()
        self.game.window.clear()
        self.batch.draw()

    def clear(self):
        pass

    def update(self, dt):
        return
