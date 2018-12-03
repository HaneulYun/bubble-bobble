from pico2d import *
import game_framework
import game_world

import app
from bubble import Bubble
from item import Item
import bubble
import monster

import scene_state_score

MPS = 1
DRAGON_SPEED_MPS = 6

LEFT_DOWN, LEFT_UP, RIGHT_DOWN, RIGHT_UP, SLEEP_TIMER, JUMP, DROP, ATTACK, NONE = range(9)

key_event_table = {
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYDOWN, SDLK_s): JUMP,
    (SDL_KEYDOWN, SDLK_a): ATTACK,
}


def update_velocity(dragon, event):
    if event == LEFT_DOWN:
        dragon.velocity -= DRAGON_SPEED_MPS
        if not dragon.input_left_safe:
            dragon.input_left_safe = 1
    elif event == RIGHT_DOWN:
        dragon.velocity += DRAGON_SPEED_MPS
        if not dragon.input_right_safe:
            dragon.input_right_safe = 1
    elif event == LEFT_UP:
        if dragon.input_left_safe:
            dragon.velocity += DRAGON_SPEED_MPS
        else:
            dragon.input_left_safe = 1
            dragon.cur_state = IdleState
    elif event == RIGHT_UP:
        if dragon.input_right_safe:
            dragon.velocity -= DRAGON_SPEED_MPS
        else:
            dragon.input_right_safe = 1
            dragon.cur_state = IdleState

    if dragon.velocity < 0:
        dragon.dir = -1
    elif dragon.velocity > 0:
        dragon.dir = 1


def update_enter(dragon, event):
    if not dragon.attack:
        dragon.frame = 0


def update_attack(dragon, event):
    if event == ATTACK:
        dragon.fire_bubble()


def update_attack_frame(dragon):
    dragon.frame = (dragon.frame + 15 * app.elapsed_time)
    if dragon.frame >= 4:
        dragon.attack = 0
        dragon.frame = 0


def update_move(dragon):
    delta = dragon.velocity * app.elapsed_time
    if dragon.y > 25:
        pass
    elif app.map[int(dragon.y)][int(dragon.x + dragon.dir)] != 1 and \
            app.map[int(dragon.y)][int(dragon.x + dragon.dir + delta)] == 1:
        delta = 0
    elif dragon.x - 1 + delta < 2 or dragon.x + 1 + delta > 38:
        delta = 0
    dragon.x += delta


def update_jump(dragon):
    if dragon.rest_jump_volume > 0:
        delta = DRAGON_SPEED_MPS * app.elapsed_time
        dragon.y += delta
        dragon.rest_jump_volume -= delta
        if dragon.rest_jump_volume < 0:
            dragon.y += dragon.rest_jump_volume
            dragon.rest_jump_volume = 0
            dragon.add_event(DROP)


def update_drop(dragon):
    delta = DRAGON_SPEED_MPS * app.elapsed_time
    if dragon.y > 25:
        dragon.y -= delta
    elif app.map[int(dragon.y)][int(dragon.x)] != 1 and app.map[int(dragon.y - delta)][int(dragon.x)] == 1:
        dragon.y = int(dragon.y)
        dragon.add_event(NONE)
    else:
        dragon.y -= delta
        if dragon.y < -2.5:
            dragon.y = 28


def draw_image(dragon, motion):
    if dragon.dir == 1:
        h = ''
    else:
        h = 'h'
    if dragon.attack:
        frame = int(dragon.frame + 4)
    else:
        frame = int(dragon.frame)

    if dragon.attack and (dragon.cur_state == IdleState or dragon.cur_state == MoveState):
        dragon.image.clip_composite_draw(frame * 25, 0 * 25, 25, 25, 0, h,
                                         dragon.x * 8 * app.scale, (dragon.y * 8 + 14.5) * app.scale,
                                         25 * app.scale, 25 * app.scale)
    else:
        dragon.image.clip_composite_draw(frame * 25, motion * 25, 25, 25, 0, h,
                                         dragon.x * 8 * app.scale, (dragon.y * 8 + 14.5) * app.scale,
                                         25 * app.scale, 25 * app.scale)


class IdleState:
    @staticmethod
    def enter(dragon, event):
        update_velocity(dragon, event)
        update_enter(dragon, event)

    @staticmethod
    def exit(dragon, event):
        update_attack(dragon, event)

    @staticmethod
    def do(dragon):
        if dragon.attack:
            update_attack_frame(dragon)
        else:
            dragon.frame = (dragon.frame + 2 * app.elapsed_time) % 2

        if app.map[int(dragon.y - 1)][int(dragon.x)] != 1:
            dragon.add_event(DROP)

    @staticmethod
    def draw(dragon):
        draw_image(dragon, 0)


class MoveState:
    @staticmethod
    def enter(dragon, event):
        update_velocity(dragon, event)
        update_enter(dragon, event)

    @staticmethod
    def exit(dragon, event):
        update_attack(dragon, event)

    @staticmethod
    def do(dragon):
        if dragon.attack:
            update_attack_frame(dragon)
        else:
            dragon.frame = (dragon.frame + 10 * app.elapsed_time) % 6

        update_move(dragon)

        if app.map[int(dragon.y - 1)][int(dragon.x)] != 1:
            dragon.add_event(DROP)

    @staticmethod
    def draw(dragon):
        draw_image(dragon, 1)


