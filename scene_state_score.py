from pico2d import *
import game_framework

import app
import font
import scene_state_main

name = 'scene_state_score'
image_back = None
image_player = None


def enter():
    global image_back, image_player
    image_back = load_image('resources\\sprites\\lobby_state\\background.png')
    image_player = load_image('resources\\sprites\\lobby_state\\player.png')


def exit():
    global image_back, image_player
    del image_back, image_player


def update():
    pass


def draw():
    clear_canvas()
    image_back.draw(app.width / 2 * app.scale, app.height / 2 * app.scale,
               app.width * app.scale, app.height * app.scale)

    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
                game_framework.change_state(scene_state_main)


def pause():
    pass


def resume():
    pass
