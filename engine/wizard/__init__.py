import random

import pyglet
from pyglet import clock
from pyglet.window import key

from PodSixNet.Connection import connection, ConnectionListener

import engine.wizard.namelist
import engine.wizard.castmanager
import engine.spells
import engine.hud.spellbook
import engine.resources
import random


class Wizard(pyglet.sprite.Sprite, ConnectionListener):

    # everyone starts with the same spell list for now
    _spells = [
       engine.spells.Fireball,
       engine.spells.Shield,
       engine.spells.LightningBlast
    ]

    def __init__(self, name, batch, uuid, *args, **kwargs):
        self.uuid = uuid
        self.nameplate = None
        self.model = random.choice(engine.resources.wizard_models)
        self.animation_manager = engine.wizard.animationmanager.AnimationManager(self, self.model)
        super(Wizard, self).__init__(self.animation_manager.start_new_anim("birth"), *args, **kwargs)

        self._name = name
        self._hitpoints = 20
        self._mana = 100
        self._movespeed = 200
        self.movement_keys = {key.LEFT, key.RIGHT, key.UP, key.DOWN}
        self.key_handler = {
            key.LEFT: False,
            key.RIGHT: False,
            key.UP: False,
            key.DOWN: False
        }
        self._disabled = False
        self._queued_for_removal = False
        super(Wizard, self).update(scale=3.0)

        self.nameplate = pyglet.text.Label(self.__str__(), font_name='Papyrus', anchor_x='center', anchor_y='top')

        self.batch = batch
        self.nameplate.batch = batch

        self.cast_manager = engine.wizard.castmanager.CastManager(self._spells)

    def __str__(self):
        return "The Wizard %s" % self._name

    def on_key_press(self, symbol, modifiers):
        if not self._disabled:
            if symbol in self.movement_keys:
                self.key_handler[symbol] = True

            cast_spell = self.cast_manager.key_press(symbol, modifiers)
            if cast_spell:
                self.image = self.animation_manager.start_new_anim(cast_spell.anim)
                print("CASTING %s!" % cast_spell)

    def on_key_release(self, symbol, modifiers):
        if not self._disabled:
            if symbol in self.movement_keys:
                self.key_handler[symbol] = False

    def animation_test(self, key, modifiers):
        if key == 49:
            self.image = self.animation_manager.start_new_anim("birth")
        if key == 50:
            self.image = self.animation_manager.start_new_anim("walk")
        if key == 51:
            self.image = self.animation_manager.start_new_anim("hit")
        if key == 52:
            self.image = self.animation_manager.start_new_anim("cast1")
        if key == 53:
            self.image = self.animation_manager.start_new_anim("cast2")
        if key == 54:
            self.image = self.animation_manager.start_new_anim("cast3")
        if key == 55:
            self.image = self.animation_manager.start_new_anim("death")
        if key == 56:
            self.model = random.choice(engine.resources.wizard_models)
            self.animation_manager = engine.wizard.animationmanager.AnimationManager(self, self.model)
            super(Wizard, self).__init__(self.animation_manager.start_new_anim("birth"), *args, **kwargs)
        # This Kills The Wizard
        if key == 57:
            self._hitpoints = -1

    def update_position(self, x, y):
        self.set_position(x, y)
        connection.Send({
            "action": "position",
            "uuid": self.uuid,
            "position": (self.x, self.y),
        })

    def set_position(self, x, y):
        super(Wizard, self).update(x=x, y=y)

    def update(self, dt):
        new_x, new_y = self.x, self.y
        if self.key_handler[key.LEFT]:
            new_x -= self._movespeed * dt
        if self.key_handler[key.RIGHT]:
            new_x += self._movespeed * dt
        if self.key_handler[key.UP]:
            new_y += self._movespeed * dt
        if self.key_handler[key.DOWN]:
            new_y -= self._movespeed * dt

        if new_x != self.x or new_y != self.y:
            self.update_position(x=new_x, y=new_y)

        self.animation_manager.update()
        if self.animation_manager.state == "idle" and self.animation_manager.expires_in <= 0:
            self.image = self.animation_manager.start_new_anim("idle")

        if self.nameplate is not None:
            self.nameplate.x, self.nameplate.y = self.x, self.y

        self.Pump()
        
        if self._hitpoints <= 0 and self._queued_for_removal == False:
            self.die()

    def die(self):
        self.image = self.animation_manager.trigger_anim("death")
        self._disabled = True  # disables all input
        self._queued_for_removal = True  # used to prevent die() from being called endlessley from update()
        for k in self.key_handler:
            self.key_handler[k] = False
        #queue removal at a delay equal to the duration of the death animation
        clock.schedule_once(self.remove_scheduled, self.model.animations["death"].get_duration())

    def remove_scheduled(self, delay):
        self.remove()
        
    def remove(self):
        self.batch = None
        self.nameplate.batch = None

    #
    # Network events
    #
    def Network_position(self, data):
        uuid = data.get("uuid")
        if uuid == self.uuid:
            x, y = data.get("position")
            self.set_position(x=x, y=y)

    def Network_animation(self, data):
        uuid = data.get("uuid")
        if uuid == self.uuid:
            print("network animation: %s" % data)
            self.image = self.animation_manager.start_new_anim(data.get("state"))