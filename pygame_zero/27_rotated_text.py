WIDTH = 480
HEIGHT = 480


def draw():
    screen.fill("white")

    angles = range(0, 360, 45)
    colors = ("red", "orange", "yellow", "green", "blue", "#4B0082", "violet", "gray")

    for angle, color in zip(angles, colors):
        screen.draw.text("  colors",
                         (WIDTH/2, HEIGHT/2),
                         angle=angle,
                         fontsize=80,
                         color=color)
