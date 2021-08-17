import random

import pyglet
from PodSixNet.Connection import connection, ConnectionListener

import engine.wizard.namelist
import engine.wizard.castmanager
import engine.spells
import engine.hud.spellbook
import engine.resources


class Wizard(pyglet.sprite.Sprite, ConnectionListener):

    # everyone starts with the same spell list for now
    _spells = [
       engine.spells.Fireball,
       engine.spells.Shield,
    ]

    def __init__(self, name, batch, uuid, *args, **kwargs):
        self.uuid = uuid
        self.nameplate = None

        self.animation_manager = engine.wizard.animationmanager.AnimationManager(engine.resources.model_purp_wiz)
        super(Wizard, self).__init__(self.animation_manager.start_new_anim("idle"), *args, **kwargs)

        self._name = name
        self._hitpoints = 20
        self._mana = 100
        self._movespeed = 200
        self.update(scale=3.0)

        self.nameplate = pyglet.text.Label(self.__str__(), font_name='Papyrus', anchor_x='center', anchor_y='top')

        self.batch = batch
        self.nameplate.batch = batch

        self.cast_manager = engine.wizard.castmanager.CastManager(self._spells)

    def __str__(self):
        return "The Wizard %s" % self._name

    def key_press(self, key, modifiers):
        cast_spell = self.cast_manager.key_press(key, modifiers)
        if cast_spell:
            print("CASTING %s!" % cast_spell)

    def animation_test(self, key, modifiers):
        if key == 57:
            self.image = self.animation_manager.start_new_anim("cast1")

    def update_position(self, x, y):
        self.Send({
            "action": "position",
            "uuid": self.uuid,
            "position": (self.x, self.y),
        })
        super(Wizard, self).update(x=x, y=y)

    def update(self):
        self.animation_manager.update()
        if self.animation_manager.state == "idle" and self.animation_manager.expires_in <= 0:
            self.image = self.animation_manager.start_new_anim("idle")

        if self.nameplate is not None:
            self.nameplate.x, self.nameplate.y = self.x, self.y

        self.Pump()

    def remove(self):
        self.batch = None
        self.nameplate.batch = None

    # Network events
    def Network_position(self, data):
        uuid = data.get("uuid")
        if uuid == self.uuid:
            x, y = data.get("position")
            self.update_position(x=x, y=y)

def random_wizard():
    return Wizard(random_name())


def random_name():
    name = random.choice(namelist.names)
    color = random.choice(namelist.colors)
    return "%s the %s" % (name, color)
