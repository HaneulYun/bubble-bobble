from pico2d import *

import app
import random
import game_world
import bubble

from game_behavior_tree import *

MPS = 1
MONSTER_SPEED_MPS = 6

LEFT, RIGHT, JUMP, DROP, NONE, BUBBLE, DIE = range(7)


class IdleState:
    @staticmethod
    def enter(monster, event):
        monster.frame = 0

    @staticmethod
    def exit(monster, event):
        pass

    @staticmethod
    def do(monster):
        monster.frame = (monster.frame + 2 * app.elapsed_time) % 4
        if app.map[int(monster.y - 1)][int(monster.x)] != 1:
            monster.add_event(DROP)
        else:
            monster.bt.run()

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
        if event == LEFT:
            monster.velocity = -MONSTER_SPEED_MPS
        elif event == RIGHT:
            monster.velocity = +MONSTER_SPEED_MPS

        if monster.velocity < 0:
            monster.dir = -1
        elif monster.velocity > 0:
            monster.dir = 1

    @staticmethod
    def exit(monster, event):
        monster.velocity = 0

    @staticmethod
    def do(monster):
        monster.frame = (monster.frame + 10 * app.elapsed_time) % 4

        if monster.velocity < 0:
            monster.x += monster.velocity * app.elapsed_time
            if monster.x < monster.target_x:
                monster.bt.run()
        elif monster.velocity > 0:
            monster.x += monster.velocity * app.elapsed_time
            if monster.x > monster.target_x:
                monster.bt.run()

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

        delta = MONSTER_SPEED_MPS * app.elapsed_time

        if monster.y > 25:
            monster.y -= delta
        elif app.map[int(monster.y)][int(monster.x)] != 1 and app.map[int(monster.y - delta)][int(monster.x)] == 1:
            monster.y = int(monster.y)
            monster.bt.run()
        else:
            monster.y -= delta
            if monster.y < -2.5:
                monster.y = 28

    @staticmethod
    def draw(monster):
        if monster.dir == 1:
            h = ''
        else:
            h = 'h'
        monster.image.clip_composite_draw(int(monster.frame) * 32, 3 * 32, 32, 32, 0, h,
                                          monster.x * 8 * app.scale, (monster.y * 8 + 18.5) * app.scale,
                                          32 * app.scale, 32 * app.scale)


class BubbleState:
    @staticmethod
    def enter(monster, event):
        monster.frame = 0

    @staticmethod
    def exit(monster, event):
        pass

    @staticmethod
    def do(monster):
        monster.frame = (monster.frame + 4 * app.elapsed_time) % 3

        dir = app.map[int(monster.y)][int(monster.x)]
        if dir == 2:
            monster.x += 2 * app.elapsed_time
        elif dir == 3:
            monster.y -= 2 * app.elapsed_time
        elif dir == 4:
            monster.x -= 2 * app.elapsed_time
        elif dir == 5 or dir == 1:
            monster.y += 2 * app.elapsed_time

    @staticmethod
    def draw(monster):
        if monster.dir == 1:
            h = ''
        else:
            h = 'h'
        bubble.Bubble.image.clip_composite_draw(6 * 24, 2 * 24, 24, 24, 0, h,
                                                monster.x * 8 * app.scale, (monster.y * 8 + 10) * app.scale,
                                                24 * app.scale, 24 * app.scale)
        monster.image.clip_composite_draw(int(monster.frame) * 32, 4 * 32, 32, 32, 0, h,
                                          monster.x * 8 * app.scale, (monster.y * 8 + 18.5) * app.scale,
                                          32 * app.scale, 32 * app.scale)


class DieState:
    @staticmethod
    def enter(monster, event):
        monster.frame = 0
        monster.bubble_x, monster.bubble_y = monster.x, monster.y
        monster.bubble_frame = 0
        print(monster.bubble_frame)

    @staticmethod
    def exit(monster, event):
        pass

    @staticmethod
    def do(monster):
        # if monster.bubble_frame < 6:
        monster.bubble_frame = (monster.bubble_frame + 8 * app.elapsed_time)
        monster.frame = (monster.frame + 4 * app.elapsed_time) % 4

        delta = MONSTER_SPEED_MPS * app.elapsed_time

        if app.map[int(monster.y)][int(monster.x)] != 1 and app.map[int(monster.y - delta)][int(monster.x)] == 1:
            monster.y = int(monster.y)
            if monster.bubble_frame >= 6:
                app.num_monster -= 1
                game_world.remove_object(monster)
        else:
            monster.y -= delta

    @staticmethod
    def draw(monster):
        if monster.dir == 1:
            h = ''
        else:
            h = 'h'

        if monster.bubble_frame < 2:
            frame_x, frame_y = int(2 + monster.bubble_frame), 1
        elif monster.bubble_frame < 6:
            frame_x, frame_y = int(monster.bubble_frame - 2), 0
        else:
            pass

        monster.image.clip_composite_draw(int(monster.frame + 4) * 32, 4 * 32, 32, 32, 0, h,
                                          monster.x * 8 * app.scale, (monster.y * 8 + 18.5) * app.scale,
                                          32 * app.scale, 32 * app.scale)
        if not monster.bubble_frame > 6:
            bubble.Bubble.image.clip_composite_draw(frame_x * 24, frame_y * 24, 24, 24, 0, h,
                                                    monster.bubble_x * 8 * app.scale, (monster.bubble_y * 8 + 10) * app.scale,
                                                    24 * app.scale, 24 * app.scale)


