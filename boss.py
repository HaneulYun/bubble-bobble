from pico2d import *
import game_framework

import app


class IdleState:
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


class MoveState:
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


class Boss:
    def __init__(self):
        pass

    def fire_bubble(self):
        pass

    def add_event(self, event):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def handle_event(self, event):
        pass
