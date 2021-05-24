#
#  (C) Copyright 2020  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

WIDTH = 480
HEIGHT = 480

BACKGROUND_COLOR = (0, 0x40, 0x40)

red_sprite = Actor("red.gif")
red_sprite.pos = (120, 240)
red_sprite.dx = 1
red_sprite.dy = 1

blue_sprite = Actor("blue.gif")
blue_sprite.pos = (240, 240)
blue_sprite.dx = 0
blue_sprite.dy = 0

yellow_sprite = Actor("yellow.gif")
yellow_sprite.pos = (360, 240)
yellow_sprite.dx = 0
yellow_sprite.dy = 0


def draw_sprite_pos(which, sprite, pos_x, pos_y, color):
    screen.draw.text(which + ":", (pos_x, pos_y), color=color)
    screen.draw.text(str(int(sprite.x)), (pos_x+70, pos_y), color=color)
    screen.draw.text(str(int(sprite.y)), (pos_x+110, pos_y), color=color)


def draw_sprite_col(sprite, other_sprites, pos_x, pos_y, color):
    collision = False
    if sprite.collidelist(other_sprites) >= 0:
        screen.draw.text("x", (pos_x, pos_y), color=color)


def draw():
    screen.fill(BACKGROUND_COLOR)
    red_sprite.draw()
    blue_sprite.draw()
    yellow_sprite.draw()

    draw_sprite_pos("Red", red_sprite, 10, 10, "#db0000")
    draw_sprite_pos("Blue", blue_sprite, 10, 30, "#00a2db")
    draw_sprite_pos("Yellow", yellow_sprite, 10, 50, "#dbc500")

    draw_sprite_col(red_sprite, (blue_sprite, yellow_sprite), 200, 10, "#db0000")
    draw_sprite_col(blue_sprite, (red_sprite, yellow_sprite), 200, 30, "#00a2db")
    draw_sprite_col(yellow_sprite, (red_sprite, blue_sprite), 200, 50, "#dbc500")


def reset_sprite():
    red_sprite.image = "red.gif"


def bounce(sprite):
    bounced = False

    if red_sprite.left < 0:
        red_sprite.left = 0
        red_sprite.dx = -red_sprite.dx
        bounced = True

    if red_sprite.right > WIDTH:
        red_sprite.right = WIDTH
        red_sprite.dx = -red_sprite.dx
        bounced = True

    if red_sprite.top < 0:
        red_sprite.top = 0
        red_sprite.dy = -red_sprite.dy
        bounced = True

    if red_sprite.bottom > HEIGHT:
        red_sprite.bottom = HEIGHT
        red_sprite.dy = -red_sprite.dy
        bounced = True

    if bounced:
        red_sprite.image = "gray.gif"
        clock.schedule_unique(reset_sprite, 0.4)
        sounds.ping.play()


def collide(sprite1, sprite2):
    if sprite1.colliderect(sprite2):
        sprite1.image = "white.gif"
        clock.schedule_unique(reset_sprite, 1.0)


def update():
    blue_sprite.left += blue_sprite.dx
    blue_sprite.top += blue_sprite.dy

    yellow_sprite.left += yellow_sprite.dx
    yellow_sprite.top += yellow_sprite.dy

    red_sprite.left += red_sprite.dx
    red_sprite.top += red_sprite.dy

    bounce(red_sprite)
    collide(red_sprite, blue_sprite)
    collide(red_sprite, yellow_sprite)


def on_key_down(key, mod, unicode):
    global dx, dy
    if key == keys.ESCAPE:
        exit()
    if key == keys.UP:
        blue_sprite.dy = -1
    if key == keys.DOWN:
        blue_sprite.dy = 1
    if key == keys.LEFT:
        blue_sprite.dx = -1
    if key == keys.RIGHT:
        blue_sprite.dx = 1
    if key == keys.W:
        yellow_sprite.dy = -1
    if key == keys.S:
        yellow_sprite.dy = 1
    if key == keys.A:
        yellow_sprite.dx = -1
    if key == keys.D:
        yellow_sprite.dx = 1


def on_key_up(key, mod):
    global dx, dy
    if key == keys.ESCAPE:
        exit()
    if key == keys.UP or key == keys.DOWN:
        blue_sprite.dy = 0
    if key == keys.LEFT or key == keys.RIGHT:
        blue_sprite.dx = 0
    if key == keys.W or key == keys.S:
        yellow_sprite.dy = 0
    if key == keys.A or key == keys.D:
        yellow_sprite.dx = 0
