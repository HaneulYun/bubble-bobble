from pico2d import *
import game_framework

image = None

char_list = {
    '!': 0,
    '@': 1,  # open "
    '#': 2,
    '$': 3,
    '%': 4,
    '&': 5,
    '^': 6,  # close '
    '(': 7,
    ')': 8,
    '*': 9,
    '+': 10,
    ',': 11,
    '-': 12,
    '.': 13,
    '/': 14,
    '0': 15,
    '1': 16,
    '2': 17,
    '3': 18,
    '4': 19,
    '5': 20,
    '6': 21,
    '7': 22,
    '8': 23,
    '9': 24,
    ':': 25,
    ';': 26,
    '<': 27,
    '=': 28,
    '>': 29,
    '?': 30,
    'c': 31,
    'A': 32,
    'B': 33,
    'C': 34,
    'D': 35,
    'E': 36,
    'F': 37,
    'G': 38,
    'H': 39,
    'I': 40,
    'J': 41,
    'K': 42,
    'L': 43,
    'M': 44,
    'N': 45,
    'O': 46,
    'P': 47,
    'Q': 48,
    'R': 49,
    'S': 50,
    'T': 51,
    'U': 52,
    'V': 53,
    'W': 54,
    'X': 55,
    'Y': 56,
    'Z': 57,
    '[': 58,
    ']': 59,
    '~': 60,
    '"': 61,  # close "
    '\'': 62,  # open '
    ' ': 63
}


def enter():
    global image
    image = load_image('resources\\fonts\\fonts.png')


def draw(string, x, y, w=8, h=8):
    i = 0
    for c in string:
        image_x = char_list[c]
        if image_x is not 63:
            image_y = 10
            image.clip_draw(image_x * 8 + image_x + 1, image_y * 8 + image_y + 1, 8, 8,
                            x + w * i * game_framework.windowScale, y,
                            w * game_framework.windowScale, h * game_framework.windowScale)
        i += 1
