from pico2d import *
import game_framework

import app
import font
import scene_state_entry

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


    image_player.clip_draw_to_origin(0, 0, 26, 22,
                                     16 * app.scale, (app.height / 2 - 35 + 16) * app.scale,
                                     26 * app.scale, 22 * app.scale)
    font.draw_to_origin('THE MOST', 8, app.height / 2 - 32 - 0, font.WHITE)
    font.draw_to_origin('AVERAGE', 8, app.height / 2 - 32 - 8, font.WHITE)
    font.draw_to_origin('ONE OF', 8, app.height / 2 - 32 - 16, font.WHITE)
    font.draw_to_origin('THE BUNCH', 8, app.height / 2 - 32 - 24, font.WHITE)

    image_player.clip_draw_to_origin(26, 0, 26, 22,
                                     (app.width * 0.5 - 64) * app.scale, (app.height / 2 - 35 + 16) * app.scale,
                                     26 * app.scale, 22 * app.scale)
    font.draw_to_origin('THE', app.width * 0.5 - 64, app.height / 2 - 32 - 0, font.WHITE)
    font.draw_to_origin('FASTEST', app.width * 0.5 - 64, app.height / 2 - 32 - 8, font.WHITE)
    font.draw_to_origin('ONE OF', app.width * 0.5 - 64, app.height / 2 - 32 - 16, font.WHITE)
    font.draw_to_origin('THE FOUR', app.width * 0.5 - 64, app.height / 2 - 32 - 24, font.WHITE)

    image_player.clip_draw_to_origin(52, 0, 26, 22,
                                     (app.width * 0.5 + 16) * app.scale, (app.height / 2 - 35 + 16) * app.scale,
                                     26 * app.scale, 22 * app.scale)
    font.draw_to_origin('THE ONE', app.width * 0.5 + 8, app.height / 2 - 32 - 0, font.WHITE)
    font.draw_to_origin('WHOSE', app.width * 0.5 + 8, app.height / 2 - 32 - 8, font.WHITE)
    font.draw_to_origin('BUBBLES', app.width * 0.5 + 8, app.height / 2 - 32 - 16, font.WHITE)
    font.draw_to_origin('FLOAT THE', app.width * 0.5 + 8, app.height / 2 - 32 - 24, font.WHITE)
    font.draw_to_origin('FURTHEST', app.width * 0.5 + 8, app.height / 2 - 32 - 32, font.WHITE)

    image_player.clip_draw_to_origin(78, 0, 26, 22,
                                     (app.width - 64) * app.scale, (app.height / 2 - 35 + 16) * app.scale,
                                     26 * app.scale, 22 * app.scale)
    font.draw_to_origin('THE ONE', app.width - 64, app.height / 2 - 32 - 0, font.WHITE)
    font.draw_to_origin('WHOSE', app.width - 64, app.height / 2 - 32 - 8, font.WHITE)
    font.draw_to_origin('BUBBLES', app.width - 64, app.height / 2 - 32 - 16, font.WHITE)
    font.draw_to_origin('FLY THE', app.width - 64, app.height / 2 - 32 - 24, font.WHITE)
    font.draw_to_origin('FASTEST', app.width - 64, app.height / 2 - 32 - 323, font.WHITE)

    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
                game_framework.change_state(scene_state_entry)


def pause():
    pass


def resume():
    pass
