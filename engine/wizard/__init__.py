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
        self.animation_manager = engine.wizard.animationmanager.AnimationManager(engine.resources.model_purp_wiz)
        self.nameplate = None
        self.spellbook = None
        super(Wizard, self).__init__(self.animation_manager.start_new_anim("idle"), *args, **kwargs)
        self._name = name
        self._hitpoints = 20
        self._mana = 100
        self._movespeed = 200
        self.update(scale=3.0)

        self.nameplate = pyglet.text.Label(self.__str__(), font_name='Papyrus', anchor_x='center', anchor_y='top')
        self.spellbook = engine.spells.spellbook.Spellbook(self._spells, batch)

        self.batch = batch
        self.nameplate.batch = batch

        self.cast_manager = engine.wizard.castmanager.CastManager(self._spells, self.spellbook)

    def __str__(self):
        return "The Wizard %s" % self._name

    def key_press(self, key, modifiers):        
        cast_spell = self.cast_manager.key_press(key, modifiers)
        if cast_spell:
            self.spellbook.casting_labels[cast_spell.casting_combo].text = ""
            print("CASTING %s!" % cast_spell)
            
    def animation_test(self, key, modifiers):
        if key == 57:
            self.image = self.animation_manager.start_new_anim("cast1")

    def update(self, *args, **kwargs):
        self.animation_manager.update()
        print(self.animation_manager.state)
        print(self.animation_manager.expires_in)
        if self.animation_manager.state == "idle" and self.animation_manager.expires_in <= 0:
            self.image = self.animation_manager.start_new_anim("idle")
            
        super(Wizard, self).update(*args, **kwargs)
        if self.nameplate is not None:
            self.nameplate.x, self.nameplate.y = self.x, self.y
#        if self.spellbook is not None:
#            self.spellbook.position_update(self.position)


def random_wizard():
    return Wizard(random_name())


def random_name():
    name = random.choice(namelist.names)
    color = random.choice(namelist.colors)
    return "%s the %s" % (name, color)
