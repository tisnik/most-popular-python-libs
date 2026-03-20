from microbit import *

while True:
    display.scroll("TEST")
    display.show(Image.TRIANGLE)
    sleep(1000)
    display.show(Image.CHESSBOARD)
    sleep(1000)
    display.show(Image.PACMAN)
    sleep(1000)
