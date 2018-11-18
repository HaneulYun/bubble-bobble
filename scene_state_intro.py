from pico2d import *
import game_framework

import app
import font

name = 'intro'

def enter():
    pass


def exit():
    pass


def update():
    pass


def draw():
    clear_canvas()
    font.draw('TEST!!!', app.width / 2, app.height / 2 + 5, font.GREEN, font.MIDDLE)
    font.draw('S P A C E T E S T', app.width / 2, app.height / 2 - 5, font.GREEN, font.MIDDLE)
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
