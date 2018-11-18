from pico2d import *
import game_framework

import font


def enter():
    pass


def exit():
    pass


def update():
    pass


def draw():
    clear_canvas()
    font.draw('TEST!!!', 160 * game_framework.windowScale, 120 * game_framework.windowScale)
    font.draw('S P A C E T E S T', 150 * game_framework.windowScale, 100 * game_framework.windowScale)
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()


def pause():
    pass


def resume():
    pass
