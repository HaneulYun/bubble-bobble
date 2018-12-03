from pico2d import *
import game_framework

import app
import font
import scene_state_main

name = 'scene_state_score'
image_back = None
image_player = None


def enter():
    global image_back, image_player
    image_back = load_image('resources\\sprites\\lobby_state\\background.png')
    image_player = load_image('resources\\sprites\\lobby_state\\player.png')

    app.ranking.append([app.score, get_time() - app.entry_time])
    app.ranking.sort()
    app.ranking.reverse()

    while app.ranking.__len__() > 10:
        app.ranking.remove(app.ranking[-1])

    with open('ranking.txt', 'w') as f:
        json.dump(app.ranking, f)


def exit():
    global image_back, image_player
    del image_back, image_player


def update():
    pass


def draw():
    clear_canvas()
    image_back.draw(app.width / 2 * app.scale, app.height / 2 * app.scale,
               app.width * app.scale, app.height * app.scale)
    font.draw('RANK', app.width / 4 * 1 + 4, app.height / 4 * 3, font.WHITE, font.MIDDLE)
    font.draw('SCORE', app.width / 4 * 2 - 16, app.height / 4 * 3, font.WHITE, font.MIDDLE)
    font.draw('TIME', app.width / 4 * 3 + 4, app.height / 4 * 3, font.WHITE, font.MIDDLE)
    for i in range(0, app.ranking.__len__()):
        font.draw(str(i + 1), app.width / 4 * 1 + 20, app.height / 4 * 3 - (i + 2) * 12, font.WHITE, font.RIGHT)
        font.draw(str(app.ranking[i][0]), app.width / 4 * 2 + 4, app.height / 4 * 3 - (i + 2) * 12, font.WHITE, 1)
        font.draw(str(app.ranking[i][1]) + ' S', app.width / 4 * 3 + 20, app.height / 4 * 3 - (i + 2) * 12, font.WHITE, 1)

        # font.draw(get_canvas_width() // 2 - 80, get_canvas_height() // 2 + 100 - 20 * i,
        #           "#" + str(i+1) + ". " + '%.2f' % ranking[i])
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
                game_framework.change_state(scene_state_main)


def pause():
    pass


def resume():
    pass
