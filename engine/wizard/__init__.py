import random

import engine.wizard.namelist
import engine.spells


class Wizard:

    # everyone starts with the same spell list for now
    _spells = [
       engine.spells.Fireball,
       engine.spells.Shield,
    ]

    def __init__(self, name, color):
        self._name = name
        self._color = color
        self._hitpoints = 20
        self._mana = 100

    def __str__(self):
        return "The Wizard %s the %s" % (self._name, self._color)


def random_wizard():
    name = random.choice(namelist.names)
    color = random.choice(namelist.colors)
    return Wizard(name, color)
