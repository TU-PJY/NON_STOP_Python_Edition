from pico2d import *

from game_class.prop import Shell, Grenade
from game_work import game_manager, game_framework


def l_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_MOUSEBUTTONDOWN and e[1].button == SDL_BUTTON_LEFT


def l_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_MOUSEBUTTONUP and e[1].button == SDL_BUTTON_LEFT


def q_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_q


def r_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_MOUSEBUTTONDOWN and e[1].button == SDL_BUTTON_RIGHT


def r_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_MOUSEBUTTONUP and e[1].button == SDL_BUTTON_RIGHT


def reload_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_r


def shift_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LSHIFT


def change_weapon(weapon):
    if weapon.weapon_type == 0:  # 총을 들고 있을 때 총 -> 근접무기
        weapon.p.look_mouse = False  # 플레이어는 더 이상 마우스를 따라보지 않는다.
        weapon.p.rotate = 0
        weapon.weapon_type = 1
        weapon.flame_display_time = 0
        weapon.zoom = False
        return

    elif weapon.weapon_type == 1:  # 근접무기를 들고 있을 때 근접무기 -> 총
        weapon.p.look_mouse = True
        weapon.weapon_type = 0


def update_delay(weapon):  # 발사 간격과 근접 무기 공속 관리
    pps = game_framework.pps
    if weapon.shoot_delay > 0:
        weapon.shoot_delay -= pps / 3
    if weapon.wield_delay > 0:
        weapon.wield_delay -= pps / 3


def update_sniper_bolt(weapon):
    if weapon.gun == 'AWP':
        if 100 < weapon.shoot_delay < 500 and not weapon.shell_out:  # 탄피를 한 번만 만들도록 한다
            weapon.bolt_action = True
            make_shell(weapon, 30, 20)
            weapon.shell_out = True

    if weapon.gun == 'SPRING':
        if 100 < weapon.shoot_delay < 400 and not weapon.shell_out:
            weapon.bolt_action = True
            make_shell(weapon, 30, 20)
            weapon.shell_out = True

    if weapon.gun == 'KAR98':
        if 100 < weapon.shoot_delay < 400 and not weapon.shell_out:
            weapon.bolt_action = True
            make_shell(weapon, 30, 20)
            weapon.shell_out = True

    if weapon.gun == 'M24':
        if 100 < weapon.shoot_delay < 500 and not weapon.shell_out:
            weapon.bolt_action = True
            make_shell(weapon, 30, 20)
            weapon.shell_out = True

    if weapon.gun == 'CHEYTAC':
        if 100 < weapon.shoot_delay < 700 and not weapon.shell_out:  # 탄피를 한 번만 만들도록 한다
            weapon.bolt_action = True
            make_shell(weapon, 40, 30)
            weapon.shell_out = True

    if weapon.shoot_delay < 100:
        weapon.bolt_action = False
        weapon.shell_out = False
        if weapon.reload_need:  # 재장전 상태가 되면 정조준 해제
            weapon.zoom = False


def make_shell(weapon, size_x=15, size_y=15):  # 탄피 생성
    if weapon.p.dir == 0:
        shell = Shell \
            (weapon.p, weapon.mp, weapon.p.x - 20, weapon.p.y - weapon.p.cam_h + 10, weapon.p.dir, size_x, size_y)
    elif weapon.p.dir == 1:
        shell = Shell \
            (weapon.p, weapon.mp, weapon.p.x + 20, weapon.p.y - weapon.p.cam_h + 10, weapon.p.dir, size_x, size_y)
    game_manager.add_object(shell, 4)  # 총을 발사하면 탄피가 나온다


def reload_gun(weapon):
    if weapon.weapon_type == 0:
        pps = game_framework.pps

        weapon.zoom = False
        if weapon.cur_reload_time < weapon.reload_time:  # 정해진 값 까지 도달할때까지 더한다
            weapon.cur_reload_time += pps / 3

        else:  # 값에 도달하면 재장전 완료
            if weapon.gun_type == 'pistol' or weapon.gun_type == 'smg':
                weapon.pistol_ammo -= (weapon.limit_ammo - weapon.cur_ammo)
                weapon.cur_ammo = weapon.limit_ammo  # 탄창을 갈아 낀다
                if weapon.pistol_ammo < 0:  # 소유 탄약이 탄창 용량보다 부족하면 소유탄약 만큼만 장전한다
                    weapon.cur_ammo += weapon.pistol_ammo
                    weapon.pistol_ammo = 0

            elif weapon.gun_type == 'ar':
                weapon.ar_ammo -= (weapon.limit_ammo - weapon.cur_ammo)
                weapon.cur_ammo = weapon.limit_ammo  # 탄창을 갈아 낀다
                if weapon.ar_ammo < 0:
                    weapon.cur_ammo += weapon.ar_ammo
                    weapon.ar_ammo = 0

            elif weapon.gun_type == 'rifle':
                weapon.rifle_ammo -= (weapon.limit_ammo - weapon.cur_ammo)
                weapon.cur_ammo = weapon.limit_ammo  # 탄창을 갈아 낀다
                if weapon.rifle_ammo < 0:
                    weapon.cur_ammo += weapon.rifle_ammo
                    weapon.rifle_ammo = 0

            elif weapon.gun_type == 'sr':
                weapon.sniper_ammo -= (weapon.limit_ammo - weapon.cur_ammo)
                weapon.cur_ammo = weapon.limit_ammo  # 탄창을 갈아 낀다
                if weapon.sniper_ammo < 0:
                    weapon.cur_ammo += weapon.sniper_ammo
                    weapon.sniper_ammo = 0

            weapon.reload_need = False
            weapon.cur_reload_time = 0
            weapon.reloading = False  # 재장전 상태 해제


def throw_grenade(weapon):
    gren = Grenade(weapon.p, weapon.mp, weapon.p.x, weapon.p.y - weapon.p.cam_h, weapon.p.dir)
    game_manager.add_object(gren, 3)
    weapon.throwable = False
    weapon.throw_delay = get_time()  # 던진 직후부터 쿨타임 측정


def update_throw_delay(weapon):
    if not weapon.throwable:  # 수류탄 던진 후 쿨타임 측정
        weapon.throw_delay_time = get_time() - weapon.throw_delay
        if weapon.throw_delay_time > 29:
            weapon.throwable = True  # 쿨타임이 0이되면 다시 수류탄 활성화