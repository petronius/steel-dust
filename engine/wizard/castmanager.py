import pyglet.window.key

class CastManager:

    bucket_l = "QWEASDXC"
    bucket_c = "RTFGHVBN"
    bucket_r = "UIOPJKLM"

    def __init__(self, spell_list, spellbook):
        self._spell_list = spell_list
        self.spellbook = spellbook
        self.curr_l = ""
        self.curr_c = ""
        self.curr_r = ""

    def key_press(self, key, modifiers):
        k = pyglet.window.key.symbol_string(key)
        if k in self.bucket_l:
            self.curr_l += k

            for s in self._spell_list:                                                      # I
                if s.casting_combo[:len(self.curr_l)] == self.curr_l:                       # TRIED
                    self.spellbook.casting_labels[s.casting_combo].text = self.curr_l       # TO
                else:                                                                       # GENERALIZE
                    self.spellbook.casting_labels[s.casting_combo].text = ""                # THIS

        elif k in self.bucket_c:
            self.curr_c += k

            for s in self._spell_list:                                                      # AND
                if s.casting_combo[:len(self.curr_c)] == self.curr_c:                       # IT
                    self.spellbook.casting_labels[s.casting_combo].text = self.curr_c       # DIDN'T
                else:                                                                       # WORK
                    self.spellbook.casting_labels[s.casting_combo].text = ""                # MAYBE

        elif k in self.bucket_r:
            self.curr_r += k

            for s in self._spell_list:                                                      # YOU
                if s.casting_combo[:len(self.curr_r)] == self.curr_r:                       # CAN
                    self.spellbook.casting_labels[s.casting_combo].text = self.curr_r       # FIX
                else:                                                                       # IT
                    self.spellbook.casting_labels[s.casting_combo].text = ""                # THANKS

        for spell in self._spell_list:
            if self.curr_l.endswith(spell.casting_combo):
                self.curr_l = ""
                return spell
            elif self.curr_r.endswith(spell.casting_combo):
                self.curr_r = ""
                return spell
            elif self.curr_c.endswith(spell.casting_combo):
                self.curr_c = ""
                return spell

