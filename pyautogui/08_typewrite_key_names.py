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

print("Simulating keyboard...")
pyautogui.typewrite(["a", "enter", "f1", "delete", "alt"], interval=1.0)
print("Done")

time.sleep(5)

print("Closing xev")
p.kill()
print("Closed")
