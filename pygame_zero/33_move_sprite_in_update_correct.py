WIDTH = 480
HEIGHT = 480

BACKGROUND_COLOR = (0, 0x80, 0x80)

sprite = Actor("sprite1.png")
sprite.pos = (240, 240)
dx = 0
dy = 0


def draw():
    screen.fill(BACKGROUND_COLOR)
    sprite.draw()


def update():
    sprite.left += dx
    sprite.top += dy


def on_key_down(key, mod, unicode):
    global dx, dy
    if key == keys.ESCAPE:
        exit()
    if key == keys.UP:
        dy = -1
    if key == keys.DOWN:
        dy = 1
    if key == keys.LEFT:
        dx = -1
    if key == keys.RIGHT:
        dx = 1


def on_key_up(key, mod):
    global dx, dy
    if key == keys.ESCAPE:
        exit()
    if key in (keys.UP, keys.DOWN, keys.LEFT, keys.RIGHT):
        dx = 0
        dy = 0
