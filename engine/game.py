import pyglet

import engine.screens.menu
import engine.screens.level as level
import engine.camera


class Game(object):
    def __init__(self):
        self.current_screen = engine.screens.menu.MainMenu(self)


    def clearCurrentScreen(self):
        self.current_screen.clear()
        self.window.remove_handler("on_key_press", self.current_screen.on_key_press)
        self.window.remove_handler("on_draw", self.current_screen.on_draw)


    def startCurrentScreen(self):
        self.window.set_handler("on_key_press", self.current_screen.on_key_press)
        self.window.set_handler("on_draw", self.current_screen.on_draw)
        self.current_screen.start()


    def startPlaying(self):
        self.clearCurrentScreen()
        self.current_screen = level.LevelAdministrator(self)
        self.startCurrentScreen()

    def execute(self):
        self.window = engine.camera.CameraWindow()
        self.startCurrentScreen()
        pyglet.app.run()
