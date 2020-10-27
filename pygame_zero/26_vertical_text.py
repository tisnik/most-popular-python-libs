WIDTH = 480
HEIGHT = 480


def draw():
    screen.fill("black")

    screen.draw.text("Pygame Zero",
                     (WIDTH/2-20, HEIGHT-60),
                     angle=90,
                     fontsize=80,
                     color="orange",
                     gcolor="red")
