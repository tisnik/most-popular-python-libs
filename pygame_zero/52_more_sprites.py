WIDTH = 480
HEIGHT = 480

BACKGROUND_COLOR = (0, 0x40, 0x40)

red_sprite = Actor("red.gif")
red_sprite.pos = (120, 240)

blue_sprite = Actor("blue.gif")
blue_sprite.pos = (240, 240)

yellow_sprite = Actor("yellow.gif")
yellow_sprite.pos = (360, 240)


def draw():
    screen.fill(BACKGROUND_COLOR)
    red_sprite.draw()
    blue_sprite.draw()
    yellow_sprite.draw()
