from random import randrange

WIDTH = 480
HEIGHT = 480

BACKGROUND_COLOR = (0, 0x80, 0x80)
X_SPREAD = 100
Y_SPREAD = 200
SPRITES_COUNT = 100
sprites = None


def init_sprites():
    global sprites
    sprites = [Actor("particle.png") for i in range(SPRITES_COUNT)]
    for sprite in sprites:
        sprite.pos = (240, 0)
        a1(sprite)


def a1(sprite):
    sprite.x = WIDTH/2 + randrange(-X_SPREAD, X_SPREAD)
    sprite.y = 0 - randrange(Y_SPREAD)
    animate(sprite,
            x=WIDTH/2 + randrange(-X_SPREAD, X_SPREAD),
            y=HEIGHT + randrange(Y_SPREAD),
            angle=randrange(360),
            on_finished=lambda: a1(sprite),
            duration=randrange(2, 7),
            tween="accelerate")


def draw():
    screen.fill(BACKGROUND_COLOR)
    for sprite in sprites:
        sprite.draw()


def on_key_down(key, mod, unicode):
    if key == keys.ESCAPE:
        exit()


init_sprites()
