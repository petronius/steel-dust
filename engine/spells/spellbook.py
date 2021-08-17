import pyglet

class Spellbook:

    def __init__(self, spells, batch):
        self.spell_labels = []
        self.casting_labels = {}
        num_spells = len(spells)
        for i, s in enumerate(spells):
            x = 10
            y = 10 + 30 * i
            self.spell_labels.append(pyglet.text.Label(s.casting_combo, font_name="Arial", font_size=14, x=x, y=y, batch=batch))
        self.spell_labels.append(pyglet.text.Label("Book of Mystery", font_name="Papyrus", font_size=20, x=10, y=num_spells*50, batch=batch))

        for i, s in enumerate(spells):
            x = 10
            y = 10 + 30 * i
            self.casting_labels[s.casting_combo] = (pyglet.text.Label("", font_name="Arial", color=(255, 0, 0, 255), font_size=14, x=x, y=y, batch=batch))


#    def position_update(self, coords):
#        x, y = coords
#        for s in self.spell_labels:
#            y -= 30
#            s.position = x, y

    def update_batch(self, batch):
        for s in self.spell_labels:
            s.batch = batch

        for s in self.casting_labels:
            s.batch = batch
