from pico2d import *

import app
import font


class Stage:
    def __init__(self):
        self.image = load_image('resources\\sprites\\game_state\\stage.png')
        self.stage = app.stage

    def update(self):
        pass

    def draw(self):
        if self.stage is 1:
            self.image.clip_draw_to_origin(760, 0, 512, 112, 0, (app.height - 112) * app.scale,
                                           512 * app.scale, 112 * app.scale)
            self.image.clip_draw_to_origin(440, 0, 320, 219, 0, 0, 320 * app.scale, 219 * app.scale)
        elif 2 <= self.stage <= 7:
            pass

        self.image.clip_draw_to_origin(0, (self.stage - 1) * 208, 320, 208, 0, 0, 320 * app.scale, 208 * app.scale)

        self.image.clip_draw_to_origin(760 + 5, 112, 1, 1,
                                       0, (app.height - 16) * app.scale, app.width * app.scale, app.height * app.scale)
        font.draw('HIGH SCORE', app.width / 2 + 4, app.height - 4, font.PINK, 0.5)

    def handle_event(self, event):
        pass
