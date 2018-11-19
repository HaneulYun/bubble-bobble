from pico2d import *
import game_framework

import app
import font

name = 'intro'
image_black = None
image_TAITO = None


def enter():
    global image_black
    image_black = load_image('resources\\sprites\\intro_state\\black.png')


def exit():
    pass


def update():
    pass


def draw():
    clear_canvas()
    image_black.draw(app.width * app.scale / 2, app.height * app.scale / 2,
                     app.width * app.scale, app.height * app.scale)
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
