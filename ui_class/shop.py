from ui_manager.shop_manager import *


class Shop:
    def __init__(self):
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.button_x = []
        self.button_y = []
        self.window_y = -500
        self.mx = 0
        self.my = 0
        self.click = False  # 마우스 누름 여부
        self.select_mode = 0  # 초기값 총 선택
        self.cat_x = []
        self.cat_y = []

        load_shop_resource(self)
        make_button_pos(self)

    def draw(self):
        draw_shop_window(self)
        draw_items(self)

    def update(self):
        calc_pps()
        window_animation(self)
        update_cat_button(self)
        if self.click:
            click_button(self)

    def handle_event(self):
        pass
