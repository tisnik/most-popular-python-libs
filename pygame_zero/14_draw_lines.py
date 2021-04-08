WIDTH = 480
HEIGHT = 480

BORDER = 20


def draw():
    screen.fill("white")

    for i in range(0, WIDTH-BORDER+1, 10):
        color = i * 255 / WIDTH
        screen.draw.line((BORDER, i), (BORDER+i, HEIGHT-BORDER), (color, 0, 255-color))
