WIDTH = 480
HEIGHT = 480

BACKGROUND_COLOR = (0, 0x40, 0x40)

red_sprite = Actor("red.gif")
red_sprite.pos = (120, 240)

blue_sprite = Actor("blue.gif")
blue_sprite.pos = (240, 240)

yellow_sprite = Actor("yellow.gif")
yellow_sprite.pos = (360, 240)

dx = 0
dy = 0


def draw_sprite_pos(which, sprite, pos_x, pos_y, color):
    screen.draw.text(which + ":", (pos_x, pos_y), color=color)
    msg = "left: {}  right: {}  top: {}  bottom: {}".format(int(sprite.left), int(sprite.right), int(sprite.top), int(sprite.bottom))
    screen.draw.text(msg, (pos_x+100, pos_y), color=color)


def draw():
    screen.fill(BACKGROUND_COLOR)
    red_sprite.draw()
    blue_sprite.draw()
    yellow_sprite.draw()

    draw_sprite_pos("Red", red_sprite, 10, 10, "#db0000")
    draw_sprite_pos("Blue", blue_sprite, 10, 30, "#00a2db")
    draw_sprite_pos("Yellow", yellow_sprite, 10, 50, "#dbc500")


def update():
    blue_sprite.left += dx
    blue_sprite.top += dy


def on_key_down(key, mod, unicode):
    global dx, dy
    if key == keys.ESCAPE:
        exit()
    if key == keys.UP:
        dy = -1
    if key == keys.DOWN:
        dy = 1
    if key == keys.LEFT:
        dx = -1
    if key == keys.RIGHT:
        dx = 1


def on_key_up(key, mod):
    global dx, dy
    if key == keys.ESCAPE:
        exit()
    if key == keys.UP or key == keys.DOWN:
        dy = 0
    if key == keys.LEFT or key == keys.RIGHT:
        dx = 0
