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
        self.window.pop_handlers()

    def startCurrentScreen(self):
        self.window.push_handlers(
            self.current_screen.on_key_press,
            self.current_screen.on_draw,
            self.current_screen.key_handler
        )
        self.current_screen.start()

    def startPlaying(self, wizard_name):
        self.clearCurrentScreen()
        self.current_screen = level.StartingLevel(self, wizard_name)
        self.startCurrentScreen()
        self.connection = ClientConnection(self.host, self.port, wizard_name)
        self.connection.Send({
            "acton": "playerconnect",
            "name": wizard_name
        })

    def execute(self):
        self.window = engine.camera.CameraWindow()
        self.window.register_event_type("keyboard")
        self.startCurrentScreen()
        pyglet.app.run()
