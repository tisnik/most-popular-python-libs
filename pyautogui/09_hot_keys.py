#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import subprocess
import time
import pyautogui

print("Opening xterm")

# otevření terminálu
p = subprocess.Popen(["xterm", "-geometry", "40x20+100+100"])
assert p is not None

print("Opened")
time.sleep(5)

print("Writing into terminal window...")
pyautogui.hotkey("shift", "a")
pyautogui.hotkey("shift", "z")
time.sleep(1)

print("Moving cursor...")
pyautogui.hotkey("ctrl", "a")
time.sleep(1)
pyautogui.hotkey("ctrl", "e")
time.sleep(1)

print("Done")

time.sleep(5)

print("Closing xterm")
p.kill()
print("Closed")