next_state_table = {
    IdleState: {LEFT: MoveState, RIGHT: MoveState, JUMP: JumpState, DROP: DropState,
                NONE: IdleState, BUBBLE: BubbleState, DIE: DieState},
    MoveState: {LEFT: MoveState, RIGHT: MoveState, JUMP: JumpState, DROP: DropState,
                NONE: IdleState, BUBBLE: BubbleState, DIE: DieState},
    JumpState: {LEFT: JumpState, RIGHT: JumpState, JUMP: JumpState, DROP: DropState,
                NONE: IdleState, BUBBLE: BubbleState, DIE: DieState},
    DropState: {LEFT: MoveState, RIGHT: MoveState, JUMP: JumpState, DROP: DropState,
                NONE: IdleState, BUBBLE: BubbleState, DIE: DieState},
    BubbleState: {LEFT: BubbleState, RIGHT: BubbleState, JUMP: BubbleState, DROP: BubbleState,
                  NONE: BubbleState, BUBBLE: BubbleState, DIE: DieState},
    DieState: {LEFT: DieState, RIGHT: DieState, JUMP: DieState, DROP: DieState,
               NONE: DieState, BUBBLE: DieState, DIE: DieState}

}


class Monster:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.image = None
        self.dir = 1
        self.velocity = 0
        self.frame = 0

        self.rest_jump_volume = 0
        self.bt = None
        self.build_behavior_tree()

        self.target_x, self.target_y = None, None

        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def get_bb(self):
        return self.x - 1.2, self.y + 0.25, self.x + 1.2, self.y + 2.75

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        for game_object in game_world.all_objects():
            if isinstance(game_object, bubble.Bubble):
                if app.collide(self, game_object) and game_object.cur_state == bubble.ShootState\
                        and self.cur_state != BubbleState:
                    self.add_event(BUBBLE)
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
                       (self.x + 1.2) * 8 * app.scale, (self.y + 2.75) * 8 * app.scale)

    def handle_event(self, event):
        pass

    def wander(self):
        pass
        # self.speed = MONSTER_SPEED_MPS
        # self.timer -= app.elapsed_time
        # if self.timer < 0:
        #     self.timer += 1.0
        #     self.dir = random.random()*2*math.pi
        # return BehaviorTree.SUCCESS

    def find_player(self):
        dragon = app.dragon
        self.target_x, self.target_y = dragon.x, dragon.y
        if self.y < dragon.y and app.map[int(self.y+4.5)][int(self.x)] == 1:
            self.add_event(JUMP)
            return BehaviorTree.SUCCESS
        elif self.x < dragon.x:
            self.add_event(RIGHT)
            return BehaviorTree.SUCCESS
        elif self.x > dragon.x:
            self.add_event(LEFT)
            return BehaviorTree.SUCCESS

        return BehaviorTree.FAIL
        # distance = (boy.x - self.x)**2 + (boy.y - self.y)**2
        # if distance < (PIXEL_PER_METER * 10)**2:
        #     self.dir = math.atan2(boy.y - self.y, boy.x - self.x)
        #     return BehaviorTree.SUCCESS
        # else:
        #     self.speed = 0
        #     return BehaviorTree.FAIL

    def move_to_player(self):
        pass
        # self.speed = RUN_SPEED_PPS
        # return BehaviorTree.SUCCESS

    def build_behavior_tree(self):
        pass
        # wander_node = LeafNode("Wander", self.wander)
        find_player_node = LeafNode("Find Player", self.find_player)
        # move_to_player_node = LeafNode("Move to Player", self.move_to_player)
        chase_node = SequenceNode("Chase")
        chase_node.add_children(find_player_node)

        wander_chase_node = SelectorNode("WanderChase")
        wander_chase_node.add_children(chase_node)
        self.bt = BehaviorTree(wander_chase_node)
