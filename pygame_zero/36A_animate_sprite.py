WIDTH = 480
HEIGHT = 480

BACKGROUND_COLOR = (0, 0x80, 0x80)

sprite = Actor("sprite1.png")
sprite.pos = (0, 240)
animation = animate(sprite, x=WIDTH)


def draw():
    screen.fill(BACKGROUND_COLOR)
    sprite.draw()


def on_key_down(key, mod, unicode):
    if key == keys.ESCAPE:
        exit()
