import game_framework
import pico2d

game_framework.windowScale = 4
windowScale = game_framework.windowScale

pico2d.open_canvas(320 * windowScale, 240 * windowScale)
game_framework.run(game_framework.TestGameState('test'))
pico2d.close_canvas()
