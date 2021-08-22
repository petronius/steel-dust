from random import choice
import uuid

import pyglet
from pyglet.window import key
from pyglet.gl import *

from PodSixNet.Connection import connection

import pyshaders

import engine.screen
import engine.resources
import engine.settings
import engine.wizard
import engine.hud
from engine.screens.networking import ClientConnectionListener


class StartingLevel(engine.screen.Screen):

    def __init__(self, game, wizard_name):

        super(StartingLevel, self).__init__(game)
        self.game = game

        self.local_player_id = str(uuid.uuid4())

        self.map_width, self.map_height = engine.settings.MAP_WIDTH, engine.settings.MAP_HEIGHT

        self.hudground = pyglet.graphics.OrderedGroup(2)
        self.foreground = pyglet.graphics.OrderedGroup(1)
        self.background = pyglet.graphics.OrderedGroup(0)
        self.bg_batch = pyglet.graphics.Batch()
        self.batch = pyglet.graphics.Batch()

        self.player_wizard = engine.wizard.Wizard(wizard_name, self.batch, self.local_player_id)
        self.hud = engine.hud.HUD(self)
        self.animation_test_keys = {key._1, key._2, key._3, key._4, key._5, key._6, key._7, key._8, key._9, key._0}
        pyglet.clock.schedule_interval(self.update, engine.settings.FRAMERATE)

        self.enemy_wizards = {}

        self.connection_listener = None
        self.player_wizard.set_position(x=200, y=200)
        self.connect_to_server(wizard_name)

        self.floor_texture = pyglet.image.TileableTexture.create_for_image(engine.resources.stone_floor)

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
            w = engine.wizard.Wizard(event_data.get("name"), self.batch, event_data.get("uuid"))
            w.x, w.y = event_data.get("position")
            w.set_position(x=w.x, y=w.y)
            self.enemy_wizards[event_data.get("uuid")] = w

    def update_players(self, data):
        uuids = {p.get("uuid"): p for p in data.get("players")}
        # Check for uuids that are in the local list of enemy wizards, but not in the player list: those players have
        # disconnected.
        for uuid in list(self.enemy_wizards.keys()):
            if uuid not in uuids:
                self.player_disconnect(uuid)
        # Check for uuids that the server has sent us, but are not in the enemy wizard list yet: those are new
        # connections
        for uuid in list(uuids.keys()):
            if uuid not in self.enemy_wizards and uuid != self.local_player_id:
                self.player_connect(uuids.get(uuid))

    def player_disconnect(self, uuid):
        self.enemy_wizards[uuid].remove()
        del self.enemy_wizards[uuid]

    def on_key_press(self, symbol, modifiers):
        self.player_wizard.on_key_press(symbol, modifiers)
        if symbol in self.animation_test_keys:
            self.player_wizard.animation_test(symbol, modifiers)

    def on_key_release(self, symbol, modifiers):
        self.player_wizard.on_key_release(symbol, modifiers)

    def start(self):
        print("GO")

    def on_draw(self):
        super(StartingLevel, self).on_draw()
#        self.shader.use()
        self.game.window.clear()
        self.floor_texture.blit_tiled(0, 0, 0, engine.settings.MAP_WIDTH, engine.settings.MAP_HEIGHT)
        self.batch.draw()
#        pyshaders.ShaderProgram.clear()

    def clear(self):
        pass

    def update(self, dt):
        self.player_wizard.update(dt)
        for w in self.enemy_wizards.values():
            w.update()

        self.hud.update(dt)

        if self.connection_listener:
            self.connection_listener.Pump()
        connection.Pump()
