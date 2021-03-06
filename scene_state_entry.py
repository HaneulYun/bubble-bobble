from pico2d import *
import game_framework

import app
import font
import scene_state_game

name = 'scene_state_entry'
image_back = None


def enter():
    global image_back
    image_back = load_image('resources\\sprites\\entry_state\\background.png')
    app.stage = 1
    app.best_score = 30000
    app.score = 0
    app.entry_time = get_time()
    app.ranking = []
    with open('ranking.txt', 'r') as f:
        app.ranking = json.load(f)


def exit():
    global image_back
    del image_back
    if app.bgm != None:
        app.bgm.stop()
    app.bgm = load_music('resources\\bgm\\game.mp3')
    app.bgm.repeat_play()


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
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
                game_framework.change_state(scene_state_game)


def pause():
    pass


def resume():
    pass
