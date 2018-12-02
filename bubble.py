from pico2d import *
import game_framework
import game_world

import app

MOVE_TIMER, DISAPPEAR = range(2)


class ShootState:
    @staticmethod
    def enter(bubble, event):
        bubble.frame = 0
        bubble.timer = get_time()

    @staticmethod
    def exit(bubble, event):
        pass

    @staticmethod
    def do(bubble):
        bubble.frame = bubble.frame + 6 * app.elapsed_time
        if int(bubble.frame) >= 6:
            bubble.add_event(MOVE_TIMER)
        bubble.x += bubble.velocity * 4 * app.elapsed_time
        if app.map[int(bubble.y)][int(bubble.x)] == 1:
            bubble.x -= bubble.velocity * 4 * app.elapsed_time
            bubble.velocity = 0

    @staticmethod
    def draw(bubble):
        if bubble.dir == 1:
            h = ''
        else:
            h = 'h'
        bubble.image.clip_composite_draw(int(bubble.frame) * 24, 2 * 24, 24, 24, 0, h,
                                         bubble.x * 8 * app.scale, (bubble.y * 8 + 14.5) * app.scale,
                                         24 * app.scale, 24 * app.scale)


class MoveState:
    @staticmethod
    def enter(bubble, event):
        bubble.frame = 0
        bubble.timer = get_time()

    @staticmethod
    def exit(bubble, event):
        pass

    @staticmethod
    def do(bubble):
        dir = app.map[int(bubble.y)][int(bubble.x)]
        if dir == 2:
            bubble.x += 2 * app.elapsed_time
        elif dir == 3:
            bubble.y -= 2 * app.elapsed_time
        elif dir == 4:
            bubble.x -= 2 * app.elapsed_time
        elif dir == 5 or dir == 1:
            bubble.y += 2 * app.elapsed_time

    @staticmethod
    def draw(bubble):
        if bubble.dir == 1:
            h = ''
        else:
            h = 'h'
        bubble.image.clip_composite_draw(6 * 24, 2 * 24, 24, 24, 0, h,
                                         bubble.x * 8 * app.scale, (bubble.y * 8 + 14.5) * app.scale,
                                         24 * app.scale, 24 * app.scale)


class DisappearState:
    @staticmethod
    def enter(bubble, event):
        bubble.frame = 0

    @staticmethod
    def exit(bubble, event):
        pass

    @staticmethod
    def do(bubble):
        bubble.frame = (bubble.frame + 8 * app.elapsed_time)
        if bubble.frame >= 6:
            game_world.remove_object(bubble)

    @staticmethod
    def draw(bubble):
        if bubble.dir == 1:
            h = ''
        else:
            h = 'h'

        if bubble.frame < 2:
            frame_x, frame_y = int(2 + bubble.frame), 1
        elif bubble.frame < 6:
            frame_x, frame_y = int(bubble.frame - 2), 0
        else:
            pass

        if not bubble.frame > 6:
            bubble.image.clip_composite_draw(frame_x * 24, frame_y * 24, 24, 24, 0, h,
                                             bubble.x * 8 * app.scale, (bubble.y * 8 + 10) * app.scale,
                                             24 * app.scale, 24 * app.scale)


next_state_table = {
    ShootState: {MOVE_TIMER: MoveState},
    MoveState: {DISAPPEAR: DisappearState}
}


class Bubble:
    image = None

    def __init__(self, x, y, velocity):
        if Bubble.image is None:
            Bubble.image = load_image('resources\\sprites\\game_state\\Bubble.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.cur_state = ShootState
        self.dir = 1
        self.frame = 0
        self.event_que = []
        self.cur_frame_per_action = 0
        self.cur_state.enter(self, None)

    def get_bb(self):
        return self.x - 1.2, self.y + 0.5, self.x + 1.2, self.y + 3

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle((self.x - 1.2) * 8 * app.scale, (self.y + 1.5 - 1) * 8 * app.scale,
                       (self.x + 1.2) * 8 * app.scale, (self.y + 1.5 + 1.5) * 8 * app.scale)

    def handle_event(self, event):
        pass
