WIDTH = 480
HEIGHT = 480

red_sprite = Actor("red.gif")
red_sprite.pos = (160, 220)

blue_sprite = Actor("blue.gif")
blue_sprite.pos = (240, 220)

yellow_sprite = Actor("yellow.gif")
yellow_sprite.pos = (320, 220)


def draw():
    screen.blit(images.pacman, (0, 0))
    red_sprite.draw()
    blue_sprite.draw()
    yellow_sprite.draw()
