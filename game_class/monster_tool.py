from game_class_manager.monster_tool_func import *
from config import *


# 몬스터 스폰 클래스


class Tool:
    def __init__(self, p, weapon, target, mp):
        self.p = p
        self.weapon = weapon
        self.target = target
        self.mp = mp
        self.frame = 0
        self.spawn_time = 0
        self.spawn_point = 0
        self.spawn_point_right = WIDTH / 2 + 2200  # 초기 몬스터 스폰 위치. 플레이어가 움직이면 그에 따라 업데이트 된다.
        self.spawn_point_left = WIDTH / 2 - 2200
        self.point_dir = 0
        self.type = 0
        self.spawn_enable = True  # 해당 변수가 true일때만 스폰
        self.rounds = 1  # 라운드 수
        self.spawn_remain = 5  # 앞으로 스폰할 몬스터 수, 이 변수와 아래의 변수가 동일하지 않으면 라운드가 넘어가지 않는다.
        self.spawn_num = 0  # 스폰된 몬스터 수
        self.limit = 5  # 첫 라운드는 5마리 제한부터 시작하여, 이후 5마리씩 최대 스폰 수가 증가한다.

        self.y, self.speed, self.hp = 0, 0, 0

    def draw(self):
        pass

    def update(self):
        if game_framework.MODE == 'play':
            update_spawn_point(self)
            spawn_monster(self)
            update_timer(self)
            update_rounds(self)

    def handle_events(self):
        pass
