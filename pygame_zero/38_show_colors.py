from pygame.colordict import THECOLORS
import random


WIDTH = 480
HEIGHT = 480

colors = THECOLORS


def draw():
    screen.fill("gray")

    for j in range(3):
        x = 10 + j * 160
        for j in range(12):
            y = 12 + j * 40
            color_name, color_value = random.choice(list(colors.items()))

            rect = Rect((x, y-8), (140, 30))
            screen.draw.filled_rect(rect, color_value)

            screen.draw.text(color_name,
                             (x, y),
                             owidth=1,
                             fontsize=24,
                             ocolor="white",
                             color="black")
