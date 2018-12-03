from pico2d import *
import game_framework
import game_world

import random
import app

item_info = {
    0: (0, 0, 10),
    1: (1, 0, 20),
    2: (2, 0, 30),
    3: (3, 0, 50),
    4: (4, 0, 60),
    5: (5, 0, 70),
    6: (6, 0, 80),
    7: (7, 0, 90),
    8: (8, 0, 100),
    9: (9, 0, 150),
    10: (10, 0, 200),
    11: (11, 0, 250),
    12: (12, 0, 300),
    13: (13, 0, 350),
    14: (14, 0, 400),
    15: (15, 0, 450),
    16: (16, 0, 500),
    17: (17, 0, 550),
    18: (18, 0, 600),
    19: (19, 0, 650),
    20: (20, 0, 700)
}


class Item:
    image = None

    def __init__(self, x, y, dir, type):
        if Item.image is None:
            Item.image = load_image('resources\\sprites\\game_state\\items.png')
        self.x, self.y = x, y
        self.dir = dir
        type = random.randint(0, 20)
        self.type_x, self.type_y, self.type_score = item_info[type][0], item_info[type][1], item_info[type][2]

    def get_bb(self):
        return self.x - 1, self.y + 0.2, self.x + 1, self.y + 2.2

    def update(self):
        pass

    def draw(self):
        if self.dir == 1:
            h = ''
        else:
            h = 'h'
        self.image.clip_composite_draw(self.type_x * 16, self.type_y * 16, 16, 16, 0, h,
                                       self.x * 8 * app.scale, (self.y + 1.2) * 8 * app.scale,
                                       16 * app.scale, 16 * app.scale)
        draw_rectangle((self.x - 1) * 8 * app.scale, (self.y + 2.2) * 8 * app.scale,
                       (self.x + 1) * 8 * app.scale, (self.y + 0.2) * 8 * app.scale)

    def handle_event(self, event):
        pass
