# 조준점 관련 함수 오음
import random

from pico2d import *

from config import *
from game_work import game_framework


def load_target(t):
    t.target_up = load_image(target_up_directory)
    t.target_down = load_image(target_down_directory)
    t.target_right = load_image(target_right_directory)
    t.target_left = load_image(target_left_directory)

    t.not_target = load_image(target_x_directory)
    t.target_melee = load_image(target_melee_directory)

    t.scope_awp = load_image(scope_awp_directory)
    t.scope_spring = load_image(scope_spring_directory)
    t.scope_kar98 = load_image(scope_kar98_directory)
    t.scope_m24 = load_image(scope_m24_directory)
    t.scope_cheytac = load_image(scope_cheytac_directory)


def draw_target(t):
    if t.weapon.weapon_type == 0:
        if t.weapon.gun_type == 'sr':
            if t.draw_scope:
                x = t.p.mx + t.p.shake_x
                y = t.p.my + t.p.shake_y

                if t.weapon.gun == 'SPRING':
                    t.scope_spring.opacify(50)
                    t.scope_spring.rotate_draw(t.p.scope_rot, x, y, t.scope_size_x, t.scope_size_y)
                if t.weapon.gun == 'KAR98':
                    t.scope_kar98.opacify(50)
                    t.scope_kar98.rotate_draw(t.p.scope_rot, x, y, t.scope_size_x, t.scope_size_y)
                if t.weapon.gun == 'M24':
                    t.scope_m24.opacify(50)
                    t.scope_m24.rotate_draw(t.p.scope_rot, x, y, t.scope_size_x, t.scope_size_y)
                if t.weapon.gun == 'AWP':
                    t.scope_awp.opacify(50)
                    t.scope_awp.rotate_draw(t.p.scope_rot, x, y, t.scope_size_x, t.scope_size_y)
                if t.weapon.gun == 'CHEYTAC':
                    t.scope_cheytac.opacify(50)
                    t.scope_cheytac.rotate_draw(t.p.scope_rot, x, y, t.scope_size_x, t.scope_size_y)

            else:
                t.target_up.opacify(150)
                t.target_down.opacify(150)
                t.target_left.opacify(150)
                t.target_right.opacify(150)
                t.target_up.draw(t.p.mx, t.p.my + t.recoil + t.dis2 + 30, 60, 60)
                t.target_down.draw(t.p.mx, t.p.my - t.recoil - t.dis2 - 30, 60, 60)
                t.target_right.draw(t.p.mx + t.recoil + t.dis2 + 30, t.p.my, 60, 60)
                t.target_left.draw(t.p.mx - t.recoil - t.dis2 - 30, t.p.my, 60, 60)

        else:
            t.target_up.opacify(1)
            t.target_down.opacify(1)
            t.target_left.opacify(1)
            t.target_right.opacify(1)
            t.target_up.draw(t.p.mx, t.p.my + t.recoil + t.dis2 + 30, 60, 60)
            t.target_down.draw(t.p.mx, t.p.my - t.recoil - t.dis2 - 30, 60, 60)
            t.target_right.draw(t.p.mx + t.recoil + t.dis2 + 30, t.p.my, 60, 60)
            t.target_left.draw(t.p.mx - t.recoil - t.dis2 - 30, t.p.my, 60, 60)

    elif t.weapon.weapon_type == 1:
        t.not_target.draw(t.p.mx, t.p.my, 120, 120)
        t.tmy = t.p.y
        y = t.tmy + t.p.cam_y - t.p.push_y

        if t.weapon.melee == 'KNIFE':
            if t.p.dir == 1:
                t.tmx = t.p.x + 180
                t.target_melee.composite_draw(0, '', t.tmx + t.p.cam_x, y, 100, 150)
            elif t.p.dir == 0:
                t.tmx = t.p.x - 180
                t.target_melee.composite_draw(0, 'h', t.tmx + t.p.cam_x, y, 100, 150)

        elif t.weapon.melee == 'BAT':
            if t.p.dir == 1:
                t.tmx = t.p.x + 220
                t.target_melee.composite_draw(0, '', t.tmx + t.p.cam_x, y, 100, 150)
            elif t.p.dir == 0:
                t.tmx = t.p.x - 220
                t.target_melee.composite_draw(0, 'h', t.tmx + t.p.cam_x, y, 100, 150)


