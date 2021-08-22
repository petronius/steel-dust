from random import choice

import pyglet

import engine.hud.booklist


class Spellbook:

    def __init__(self, spells, batch, bg_group, fg_group):
        self.spell_labels = []
        self.casting_labels = {}
        self.cam_x, self.cam_y = 0, 0
        self.name = engine.hud.booklist.random_spellbook()
        num_spells = len(spells)
        for i, s in enumerate(spells):
            x = 10
            y = 10 + 30 * i
            self.spell_labels.append(pyglet.text.Label(s.casting_combo, font_name="Algerian", font_size=14, x=x, y=y, batch=batch, group=bg_group))
        self.spell_labels.append(pyglet.text.Label(self.name, font_name="Algerian", font_size=20, x=10, y=num_spells*50, batch=batch, group=bg_group))

        for i, s in enumerate(spells):
            x = 10
            y = 10 + 30 * i
            self.casting_labels[s.casting_combo] = (pyglet.text.Label("", font_name="Algerian", color=(255, 0, 0, 255), font_size=14, x=x, y=y, batch=batch, group=fg_group))

    @property
    def spell_pos_x(self):
        return self.cam_x + 10

    @property
    def spell_pos_y(self):
        return self.cam_y + 10

    def update_position(self, cam_x, cam_y):
        self.cam_x, self.cam_y = cam_x, cam_y

        for i, s in enumerate(self.spell_labels):
            s.position = self.spell_pos_x, self.spell_pos_y + 30 * i

        for i, s in enumerate(self.casting_labels.values()):
            s.position = self.spell_pos_x, self.spell_pos_y + 30 * i

    def update_batch(self, batch):
        for s in self.spell_labels:
            s.batch = batch

        for s in self.casting_labels:
            s.batch = batch
