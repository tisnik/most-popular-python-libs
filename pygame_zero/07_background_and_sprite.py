WIDTH = 480
HEIGHT = 480

sprite = Actor("sprite1.png")
sprite.pos = (240, 240)


def draw():
    screen.blit(images.plasma, (0, 0))
    sprite.draw()
