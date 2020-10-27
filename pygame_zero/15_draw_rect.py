WIDTH = 480
HEIGHT = 480

BORDER = 20


def draw():
    screen.fill("darkgreen")
    rect = Rect((BORDER, BORDER), (WIDTH-BORDER*2, HEIGHT-BORDER*2))
    screen.draw.rect(rect, (255, 255, 255))
