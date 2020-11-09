from math import sin, cos, radians

WIDTH = 480
HEIGHT = 480

BACKGROUND_COLOR = (0, 0x80, 0x80)

sprite = Actor("spaceship.png")
sprite.pos = (240, 240)
speed_delta = 0
angle_delta = 0
speed = 0
angle = 0


def draw():
    screen.fill(BACKGROUND_COLOR)
    sprite.draw()


def update():
    global speed, angle, speed_delta
    angle += angle_delta
    sprite.top -= speed*cos(radians(angle))
    sprite.left -= speed*sin(radians(angle))
    sprite.angle = angle
    speed += speed_delta
    speed *= 0.95


def on_key_down(key, mod, unicode):
    global speed_delta, angle_delta, speed
    if key == keys.ESCAPE:
        exit()
    if key == keys.R:
        speed_delta = 0
        speed = 0
        sprite.x = WIDTH/2
        sprite.y = HEIGHT/2
    if key == keys.UP:
        speed_delta = 1.5
    if key == keys.DOWN:
        speed_delta = -1.5
    if key == keys.LEFT:
        angle_delta = 1
    if key == keys.RIGHT:
        angle_delta = -1


def on_key_up(key, mod):
    global speed_delta, angle_delta
    if key == keys.ESCAPE:
        exit()
    if key == keys.LEFT or key == keys.RIGHT:
        angle_delta = 0
    if key == keys.UP or key == keys.DOWN:
        speed_delta = 0
