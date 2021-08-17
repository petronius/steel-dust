import pyglet.window.key

class CastManager:

    bucket_l = "QWEASDXC"
    bucket_c = "RTFGHVBN"
    bucket_r = "UIOPJKLM"

    def __init__(self, spell_list):
        self._spell_list = spell_list
        self.curr_l = ""
        self.curr_c = ""
        self.curr_r = ""

    def key_press(self, key, modifiers):
        k = pyglet.window.key.symbol_string(key)
        if k in self.bucket_l:
            self.curr_l += k
        elif k in self.bucket_c:
            self.curr_c += k
        elif k in self.bucket_r:
            self.curr_r += k

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

