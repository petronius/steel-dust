import engine.hud.spellbook


class HUD:

    def __init__(self, level):
        self.level = level
        self.spellbook = engine.hud.spellbook.Spellbook(level.player_wizard._spells, level.batch, level.foreground, level.hudground)

    def update(self, dt):
        cast_mgr = self.level.player_wizard.cast_manager
        spell_list = self.level.player_wizard._spells

        for s in spell_list:
            if len(cast_mgr.curr_l) > 0:
                if s.casting_combo == cast_mgr.curr_l:
                    self.spellbook.casting_labels[s.casting_combo].text = ""
                elif s.casting_combo[:len(cast_mgr.curr_l)] == cast_mgr.curr_l:
                    self.spellbook.casting_labels[s.casting_combo].text = cast_mgr.curr_l
                else:
                    self.spellbook.casting_labels[s.casting_combo].text = ""

            if len(cast_mgr.curr_c) > 0:
                if s.casting_combo == cast_mgr.curr_c:
                    self.spellbook.casting_labels[s.casting_combo].text = ""
                elif s.casting_combo[:len(cast_mgr.curr_c)] == cast_mgr.curr_c:
                    self.spellbook.casting_labels[s.casting_combo].text = cast_mgr.curr_c
                else:
                    self.spellbook.casting_labels[s.casting_combo].text = ""

            if len(cast_mgr.curr_r) > 0:
                if s.casting_combo == cast_mgr.curr_r:
                    self.spellbook.casting_labels[s.casting_combo].text = ""
                elif s.casting_combo[:len(cast_mgr.curr_r)] == cast_mgr.curr_r:
                    self.spellbook.casting_labels[s.casting_combo].text = cast_mgr.curr_r
                else:
                    self.spellbook.casting_labels[s.casting_combo].text = ""

        current_cam = self.level.game.window.cam
        cam_x, cam_y = current_cam.x, current_cam.y
        self.spellbook.update_position(cam_x, cam_y)
