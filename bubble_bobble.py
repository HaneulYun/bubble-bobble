import pico2d
import game_framework

import scene_state_intro

game_framework.windowScale = 4
windowScale = game_framework.windowScale

pico2d.open_canvas(320 * windowScale, 240 * windowScale)
game_framework.run(scene_state_intro)
pico2d.close_canvas()
