import pyglet

import engine.screens.menu
import engine.screens.level as level
import engine.camera


class Game(object):

    def __init__(self, host, port):
        self.current_screen = engine.screens.menu.MainMenu(self)
        self.window = None
        # Keep these, used by the level
        self.host = host
        self.port = port

    def clear_current_screen(self):
        self.current_screen.clear()
        self.window.pop_handlers()

    def start_current_screen(self):
        self.window.push_handlers(
            self.current_screen.on_key_press,
            self.current_screen.on_key_release,
            self.current_screen.on_draw,
        )
        self.current_screen.start()

    def start_playing(self, wizard_name):
        self.clear_current_screen()
        self.current_screen = level.StartingLevel(self, wizard_name)
        self.start_current_screen()

    def execute(self):
        self.window = engine.camera.CameraWindow()
        self.window.register_event_type("keyboard")
        self.start_current_screen()
        pyglet.app.run()
