WIDTH = 480
HEIGHT = 480

BORDER = 20

def draw():
    screen.fill("darkgreen")
    screen.draw.line((BORDER, BORDER), (WIDTH-BORDER, BORDER), (255, 255, 255))
    screen.draw.line((WIDTH-BORDER, BORDER), (WIDTH-BORDER, HEIGHT-BORDER), (255, 255, 255))
    screen.draw.line((BORDER, BORDER), (BORDER, HEIGHT-BORDER), (255, 255, 255))
    screen.draw.line((BORDER, HEIGHT-BORDER), (WIDTH-BORDER, HEIGHT-BORDER), (255, 255, 255))
