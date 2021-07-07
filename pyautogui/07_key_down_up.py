#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import subprocess
import time
import pyautogui

print("Opening xev")

# otevření aplikace xev
p = subprocess.Popen(["xev", "-geometry", "400x400+0+0"])
assert p is not None

print("Opened")
time.sleep(5)

print("Key down")
pyautogui.keyDown("F1")
pyautogui.keyDown("F2")
pyautogui.keyDown("F3")
pyautogui.keyDown("F4")

print("Key up")
pyautogui.keyUp("F4")
pyautogui.keyUp("F3")
pyautogui.keyUp("F2")
pyautogui.keyUp("F1")

time.sleep(5)

print("Closing xev")
p.kill()
print("Closed")