class JIdleState:
    @staticmethod
    def enter(dragon, event):
        update_velocity(dragon, event)
        update_enter(dragon, event)
        if dragon.rest_jump_volume == 0:
            dragon.rest_jump_volume = 5.5

    @staticmethod
    def exit(dragon, event):
        update_attack(dragon, event)

    @staticmethod
    def do(dragon):
        if dragon.attack:
            update_attack_frame(dragon)
        else:
            dragon.frame = (dragon.frame + 4 * app.elapsed_time) % 4

        update_jump(dragon)

    @staticmethod
    def draw(dragon):
        draw_image(dragon, 2)


class JumpState:
    @staticmethod
    def enter(dragon, event):
        update_velocity(dragon, event)
        update_enter(dragon, event)
        if dragon.rest_jump_volume == 0:
            dragon.rest_jump_volume = 5.5

    @staticmethod
    def exit(dragon, event):
        update_attack(dragon, event)

    @staticmethod
    def do(dragon):
        if dragon.attack:
            update_attack_frame(dragon)
        else:
            dragon.frame = (dragon.frame + 4 * app.elapsed_time) % 4

        update_move(dragon)
        update_jump(dragon)

    @staticmethod
    def draw(dragon):
        draw_image(dragon, 2)


class DIdleState:
    @staticmethod
    def enter(dragon, event):
        update_velocity(dragon, event)
        update_enter(dragon, event)

    @staticmethod
    def exit(dragon, event):
        update_attack(dragon, event)

    @staticmethod
    def do(dragon):
        if dragon.attack:
            update_attack_frame(dragon)
        else:
            dragon.frame = (dragon.frame + 4 * app.elapsed_time) % 4

        update_drop(dragon)


    @staticmethod
    def draw(dragon):
        draw_image(dragon, 3)


class DropState:
    @staticmethod
    def enter(dragon, event):
        update_velocity(dragon, event)
        update_enter(dragon, event)

    @staticmethod
    def exit(dragon, event):
        update_attack(dragon, event)

    @staticmethod
    def do(dragon):
        if dragon.attack:
            update_attack_frame(dragon)
        else:
            dragon.frame = (dragon.frame + 4 * app.elapsed_time) % 4

        update_move(dragon)
        update_drop(dragon)

    @staticmethod
    def draw(dragon):
        draw_image(dragon, 3)


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
                SLEEP_TIMER: SleepState, JUMP: JIdleState, DROP: DIdleState, ATTACK: IdleState, NONE: IdleState},
    MoveState: {LEFT_DOWN: IdleState, LEFT_UP: IdleState, RIGHT_DOWN: IdleState, RIGHT_UP: IdleState,
                SLEEP_TIMER: MoveState, JUMP: JumpState, DROP: DropState, ATTACK: MoveState, NONE: IdleState},
    JIdleState: {LEFT_DOWN: JumpState, LEFT_UP: JumpState, RIGHT_DOWN: JumpState, RIGHT_UP: JumpState,
                 SLEEP_TIMER: MoveState, JUMP: JIdleState, DROP: DIdleState, ATTACK: JIdleState, NONE: IdleState},
    JumpState: {LEFT_DOWN: JIdleState, LEFT_UP: JIdleState, RIGHT_DOWN: JIdleState, RIGHT_UP: JIdleState,
                SLEEP_TIMER: MoveState, JUMP: JumpState, DROP: DropState, ATTACK: JumpState, NONE: MoveState},
    DIdleState: {LEFT_DOWN: DropState, LEFT_UP: DropState, RIGHT_DOWN: DropState, RIGHT_UP: DropState,
                 SLEEP_TIMER: MoveState, JUMP: DIdleState, DROP: DIdleState, ATTACK: DIdleState, NONE: IdleState},
    DropState: {LEFT_DOWN: DIdleState, LEFT_UP: DIdleState, RIGHT_DOWN: DIdleState, RIGHT_UP: DIdleState,
                SLEEP_TIMER: MoveState, JUMP: DropState, DROP: DropState, ATTACK: DropState, NONE: MoveState}
}


class Dragon:
    def __init__(self):
        self.x, self.y = 3.5, 1
        self.image = load_image('resources\\sprites\\game_state\\dragon.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0

        self.input_left_safe = 0
        self.input_right_safe = 0

        self.rest_attack_time = 0
        self.rest_jump_volume = 0
        self.attack = 0

        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def get_bb(self):
        return self.x - 1.2, self.y + 0.25, self.x + 1.2, self.y + 3

    def fire_bubble(self):
        if self.rest_attack_time != 0:
            return
        bubble = Bubble(self.x, self.y, self.dir * 3)
        game_world.add_object(bubble, 1)
        self.rest_attack_time = 0.5
        self.attack = 1
        self.frame = 0

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        if self.rest_attack_time != 0:
            self.rest_attack_time -= app.elapsed_time
            if self.rest_attack_time < 0:
                self.rest_attack_time = 0
        for game_object in game_world.all_objects():
            if isinstance(game_object, monster.Monster):
                if app.collide(self, game_object):
                    if game_object.cur_state == monster.BubbleState:
                        game_object.add_event(monster.DIE)
                    elif game_object.cur_state == monster.DieState:
                        pass
                    else:
                        game_framework.change_state(scene_state_score)
            elif isinstance(game_object, Bubble):
                if app.collide(self, game_object) and game_object.cur_state == bubble.MoveState:
                    game_object.add_event(bubble.DISAPPEAR)
            elif isinstance(game_object, Item):
                if app.collide(self, game_object):
                    app.score += game_object.type_score
                    game_world.remove_object(game_object)

        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle((self.x - 1.2) * 8 * app.scale, (self.y + 0.25) * 8 * app.scale,
                       (self.x + 1.2) * 8 * app.scale, (self.y + 3) * 8 * app.scale)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
