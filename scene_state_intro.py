from pico2d import *
import game_framework


def enter():
    pass


def exit():
    pass


def update():
    pass


def draw():
    clear_canvas()
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()


def pause(): pass


def resume(): pass
