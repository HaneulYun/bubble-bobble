from pico2d import *
import game_framework

import app
import font
import scene_state_main

name = 'scene_state_intro'
image_black = None
image_TAITO = None
intro_time = None

TIMER, TAITO = range(2)
state = None


def enter():
    global image_black, image_TAITO, intro_time
    image_black = load_image('resources\\sprites\\intro_state\\black.png')
    image_TAITO = load_image('resources\\sprites\\intro_state\\taito.png')
    intro_time = get_time()


def exit():
    global image_black, image_TAITO
    del image_black, image_TAITO


def update():
    global state
    time = (get_time() - intro_time)
    if time < 5:
        state = TIMER
    elif time < 5.5:
        state = None
    elif time < 7:
        state = TAITO
    else:
        game_framework.change_state(scene_state_main)


def draw():
    clear_canvas()
    image_black.draw(app.width / 2 * app.scale, app.height / 2 * app.scale,
                     app.width * app.scale, app.height * app.scale)

    if state is TIMER:
        font.draw('WAIT A MAMENT ' + str(int(6-(get_time() - intro_time))), app.width / 2, app.height / 2 + 5, font.WHITE, font.MIDDLE)
    elif state is TAITO:
        image_TAITO.draw(app.width / 2 * app.scale, app.height / 2 * app.scale,
                         image_TAITO.w * app.scale, image_TAITO.h * app.scale)
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
