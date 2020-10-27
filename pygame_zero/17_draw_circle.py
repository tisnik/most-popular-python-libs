WIDTH = 480
HEIGHT = 480

BORDER = 20


def draw():
    screen.fill("darkgreen")
    center = WIDTH//2, WIDTH//2
    radius = WIDTH//3
    screen.draw.circle(center, radius, (255, 255, 255))
