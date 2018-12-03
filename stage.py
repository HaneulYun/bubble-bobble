from pico2d import *

import game_framework
import game_world

import app
import font

import scene_state_game
import scene_state_score

from monster_zen_chan import ZenChan


def build_stage(url):
    app.map = []
    f = open(url, 'r')
    while True:
        mode = f.readline()
        if mode == '':
            break
        elif mode[0] == 'u':
            app.num_monster += 1
            x = float(f.readline())
            y = float(f.readline())
            type = float(f.readline())
            if type == 1:
                game_world.add_object(ZenChan(x, y), 2)
        elif mode[0] == 'm':
            lines = f.readlines()
            tmp = [i.split() for i in lines]
            for i in tmp:
                app.map = [[int(j) for j in i]] + app.map
        else:
            break
    f.close()


class Stage:
    def __init__(self):
        self.image = load_image('resources\\sprites\\game_state\\stage.png')
        self.stage = app.stage

    def update(self):
        if app.num_monster == 0:
            app.stage += 1
            if app.stage > app.max_stage:
                game_framework.change_state(scene_state_score)
            else:
                game_framework.change_state(scene_state_game)

    def draw(self):
        if self.stage is 1:
            self.image.clip_draw_to_origin(760, 0, 512, 112, 0, (app.height - 112) * app.scale,
                                           512 * app.scale, 112 * app.scale)
            self.image.clip_draw_to_origin(440, 0, 320, 219, 0, 0, 320 * app.scale, 219 * app.scale)
        elif 2 <= self.stage <= 7:
            self.image.clip_draw(440, 219, 352, 224, app.width / 2 * app.scale, app.height / 2 * app.scale,
                                 352 * app.scale, 224 * app.scale)
            self.image.clip_draw(792, 219, 320, 188, app.width / 2 * app.scale, (app.height / 2 - 18) * app.scale,
                                 320 * app.scale, 188 * app.scale)

        self.image.clip_draw_to_origin(0, (self.stage - 1) * 208, 320, 208, 0, 0, 320 * app.scale, 208 * app.scale)

        self.image.clip_draw_to_origin(760 + 5, 112, 1, 1,
                                       0, (app.height - 16) * app.scale, app.width * app.scale, app.height * app.scale)
        font.draw('HIGH SCORE', app.width / 2 + 4, app.height - 4, font.PINK, 0.5)
        font.draw(str(app.best_score), app.width / 2 + 44, app.height - 12, font.WHITE, 1)

        font.draw('1UP', app.width / 2 - 88, app.height - 4, font.GREEN, 0.5)
        font.draw(str(app.score), app.width / 2 - 60, app.height - 12, font.WHITE, 1)

    def handle_event(self, event):
        pass
