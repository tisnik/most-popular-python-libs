from random import randrange

WIDTH = 480
HEIGHT = 480

BACKGROUND_COLOR = (0, 0x80, 0x80)


def draw():
    screen.fill(BACKGROUND_COLOR)


def on_key_down(key, mod, unicode):
    if key == keys.ESCAPE:
        exit()
    if key == keys.SPACE:
        sounds.login.play()
