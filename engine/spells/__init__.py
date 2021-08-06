

class Spell:

    spell_level = 1
    mana_cost = 10
    casting_combo = ""

    def __init__(self):
        raise NotImplementedError("Subclass the Spell class rather than using it directly")

    def on_cast(self):
        raise NotImplementedError("Subclass the Spell class rather than using it directly")


class Fireball:
    """
    Simple fireball spell.
    """
    spell_level = 1
    mana_cost = 5
    casting_combo = "()"
    casting_type = "SINGLE_SHOT"
    damage = 5
    defense = 0

    def __init__(self):
        self._name = "Fireball"

    def on_cast(self):
        pass


class Shield:
    """
    Simple shield spell. Active while the keycombo is held, and has a limit on damage it can block
    """
    spell_level = 1
    mana_cost = 10
    casting_combo = " "
    casting_type = "CHANNELED"
    damage = 0
    defense = 10

    def __init__(self):
        self._name = "Fireball"

    def on_cast(self):
        pass
