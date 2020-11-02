WIDTH = 480
HEIGHT = 480

BACKGROUND_COLOR = (0, 0x80, 0x80)

sprite = Actor("sprite1.png")
sprite.pos = (240, 240)


def draw():
    screen.fill(BACKGROUND_COLOR)
    sprite.draw()


def on_key_down(key, mod, unicode):
    if key == keys.ESCAPE:
        exit()
    if key == keys.UP:
        sprite.top -= 1
    if key == keys.DOWN:
        sprite.top += 1
    if key == keys.LEFT:
        sprite.left -= 1
    if key == keys.RIGHT:
        sprite.left += 1
