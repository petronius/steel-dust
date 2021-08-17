import random

import pyglet

import engine.wizard.namelist
import engine.wizard.castmanager
import engine.spells
import engine.spells.spellbook
import engine.resources


class Wizard(pyglet.sprite.Sprite):

    # everyone starts with the same spell list for now
    _spells = [
       engine.spells.Fireball,
       engine.spells.Shield,
    ]

    def __init__(self, name, batch, *args, **kwargs):
        default_image = engine.resources.wizard0
        self.nameplate = None
        self.spellbook = None
        super(Wizard, self).__init__(default_image, *args, **kwargs)
        self.update(scale=3.0)
        self._name = name
        self._hitpoints = 20
        self._mana = 100
        self._movespeed = 200

        self.nameplate = pyglet.text.Label(self.__str__(), font_name='Papyrus', anchor_x='center', anchor_y='top')
        self.spellbook = engine.spells.spellbook.Spellbook(self._spells, batch)

        self.batch = batch
        self.nameplate.batch = batch

        self.cast_manager = engine.wizard.castmanager.CastManager(self._spells)

    def __str__(self):
        return "The Wizard %s" % self._name

    def key_press(self, key, modifiers):
        cast_spell = self.cast_manager.key_press(key, modifiers)
        if cast_spell:
            print("CASTING %s!" % cast_spell)

    def update(self, *args, **kwargs):
        super(Wizard, self).update(*args, **kwargs)
        if self.nameplate is not None:
            self.nameplate.x, self.nameplate.y = self.x, self.y
        if self.spellbook is not None:
            self.spellbook.position_update(self.position)


def random_wizard():
    return Wizard(random_name())


def random_name():
    name = random.choice(namelist.names)
    color = random.choice(namelist.colors)
    return "%s the %s" % (name, color)
