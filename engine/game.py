import pyglet

import engine.screens.menu
import engine.screens.level as level
import engine.camera
from engine.networking import ClientConnection

class Game(object):
    def __init__(self, host, port):
        self.current_screen = engine.screens.menu.MainMenu(self)
        self.connection = None
        self.host = host
        self.port = port

    def clearCurrentScreen(self):
        self.current_screen.clear()
        self.window.remove_handler("on_key_press", self.current_screen.on_key_press)
        self.window.remove_handler("on_draw", self.current_screen.on_draw)


    def startCurrentScreen(self):
        self.window.set_handler("on_key_press", self.current_screen.on_key_press)
        self.window.set_handler("on_draw", self.current_screen.on_draw)
        self.current_screen.start()


    def startPlaying(self, wizard_name):
        self.clearCurrentScreen()
        self.current_screen = level.StartingLevel(self, wizard_name)
        self.startCurrentScreen()
        self.connection = ClientConnection(self.host, self.port, "Captain Placeholder")

    def execute(self):
        self.window = engine.camera.CameraWindow()
        self.startCurrentScreen()
        pyglet.app.run()
