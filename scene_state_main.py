from pico2d import *
import game_framework

import app
import font

name = 'intro'
image_black = None


def enter():
    global image_black
    image_black = load_image('resources\\sprites\\intro_state\\black.png')


def exit():
    global image_black
    del image_black


def update():
    pass


def draw():
    clear_canvas()
    image_black.draw(app.width / 2 * app.scale, app.height / 2 * app.scale,
                     app.width * app.scale, app.height * app.scale)
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
