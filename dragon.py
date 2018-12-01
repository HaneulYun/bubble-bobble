from pico2d import *
import game_framework

import app

MPS = 1
DRAGON_SPEED_MPS = 5

LEFT_DOWN, LEFT_UP, RIGHT_DOWN, RIGHT_UP, SLEEP_TIMER, JUMP, DROP, ATTACK = range(8)

key_event_table = {
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYDOWN, SDLK_s): JUMP,
    (SDL_KEYDOWN, SDLK_a): ATTACK,
}

class IdleState:
    @staticmethod
    def enter(dragon, event):
        if event == LEFT_DOWN:
            dragon.velocity -= DRAGON_SPEED_MPS
        elif event == RIGHT_DOWN:
            dragon.velocity += DRAGON_SPEED_MPS
        elif event == LEFT_UP:
            dragon.velocity += DRAGON_SPEED_MPS
        elif event == RIGHT_UP:
            dragon.velocity -= DRAGON_SPEED_MPS

        if dragon.velocity < 0:
            dragon.dir = -1
        elif dragon.velocity > 0:
            dragon.dir = 1

    @staticmethod
    def exit(dragon, event):
        pass

    @staticmethod
    def do(dragon):
        dragon.frame = (dragon.frame + 2 * app.elapsed_time) % 2

    @staticmethod
    def draw(dragon):
        if dragon.dir == 1:
            h = ''
        else:
            h = 'h'

        dragon.image.clip_composite_draw(int(dragon.frame) * 25, 0 * 25, 25, 25, 0, h,
                                         dragon.x * 8 * app.scale, (dragon.y * 8 + 14.5) * app.scale,
                                         25 * app.scale, 25 * app.scale)


class MoveState:
    @staticmethod
    def enter(dragon, event):
        if event == LEFT_DOWN:
            dragon.velocity -= DRAGON_SPEED_MPS
        elif event == RIGHT_DOWN:
            dragon.velocity += DRAGON_SPEED_MPS
        elif event == LEFT_UP:
            dragon.velocity += DRAGON_SPEED_MPS
        elif event == RIGHT_UP:
            dragon.velocity -= DRAGON_SPEED_MPS

        if dragon.velocity < 0:
            dragon.dir = -1
        elif dragon.velocity > 0:
            dragon.dir = 1

        dragon.frame = 0

    @staticmethod
    def exit(dragon, event):
        pass

    @staticmethod
    def do(dragon):
        dragon.frame = (dragon.frame + 6 * app.elapsed_time) % 6

        if dragon.velocity < 0:
            # if not main_state.stage.map[int(dragon.y)][int(dragon.x - 1.5)]:
            dragon.x += dragon.velocity * app.elapsed_time  # * game_framework.frame_time
        elif dragon.velocity > 0:
            # if not main_state.stage.map[int(dragon.y)][int(dragon.x + 1.5)]:
            dragon.x += dragon.velocity * app.elapsed_time # * game_framework.frame_time

    @staticmethod
    def draw(dragon):
        if dragon.dir == 1:
            h = ''
        else:
            h = 'h'

        dragon.image.clip_composite_draw(int(dragon.frame) * 25, 1 * 25, 25, 25, 0, h,
                                         dragon.x * 8 * app.scale, (dragon.y * 8 + 14.5) * app.scale,
                                         25 * app.scale, 25 * app.scale)


class JumpState:
    @staticmethod
    def enter(dragon, event):
        pass

    @staticmethod
    def exit(dragon, event):
        pass

    @staticmethod
    def do(dragon):
        pass

    @staticmethod
    def draw(dragon):
        pass


class DropState:
    @staticmethod
    def enter(dragon, event):
        pass

    @staticmethod
    def exit(dragon, event):
        pass

    @staticmethod
    def do(dragon):
        pass

    @staticmethod
    def draw(dragon):
        pass


class SleepState:
    @staticmethod
    def enter(dragon, event):
        pass

    @staticmethod
    def exit(dragon, event):
        pass

    @staticmethod
    def do(dragon):
        pass

    @staticmethod
    def draw(dragon):
        pass


next_state_table = {
    IdleState: {LEFT_DOWN: MoveState, LEFT_UP: MoveState, RIGHT_DOWN: MoveState, RIGHT_UP: MoveState,
                SLEEP_TIMER: SleepState, JUMP: IdleState, DROP: IdleState, ATTACK: IdleState},
    MoveState: {LEFT_DOWN: IdleState, LEFT_UP: IdleState, RIGHT_DOWN: IdleState, RIGHT_UP: IdleState,
                SLEEP_TIMER: MoveState, JUMP: MoveState, DROP: MoveState, ATTACK: MoveState}
}


class Dragon:
    def __init__(self):
        self.x, self.y = 3.5, 1
        self.image = load_image('resources\\sprites\\game_state\\dragon.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def fire_bubble(self):
        pass

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

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
