import pico2d
import game_framework

import app
import font
import scene_state_intro
import scene_state_main
import scene_state_entry


pico2d.open_canvas(app.width * app.scale, app.height * app.scale)
font.enter()
game_framework.run(scene_state_entry)
pico2d.close_canvas()
