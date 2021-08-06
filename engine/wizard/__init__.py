
class Wizard:

    def __init__(self, name, color):
        self._name = name
        self._color = color

    def __str__(self):
        return "(The Wizard %s, the %s)" % (self._name, self._color)
