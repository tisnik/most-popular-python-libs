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

print("Mouse move")
pyautogui.moveTo(100, 100, duration=0)
pyautogui.moveTo(200, 100, duration=2)
pyautogui.moveTo(200, 200, duration=2)
pyautogui.moveTo(100, 200, duration=2)
pyautogui.moveTo(100, 100, duration=2)

print("Done")
time.sleep(2)

print("Closing xev")
p.kill()
print("Closed")
