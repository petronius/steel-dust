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
        self.batch = pyglet.graphics.Batch()
        self.player_wizard = engine.wizard.Wizard(wizard_name, self.batch)

    def on_key_press(self, symbol, modifiers):
        self.player_wizard.key_press(symbol, modifiers)

    def start(self):
        self.player_wizard.x, self.player_wizard.y = 200, 200
        print("GO")

    def on_draw(self):
        super(StartingLevel, self).on_draw()
        self.game.window.clear()
        self.batch.draw()

    def clear(self):
        pass

    def update(self, dt):
        return
