def draw_melee(weapon):
    if weapon.weapon_type == 1:
        if weapon.melee_x == 0 and weapon.melee == 'KNIFE':
            weapon.melee_deg = 170

        elif weapon.melee == 'BAT' and not weapon.swing:
            weapon.melee_deg = 120

        elif weapon.melee == 'KATANA' and not weapon.swing:
            weapon.melee_deg = 0

        elif weapon.melee_x == 0 and weapon.melee == 'RAPIER':
            weapon.melee_deg = 0.3
            weapon.rapier_y = 0

        if weapon.melee == 'KNIFE':
            y = weapon.p.wy - 10  # 고정값

        elif weapon.melee == 'BAT':
            y = weapon.p.wy - 10

        elif weapon.melee == 'KATANA':
            y = weapon.p.wy - 10

        elif weapon.melee == 'RAPIER':
            y = weapon.p.wy - 10 + weapon.rapier_y

        if weapon.melee == 'KNIFE':
            if weapon.p.dir == 1:
                x = weapon.p.px + weapon.melee_x + 50
                weapon.knife_right.clip_composite_draw(0, 0, 150, 100, weapon.melee_deg, '', x, y, 100, 50)
            elif weapon.p.dir == 0:
                x = weapon.p.px - weapon.melee_x - 50
                weapon.knife_left.clip_composite_draw(0, 0, 150, 100, -weapon.melee_deg, '', x, y, 100, 50)

        elif weapon.melee == 'BAT':
            if not weapon.swing or (weapon.swing and weapon.swing_up):
                if weapon.p.dir == 1:
                    x = weapon.p.px + weapon.melee_x
                    weapon.bat.clip_composite_draw(0, 0, 50, 400, weapon.melee_deg, '', x, y, 50, 400)
                elif weapon.p.dir == 0:
                    x = weapon.p.px - weapon.melee_x
                    weapon.bat.clip_composite_draw(0, 0, 50, 400, -weapon.melee_deg, 'h', x, y, 50, 400)

            elif weapon.swing and weapon.swing_down:
                if weapon.p.dir == 1:
                    x = weapon.p.px + weapon.melee_x
                    weapon.bat_swing.clip_composite_draw(0, 0, 400, 400, weapon.melee_deg, '', x, y, 400, 400)
                elif weapon.p.dir == 0:
                    x = weapon.p.px - weapon.melee_x
                    weapon.bat_swing.clip_composite_draw(0, 0, 400, 400, -weapon.melee_deg, 'h', x, y, 400, 400)

        elif weapon.melee == 'RAPIER':
            if weapon.p.dir == 1:
                x = weapon.p.px + weapon.melee_x + 20
                weapon.rapier.clip_composite_draw(0, 0, 350, 100, weapon.melee_deg, '', x, y, 335, 75)
            elif weapon.p.dir == 0:
                x = weapon.p.px - weapon.melee_x - 20
                weapon.rapier.clip_composite_draw(0, 0, 350, 100, -weapon.melee_deg, 'h', x, y, 335, 75)

            if weapon.skill_enable:
                if weapon.p.dir == 1:
                    rx = weapon.p.px + weapon.melee_x + 170 + weapon.rapid_x
                    weapon.rapid.clip_composite_draw(0, 0, 350, 100, 0, '', rx, y, 335, 75)
                elif weapon.p.dir == 0:
                    rx = weapon.p.px - weapon.melee_x - 170 - weapon.rapid_x
                    weapon.rapid.clip_composite_draw(0, 0, 350, 100, 0, 'h', rx, y, 335, 75)

        elif weapon.melee == 'KATANA':
            if not weapon.swing or (weapon.swing and weapon.swing_up):
                if weapon.p.dir == 1:
                    x = weapon.p.px + weapon.melee_x + 40
                    weapon.katana.clip_composite_draw(0, 0, 60, 410, weapon.melee_deg, '', x, y, 50, 360)
                elif weapon.p.dir == 0:
                    x = weapon.p.px - weapon.melee_x - 40
                    weapon.katana.clip_composite_draw(0, 0, 60, 410, -weapon.melee_deg, 'h', x, y, 50, 360)

            elif weapon.swing and weapon.swing_down:
                if weapon.p.dir == 1:
                    x = weapon.p.px + weapon.melee_x + 40
                    weapon.katana_swing.clip_composite_draw(0, 0, 410, 410, weapon.melee_deg, '', x, y, 400, 360)
                elif weapon.p.dir == 0:
                    x = weapon.p.px - weapon.melee_x - 40
                    weapon.katana_swing.clip_composite_draw(0, 0, 410, 410, -weapon.melee_deg, 'h', x, y, 400, 360)


