from pico2d import *
import game_framework

import app
import font

name = 'scene_state_selection'
image_back = None
image_player = None
back_scroll = None


def enter():
    global image_back, image_player, back_scroll
    image_back = load_image('resources\\sprites\\lobby_state\\background.png')
    image_player = load_image('resources\\sprites\\selection_state\\selection.png')
    back_scroll = 0.0


def exit():
    global image_back, image_player
    del image_back, image_player


def update():
    global back_scroll
    back_scroll = (back_scroll + 0.3) % app.height


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


def pause():
    pass


def resume():
    pass
