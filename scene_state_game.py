from pico2d import *
import game_framework

import app
import font
import game_world

name = 'scene_state_game'
image_back = None


def enter():
    game_world.init_objects()
    for game_object in game_world.all_objects():
        game_object.enter()


def exit():
    game_world.clear()


def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            for game_object in game_world.all_objects():
                game_object.handle_event(event)


def pause():
    pass


def resume():
    pass
