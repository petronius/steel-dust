import pyglet
from pyglet.window import key

import glooey

import engine.screen
import engine.resources as resources
import engine.wizard


class MenuLabel(glooey.Label):
    custom_font_name = 'Lato Regular'
    custom_font_size = 16
    custom_color = '#ffffff'
    custom_alignment = 'center'


class MainMenu(engine.screen.Screen):
    def __init__(self, game):
        super(MainMenu, self).__init__(game)
        self.wizard_names = [
            engine.wizard.random_name(),
            engine.wizard.random_name(),
            engine.wizard.random_name(),
        ]

    def handleNewGame(self):
        self.game.startPlaying()

    def on_key_press(self, symbol, modifiers):
        if symbol == key._1:
            self.game.startPlaying(self.wizard_names[0])
        elif symbol == key._2:
            self.game.startPlaying(self.wizard_names[1])
        elif symbol == key._3:
            self.game.startPlaying(self.wizard_names[2])
        else:
            pass

    def on_key_release(self, symbol, modifiers):
        pass

    def clear(self):
        pass

    def start(self):
        self.batch = pyglet.graphics.Batch()
        self.hello = pyglet.sprite.Sprite(img=resources.title,
                                          x=0,
                                          y=0,
                                          batch=self.batch)
        self.hello.scale = self.game.window.get_pixel_ratio()
        self.gui()

    def gui(self):
        self.gui_batch = pyglet.graphics.Batch()
        gui = glooey.Gui(self.game.window, batch=self.gui_batch)

        vbox = glooey.VBox()
        vbox.add(MenuLabel("CHOOSE YOUR WIZARD NAME"))
        vbox.add(MenuLabel("(by pressing the associated key)"))
        vbox.add(MenuLabel("1 – %s" % self.wizard_names[0]))
        vbox.add(MenuLabel("2 – %s" % self.wizard_names[1]))
        vbox.add(MenuLabel("3 – %s" % self.wizard_names[2]))
        gui.add(vbox)

    def on_draw(self):
        self.game.window.clear()
        self.batch.draw()
        self.gui_batch.draw()
