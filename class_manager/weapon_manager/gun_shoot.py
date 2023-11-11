from class_manager.weapon_manager.etc import make_shell
from config import FLAME_DISPLAY_TIME


def shoot_gun(weapon):
    if weapon.trigger and weapon.weapon_type == 0:
        if weapon.shoot_delay <= 0:  # 딜레이는 총마다 다르며, 딜레이 수치가 낮을수록 연사 속도가 빠르다. 0이 될 때마다 발사된다.
            # True일시 해당 값을 Target 클래스로 전달하여 Target 클래스의 recoil을 증가시킨다.
            weapon.shoot = True

            if weapon.gun == 'SCAR_H':
                weapon.shoot_delay = 38
                weapon.p.shake_range = 17

            elif weapon.gun == 'M16':
                weapon.shoot_delay = 28
                weapon.p.shake_range = 15

            elif weapon.gun == 'MP44':
                weapon.shoot_delay = 60
                weapon.p.shake_range = 20

            elif weapon.gun == 'AUG':
                weapon.shoot_delay = 32
                weapon.p.shake_range = 15

            elif weapon.gun == 'GROZA':
                weapon.shoot_delay = 26
                weapon.p.shake_range = 15

            elif weapon.gun == 'AKS74':
                weapon.shoot_delay = 28
                weapon.p.shake_range = 10

            elif weapon.gun == 'UMP':
                weapon.shoot_delay = 35
                weapon.p.shake_range = 13

            elif weapon.gun == 'VECTOR':
                weapon.shoot_delay = 15
                weapon.p.shake_range = 10

            elif weapon.gun == 'THOMPSON':
                weapon.shoot_delay = 31
                weapon.p.shake_range = 16

            elif weapon.gun == 'P90':
                weapon.shoot_delay = 24
                weapon.p.shake_range = 15

            elif weapon.gun == 'M1':  # 반자동 소총이므로 연사 딜레이를 무한대로 부여함
                weapon.shoot_delay = 220
                weapon.p.shake_range = 30

            elif weapon.gun == 'WIN':
                weapon.shoot_delay = 310
                weapon.p.shake_range = 40
                weapon.is_spin = True
                weapon.flame_display_time = FLAME_DISPLAY_TIME

            elif weapon.gun == 'MINI14':
                weapon.shoot_delay = 140
                weapon.p.shake_range = 25

            elif weapon.gun == 'FAL':
                weapon.shoot_delay = 180
                weapon.p.shake_range = 30

            elif weapon.gun == 'LVOAS':
                if weapon.shoot_count < 1:
                    weapon.shoot_delay = 25
                    weapon.p.shake_range = 15
                    weapon.shoot_count += 1
                else:
                    weapon.shoot_delay = 120
                    weapon.p.shake_range = 20
                    weapon.shoot_count = 0

            elif weapon.gun == 'AWP':
                if weapon.zoom:  # 정조준 시에만 발사 가능
                    weapon.shoot_delay = 550
                    weapon.p.shake_range = 70
                    weapon.flame_display_time = FLAME_DISPLAY_TIME

            # 일부 총기는 장전 시 탄피를 배출하므로 예외 처리
            if not weapon.gun == 'AWP' and not weapon.gun == 'WIN':  # 총 종류에 따라 탄피 크기가 다르다
                if weapon.gun_type == 'smg':
                    make_shell(weapon)

                elif weapon.gun_type == 'ar':
                    make_shell(weapon, 18, 18)

                elif weapon.gun_type == 'rifle':
                    if weapon.gun == 'MINI14':  # mini14는 5.56mm보통탄을 쓰므로 예외
                        make_shell(weapon, 18, 18)
                    else:
                        make_shell(weapon, 20, 20)

                weapon.flame_display_time = FLAME_DISPLAY_TIME

            if weapon.gun == 'VECTOR':
                weapon.flame_display_time = 6

        else:
            weapon.shoot = False
