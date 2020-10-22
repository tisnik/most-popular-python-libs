WIDTH = 480
HEIGHT = 480

BACKGROUND_COLOR = (0, 0x80, 0x80)

sprite = Actor("sprite1.png")
sprite.pos = (240, 240)

def draw():
    screen.fill(BACKGROUND_COLOR)
    sprite.draw()
