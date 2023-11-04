from pico2d import *
from config import *
from game_work import game_manager, game_framework

from ui_class.shop import Shop


def handle_events():
    global mx, my, exit_enable
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYUP and event.key == SDLK_TAB:
            exit_enable = True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE or event.key == SDLK_TAB:  # to play_mode
            if exit_enable:
                game_framework.MODE = 'play'
                game_framework.pop_mode()
                hide_cursor()
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, HEIGHT - 1 - event.y


def init():
    global shop, exit_enable
    exit_enable = False
    shop = Shop()
    game_manager.add_object(shop, 7)


def update():
    game_manager.update()


def draw():
    clear_canvas()
    game_manager.render()
    update_canvas()


def finish():
    game_manager.remove_object(shop)
    pass


def pause():
    pass


def resume():
    pass
