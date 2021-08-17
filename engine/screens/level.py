from random import choice

import pyglet
from pyglet.window import key

from PodSixNet.Connection import ConnectionListener, connection

import pyshaders

import engine.screen
import engine.resources
import engine.settings
import engine.wizard
from engine.networking import ClientConnectionListener


class StartingLevel(engine.screen.Screen):

    def __init__(self, game, wizard_name):

        super(StartingLevel, self).__init__(game)
        self.game = game

        self.connection_listener = None
        self.connect_to_server(wizard_name)

        self.map_width, self.map_height = engine.settings.MAP_WIDTH, engine.settings.MAP_HEIGHT

        self.foreground = pyglet.graphics.OrderedGroup(1)
        self.background = pyglet.graphics.OrderedGroup(0)
        self.batch = pyglet.graphics.Batch()

        self.player_wizard = engine.wizard.Wizard(wizard_name, self.batch)
        self.movement_keys = set((key.LEFT, key.RIGHT, key.UP, key.DOWN))
        self.key_handler = {
            key.LEFT: False,
            key.RIGHT: False,
            key.UP: False,
            key.DOWN: False
        }
        pyglet.clock.schedule_interval(self.update, engine.settings.FRAMERATE)

#        try:
#            self.shader = pyshaders.from_files_names("shaders/sprite_shader.vert", "shaders/sprite_shader.frag")
#        except pyshaders.ShaderCompilationError as p:
#            self.shader = None
#            print(p.logs)
#            exit()

    def connect_to_server(self, wizard_name):
        self.connection_listener = ClientConnectionListener(self.game.host, self.game.port)
        self.connection_listener.Send({
            "action": "playerconnect",
            "name": wizard_name
        })
        print("(Client) Connected: ", self.connection_listener)

    def on_key_press(self, symbol, modifiers):
        if symbol in self.movement_keys:
            self.key_handler[symbol] = True
        self.player_wizard.key_press(symbol, modifiers)

    def on_key_release(self, symbol, modifiers):
        if symbol in self.movement_keys:
            self.key_handler[symbol] = False

    def start(self):
        self.player_wizard.x, self.player_wizard.y = 200, 200
        print("GO")

    def on_draw(self):
        super(StartingLevel, self).on_draw()
#        self.shader.use()
        self.game.window.clear()
        self.batch.draw()
#        pyshaders.ShaderProgram.clear()

    def clear(self):
        pass

    def update(self, dt):
        new_x, new_y = self.player_wizard.x, self.player_wizard.y
        if self.key_handler[key.LEFT]:
            new_x -= self.player_wizard._movespeed * dt
        if self.key_handler[key.RIGHT]:
            new_x += self.player_wizard._movespeed * dt
        if self.key_handler[key.UP]:
            new_y += self.player_wizard._movespeed * dt
        if self.key_handler[key.DOWN]:
            new_y -= self.player_wizard._movespeed * dt
        self.player_wizard.update(x=new_x, y=new_y)

        if self.connection_listener is not None:
            self.connection_listener.update()
