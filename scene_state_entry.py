from pico2d import *
import game_framework

import app
import font

name = 'scene_state_entry'
image_back = None


def enter():
    global image_back
    image_back = load_image('resources\\sprites\\entry_state\\background.png')


def exit():
    global image_back
    del image_back


def update():
    pass


def draw():
    clear_canvas()
    image_back.draw(app.width / 2 * app.scale, app.height / 2 * app.scale,
                    app.width * app.scale, app.height * app.scale)
    font.draw(' THE NEW ADVENTURE OF', app.width / 2, 200, font.GREEN, 0.5)
    font.draw('@BUBBLE BOBBLE\"', app.width / 2, 200 - 16, font.GREEN, 0.5)
    font.draw('- THE NEXT GENERATION -', app.width / 2, 200 - 32, font.GREEN, 0.5)


    font.draw_to_origin('LET^ TRY AND CHALLENGE!', app.width / 2, 40, font.WHITE, 0.5)
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