def update_target(t):
    pps = game_framework.pps
    t.dis = math.sqrt((t.p.mx - (t.p.x + t.p.cam_x)) ** 2 + (t.p.my - (t.p.y + t.p.cam_y)) ** 2)

    if t.recoil > 0:
        t.recoil -= pps / 7
    else:
        t.recoil = 0

    if t.dis < 0:  # 분산도가 0 밑으로 내려가지 않도록 한다.
        t.dis = 0

    # 나누는 숫자가 작을 수록 분산도가 커진다.
    # 총기마다 반동 수치가 달라 조준점이 벌어지는 정도가 다르다.
    if t.weapon.gun == 'M1911':
        t.dis2 = t.dis / 15
        if t.weapon.shoot:
            t.recoil += 20

    elif t.weapon.gun == 'M92':
        t.dis2 = t.dis / 15
        if t.weapon.shoot:
            t.recoil += 20

    elif t.weapon.gun == 'DEGLE':
        t.dis2 = t.dis / 15
        if t.weapon.shoot:
            t.recoil += 45

    elif t.weapon.gun == 'M500':
        t.dis2 = t.dis / 15
        if t.weapon.shoot:
            t.recoil += 65

    elif t.weapon.gun == 'QHAND':
        t.dis2 = t.dis / 13
        if t.weapon.shoot:
            t.recoil += 20

    elif t.weapon.gun == 'AKS74':
        t.dis2 = t.dis / 30
        if t.weapon.shoot:
            t.recoil += 13

    elif t.weapon.gun == 'UMP':
        t.dis2 = t.dis / 25
        if t.weapon.shoot:
            t.recoil += 17

    elif t.weapon.gun == 'VECTOR':
        t.dis2 = t.dis / 12
        if t.weapon.shoot:
            t.recoil += 8

    elif t.weapon.gun == 'THOMPSON':
        t.dis2 = t.dis / 20
        if t.weapon.shoot:
            t.recoil += 16

    elif t.weapon.gun == 'P90':
        t.dis2 = t.dis / 20
        if t.weapon.shoot:
            t.recoil += 12

    elif t.weapon.gun == 'SCAR_H':
        t.dis2 = t.dis / 20
        if t.weapon.shoot:
            t.recoil += 20

    elif t.weapon.gun == 'M16':
        t.dis2 = t.dis / 30
        if t.weapon.shoot:
            t.recoil += 15

    elif t.weapon.gun == 'MP44':
        t.dis2 = t.dis / 35
        if t.weapon.shoot:
            t.recoil += 29

    elif t.weapon.gun == 'AUG':
        t.dis2 = t.dis / 45
        if t.weapon.shoot:
            t.recoil += 16

    elif t.weapon.gun == 'GROZA':
        t.dis2 = t.dis / 40
        if t.weapon.shoot:
            t.recoil += 13

    elif t.weapon.gun == 'M1':
        t.dis2 = t.dis / 55
        if t.weapon.shoot:
            t.recoil += 110

    elif t.weapon.gun == 'WIN':
        t.dis2 = t.dis / 55
        if t.weapon.shoot:
            t.recoil += 120

    elif t.weapon.gun == 'MINI14':
        t.dis2 = t.dis / 55
        if t.weapon.shoot:
            t.recoil += 65

    elif t.weapon.gun == 'FAL':
        t.dis2 = t.dis / 55
        if t.weapon.shoot:
            t.recoil += 83

    elif t.weapon.gun == 'LVOAS':
        t.dis2 = t.dis / 55
        if t.weapon.shoot:
            t.recoil += 35

    elif t.weapon.gun_type == 'sr':
        t.dis2 = 0
        update_scope(t)


def make_target_point(t):  # 이 함수에서 생성되는 좌표로 적 피격을 판정한다.
    if t.weapon.shoot:
        t.tx = random.randint \
            (t.p.mx - int(t.recoil) - int(t.dis2) - 1, t.p.mx + int(t.recoil) + int(t.dis2) + 1)
        t.ty = random.randint \
            (t.p.my - int(t.recoil) - int(t.dis2) - 1, t.p.my + int(t.recoil) + int(t.dis2) + 1)


def update_scope(t):
    pps = game_framework.pps
    if t.weapon.zoom:  # 우클릭 시 스코프 애니메이션 출력
        if t.weapon.bolt_action:  # 발사 후에는 자동으로 스코프가 비활성화 되었다가 다시 활성화 된다
            if t.scope_size_x < 32768:
                t.scope_size_x += 400 * pps
            if t.scope_size_y < 16384:
                t.scope_size_y += 200 * pps

                if t.scope_size_x > 32768:
                    t.scope_size_x = 32768
                    t.draw_scope = False

                if t.scope_size_y > 16384:
                    t.scope_size_y = 16384
        else:
            t.draw_scope = True
            if t.scope_size_x > 8192:
                t.scope_size_x -= 400 * pps
            if t.scope_size_y > 4096:
                t.scope_size_y -= 200 * pps

                if t.scope_size_x < 8192:
                    t.scope_size_x = 8192
                if t.scope_size_y < 4096:
                    t.scope_size_y = 4096

    elif not t.weapon.zoom:
        if t.scope_size_x < 32768:
            t.scope_size_x += 400 * pps
        if t.scope_size_y < 16384:
            t.scope_size_y += 200 * pps

            if t.scope_size_x > 32768:
                t.scope_size_x = 32768
                t.draw_scope = False

            if t.scope_size_y > 16384:
                t.scope_size_y = 16384
