WIDTH = 480
HEIGHT = 480


def draw():
    screen.fill("white")

    radius = 10

    for j in range(0, 255, 16):
        for i in range(0, 255, 16):
            color = (0, i, j)
            pos = 20+i*1.5, 20+j*1.5
            screen.draw.filled_circle(pos, radius, color)

    for j in range(0, 255, 16):
        color = (j, 0, 0)
        pos = 420, 20+j*1.5
        screen.draw.filled_circle(pos, radius, color)

    for i in range(0, 255, 16):
        color = (i, i, 0)
        pos = 20+i*1.5, 420
        screen.draw.filled_circle(pos, radius, color)
