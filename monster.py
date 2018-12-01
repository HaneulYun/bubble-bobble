from pico2d import *

import app

MPS = 1
MONSTER_SPEED_MPS = 6

LEFT, RIGHT, JUMP, DROP, NONE = range(5)


class IdleState:
    @staticmethod
    def enter(monster, event):
        monster.frame = 0

    @staticmethod
    def exit(monster, event):
        pass

    @staticmethod
    def do(monster):
        monster.frame = (monster.frame + 2 * app.elapsed_time) % 2
        if app.map[int(monster.y - 1)][int(monster.x)] != 1:
            monster.add_event(DROP)

    @staticmethod
    def draw(monster):
        if monster.dir == 1:
            h = ''
        else:
            h = 'h'
        monster.image.clip_composite_draw(int(monster.frame) * 32, 1 * 32, 32, 32, 0, h,
                                          monster.x * 8 * app.scale, (monster.y * 8 + 18.5) * app.scale,
                                          32 * app.scale, 32 * app.scale)


class MoveState:
    @staticmethod
    def enter(monster, event):
        monster.frame = 0

    @staticmethod
    def exit(monster, event):
        pass

    @staticmethod
    def do(monster):
        monster.frame = (monster.frame + 10 * app.elapsed_time) % 6
        if monster.velocity < 0:
            monster.x += monster.velocity * app.elapsed_time
        elif monster.velocity > 0:
            monster.x += monster.velocity * app.elapsed_time
        if app.map[int(monster.y - 1)][int(monster.x)] != 1:
            monster.add_event(DROP)

    @staticmethod
    def draw(monster):
        if monster.dir == 1:
            h = ''
        else:
            h = 'h'
        monster.image.clip_composite_draw(int(monster.frame) * 32, 1 * 32, 32, 32, 0, h,
                                          monster.x * 8 * app.scale, (monster.y * 8 + 18.5) * app.scale,
                                          32 * app.scale, 32 * app.scale)


class JumpState:
    @staticmethod
    def enter(monster, event):
        monster.frame = 0
        if monster.rest_jump_volume == 0:
            monster.rest_jump_volume = 5.5

    @staticmethod
    def exit(monster, event):
        pass

    @staticmethod
    def do(monster):
        monster.frame = (monster.frame + 4 * app.elapsed_time) % 4

        if monster.velocity < 0:
            monster.x += monster.velocity * app.elapsed_time
        elif monster.velocity > 0:
            monster.x += monster.velocity * app.elapsed_time

        if monster.rest_jump_volume > 0:
            delta = MONSTER_SPEED_MPS * app.elapsed_time
            monster.y += delta
            monster.rest_jump_volume -= delta
            if monster.rest_jump_volume < 0:
                monster.y += monster.rest_jump_volume
                monster.rest_jump_volume = 0
                monster.add_event(DROP)

    @staticmethod
    def draw(monster):
        if monster.dir == 1:
            h = ''
        else:
            h = 'h'
        monster.image.clip_composite_draw(int(monster.frame) * 32, 2 * 32, 32, 32, 0, h,
                                          monster.x * 8 * app.scale, (monster.y * 8 + 18.5) * app.scale,
                                          32 * app.scale, 32 * app.scale)

class DropState:
    @staticmethod
    def enter(monster, event):
        monster.frame = 0

    @staticmethod
    def exit(monster, event):
        pass

    @staticmethod
    def do(monster):
        monster.frame = (monster.frame + 4 * app.elapsed_time) % 4

        if monster.velocity < 0:
            monster.x += monster.velocity * app.elapsed_time
        elif monster.velocity > 0:
            monster.x += monster.velocity * app.elapsed_time

        delta = MONSTER_SPEED_MPS * app.elapsed_time

        if app.map[int(monster.y)][int(monster.x)] != 1 and app.map[int(monster.y - delta)][int(monster.x)] == 1:
            monster.y = int(monster.y)
            monster.add_event(NONE)
        else:
            monster.y -= delta

    @staticmethod
    def draw(monster):
        if monster.dir == 1:
            h = ''
        else:
            h = 'h'
        monster.image.clip_composite_draw(int(monster.frame) * 32, 3 * 32, 32, 32, 0, h,
                                          monster.x * 8 * app.scale, (monster.y * 8 + 18.5) * app.scale,
                                          32 * app.scale, 32 * app.scale)


next_state_table = {
    IdleState: {LEFT: MoveState, RIGHT: MoveState, JUMP: JumpState, DROP: DropState},
    MoveState: {LEFT: MoveState, RIGHT: MoveState, JUMP: JumpState, DROP: DropState},
    JumpState: {LEFT: MoveState, RIGHT: MoveState, JUMP: JumpState, DROP: DropState},
    DropState: {LEFT: MoveState, RIGHT: MoveState, JUMP: JumpState, DROP: DropState, NONE: IdleState}
}


class Monster:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.image = None
        self.dir = 1
        self.velocity = 0
        self.frame = 0

        self.rest_jump_volume = 0

        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

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
        draw_rectangle((self.x - 1.2) * 8 * app.scale, (self.y * 8 + 18.5 - 16.5) * app.scale,
                       (self.x + 1.2) * 8 * app.scale, (self.y * 8 + 18.5 + 10) * app.scale)

    def handle_event(self, event):
        pass
