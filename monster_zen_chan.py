from pico2d import *
import monster


class ZenChan(monster.Monster):
    image = None

    def __init__(self, x, y):
        super().__init__(x, y)
        if ZenChan.image is None:
            ZenChan.image = load_image('resources\\sprites\\game_state\\mon_zen-chan.png')
        self.image = ZenChan.image
