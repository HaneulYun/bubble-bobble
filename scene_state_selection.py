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
    image_player = load_image('resources\\sprites\\lobby_state\\player.png')
    back_scroll = 0.0


def exit():
    global image_back, image_player
    del image_back, image_player


def update():
    global back_scroll
    back_scroll = (back_scroll + 0.3) % app.height


def draw():
    clear_canvas()
    image_back.draw_to_origin(-back_scroll * app.scale, back_scroll * app.scale,
                              app.width * app.scale, app.height * app.scale)
    image_back.draw_to_origin((-back_scroll + app.width) * app.scale, back_scroll * app.scale,
                              app.width * app.scale, app.height * app.scale)
    image_back.draw_to_origin(-back_scroll * app.scale, (back_scroll - app.height / 7 * 6) * app.scale,
                              app.width * app.scale, app.height * app.scale)
    image_back.draw_to_origin((-back_scroll + app.width) * app.scale, (back_scroll - app.height / 7 * 6) * app.scale,
                              app.width * app.scale, app.height * app.scale)
    image_back.draw_to_origin(-back_scroll * app.scale, (back_scroll - app.height / 7 * 12) * app.scale,
                              app.width * app.scale, app.height * app.scale)
    image_back.draw_to_origin((-back_scroll + app.width) * app.scale, (back_scroll - app.height / 7 * 12) * app.scale,
                              app.width * app.scale, app.height * app.scale)

    font.draw('THE MOST', 8, app.height / 2 - 32 - 0, font.WHITE)
    font.draw('AVERAGE', 8, app.height / 2 - 32 - 8, font.WHITE)
    font.draw('ONE OF', 8, app.height / 2 - 32 - 16, font.WHITE)
    font.draw('THE BUNCH', 8, app.height / 2 - 32 - 24, font.WHITE)

    font.draw('THE', app.width * 0.5 - 64, app.height / 2 - 32 - 0, font.WHITE)
    font.draw('FASTEST', app.width * 0.5 - 64, app.height / 2 - 32 - 8, font.WHITE)
    font.draw('ONE OF', app.width * 0.5 - 64, app.height / 2 - 32 - 16, font.WHITE)
    font.draw('THE FOUR', app.width * 0.5 - 64, app.height / 2 - 32 - 24, font.WHITE)

    font.draw('THE ONE', app.width * 0.5 + 8, app.height / 2 - 32 - 0, font.WHITE)
    font.draw('WHOSE', app.width * 0.5 + 8, app.height / 2 - 32 - 8, font.WHITE)
    font.draw('BUBBLES', app.width * 0.5 + 8, app.height / 2 - 32 - 16, font.WHITE)
    font.draw('FLOAT THE', app.width * 0.5 + 8, app.height / 2 - 32 - 24, font.WHITE)
    font.draw('FURTHEST', app.width * 0.5 + 8, app.height / 2 - 32 - 32, font.WHITE)

    font.draw('THE ONE', app.width - 64, app.height / 2 - 32 - 0, font.WHITE)
    font.draw('WHOSE', app.width - 64, app.height / 2 - 32 - 8, font.WHITE)
    font.draw('BUBBLES', app.width - 64, app.height / 2 - 32 - 16, font.WHITE)
    font.draw('FLY THE', app.width - 64, app.height / 2 - 32 - 24, font.WHITE)
    font.draw('FASTEST', app.width - 64, app.height / 2 - 32 - 323, font.WHITE)

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
