WIDTH = 480
HEIGHT = 480

BACKGROUND_COLOR = (0, 0x80, 0x80)
TEXT_COLOR = "Orange"
TEXT_LEFT = 10
TEXT_HEIGHT = 16

MESSAGES = (
        "F - fast animation",
        "R - reset animation",
        "",
        "Esc - exit"
        )

sprite = Actor("sprite1.png")
sprite.pos = (0, 240)


def draw():
    screen.fill(BACKGROUND_COLOR)
    sprite.draw()

    y = 10
    for message in MESSAGES:
        screen.draw.text(message, (TEXT_LEFT, y), color=TEXT_COLOR)
        y += TEXT_HEIGHT


def on_key_down(key, mod, unicode):
    if key == keys.ESCAPE:
        exit()
    if key == keys.R:
        sprite.x = 0
    if key == keys.F:
        animate(sprite, x=WIDTH)
