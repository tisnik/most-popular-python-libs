#!/usr/bin/env python3
# vim: set fileencoding=utf-8

#
#  (C) Copyright 2021  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

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
pyautogui.moveTo(100, 100)
pyautogui.moveTo(200, 100)
pyautogui.moveTo(200, 200)
pyautogui.moveTo(100, 200)
pyautogui.moveTo(100, 100)

print("Done")
time.sleep(2)

print("Closing xev")
p.kill()
print("Closed")
