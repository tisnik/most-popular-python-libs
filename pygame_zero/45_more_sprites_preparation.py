from random import randrange

WIDTH = 480
HEIGHT = 480

BACKGROUND_COLOR = (0, 0x80, 0x80)
X_SPREAD = 50

sprite = Actor("particle.png")
sprite.pos = (240, 0)


def a1():
    sprite.x = WIDTH/2 + randrange(-X_SPREAD, X_SPREAD)
    sprite.y = -10
    animate(sprite,
            x=WIDTH/2 + randrange(-X_SPREAD, X_SPREAD),
            y=HEIGHT,
            on_finished=a1,
            duration=5,
            tween="accelerate")


def draw():
    screen.fill(BACKGROUND_COLOR)
    sprite.draw()


def on_key_down(key, mod, unicode):
    if key == keys.ESCAPE:
        exit()


a1()
