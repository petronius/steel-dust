from random import choice
import uuid

import pyglet
from pyglet.window import key

from PodSixNet.Connection import ConnectionListener, connection

import pyshaders

import engine.screen
import engine.resources
import engine.settings
import engine.wizard
from engine.screens.networking import ClientConnectionListener


class StartingLevel(engine.screen.Screen):

    def __init__(self, game, wizard_name):

        super(StartingLevel, self).__init__(game)
        self.game = game

        self.local_player_id = str(uuid.uuid4())

        self.map_width, self.map_height = engine.settings.MAP_WIDTH, engine.settings.MAP_HEIGHT

        self.foreground = pyglet.graphics.OrderedGroup(1)
        self.background = pyglet.graphics.OrderedGroup(0)
        self.batch = pyglet.graphics.Batch()

        self.player_wizard = engine.wizard.Wizard(wizard_name, self.batch)
        self.player_wizard.update(x=200, y=200)
        self.movement_keys = set((key.LEFT, key.RIGHT, key.UP, key.DOWN))
        self.key_handler = {
            key.LEFT: False,
            key.RIGHT: False,
            key.UP: False,
            key.DOWN: False
        }
        pyglet.clock.schedule_interval(self.update, engine.settings.FRAMERATE)

        self.enemy_wizards = {}

        self.connection_listener = None
        self.connect_to_server(wizard_name)

#        try:
#            self.shader = pyshaders.from_files_names("shaders/sprite_shader.vert", "shaders/sprite_shader.frag")
#        except pyshaders.ShaderCompilationError as p:
#            self.shader = None
#            print(p.logs)
#            exit()

    def connect_to_server(self, wizard_name):
        self.connection_listener = ClientConnectionListener(self)
        self.connection_listener.Send({
            "action": "playerconnect",
            "name": wizard_name,
            "uuid": self.local_player_id,
            "position": (self.player_wizard.x, self.player_wizard.y),
        })

    def player_connect(self, event_data):
        if event_data.get("uuid") == self.local_player_id:
            pass
        else:
            w = engine.wizard.Wizard(event_data.get("name"), self.batch)
            w.x, w.y = event_data.get("position")
            w.update(x=w.x, y=w.y)
            self.enemy_wizards[event_data.get("uuid")] = w

    def update_players(self, data):
        uuids = {p.get("uuid"): p for p in data.get("players")}
        # Check for uuids that are in the local list of enemy wizards, but not in the player list: those players have
        # disconnected.
        for uuid in self.enemy_wizards:
            if uuid not in uuids:
                self.player_disconnect(uuids.get(uuid))
        # Check for uuids that the server has sent us, but are not in the enemy wizard list yet: those are new
        # connections
        for uuid in uuids:
            if uuid not in self.enemy_wizards and uuid != self.local_player_id:
                self.player_connect(uuids.get(uuid))

    def player_disconnect(self, event_data):
        self.enemy_wizards[event_data.get("uuid")].batch = None
        del self.enemy_wizards[event_data.get("uuid")]

    def player_position(self, event_data):
        print("position update:", event_data)
        w = self.enemy_wizards.get(event_data.get("uuid"))
        if w and event_data.get("position"):
            x, y = event_data.get("position")
            w.update(x=x, y=y)

    def on_key_press(self, symbol, modifiers):
        if symbol in self.movement_keys:
            self.key_handler[symbol] = True
        self.player_wizard.key_press(symbol, modifiers)

    def on_key_release(self, symbol, modifiers):
        if symbol in self.movement_keys:
            self.key_handler[symbol] = False

    def start(self):
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

        if self.player_wizard.x != new_x or self.player_wizard.y != new_y:
            if self.connection_listener:
                self.connection_listener.Send({
                    "action": "position",
                    "uuid": self.local_player_id,
                    "position": (self.player_wizard.x, self.player_wizard.y),
                })
            self.player_wizard.update(x=new_x, y=new_y)

        if self.connection_listener:
            self.connection_listener.update()
