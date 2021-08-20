

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
    casting_combo = "PO"
    damage = 5
    defense = 0
    duration = 100
    anim = "cast1"

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
    casting_combo = "QWE"
    damage = 0
    defense = 10
    duration = 5
    anim = "cast2"

    def __init__(self):
        self._name = "Shield"

    def on_cast(self):
        pass
        
class LightningBlast:
    spell_level = 2
    mana_cost = 20
    casting_combo = "FGN"
    damage = 10
    defense = 0
    duration = 0
    anim = "cast3"
    
    def __init__(self):
        self._name = "Lightning Blast"
        
    def on_cast(self):
        pass
