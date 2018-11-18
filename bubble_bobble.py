import pico2d
import game_framework

import font
import scene_state_intro

game_framework.windowScale = 4
windowScale = game_framework.windowScale

pico2d.open_canvas(320 * windowScale, 240 * windowScale)
font.enter()
game_framework.run(scene_state_intro)
pico2d.close_canvas()
