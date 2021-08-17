import pyglet

class Spellbook:

    def __init__(self, spells, batch):
        self.spell_labels = []
        for s in spells:
            self.spell_labels.append(pyglet.text.Label(s.casting_combo, font_name="Arial", font_size=14, x=50, y=50, batch=batch))
            print(s.casting_combo)

    def position_update(self, coords):
        x, y = coords
        for s in self.spell_labels:
            y -= 30
            s.position = x, y

    def update_batch(self, batch):
        for s in self.spell_labels:
            s.batch = batch
