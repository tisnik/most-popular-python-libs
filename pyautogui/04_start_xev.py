#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import subprocess
import time

print("Opening xev")

# otevření aplikace xev
p = subprocess.Popen(["xev", "-geometry", "400x400+0+0"])
assert p is not None

print("Opened")
time.sleep(5)

print("Closing xev")
p.kill()
print("Closed")
