import random

import pyglet

import engine.wizard.namelist
import engine.spells
import engine.resources


class Wizard(pyglet.sprite.Sprite):

    # everyone starts with the same spell list for now
    _spells = [
       engine.spells.Fireball,
       engine.spells.Shield,
    ]

    def __init__(self, name, batch, *args, **kwargs):
        default_image = engine.resources.wizard0
        super(Wizard, self).__init__(default_image, *args, **kwargs)
        self.update(scale=3.0)
        self._name = name
        self._hitpoints = 20
        self._mana = 100

        self.nameplate = pyglet.text.Label(self.__str__())

        self.batch = batch
        self.nameplate.batch = batch

    def __str__(self):
        return "The Wizard %s" % self._name


def random_wizard():
    return Wizard(random_name())


def random_name():
    name = random.choice(namelist.names)
    color = random.choice(namelist.colors)
    return "%s the %s" % (name, color)
