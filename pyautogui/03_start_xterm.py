#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import subprocess
import time

print("Opening xterm")

# otevření terminálu
p = subprocess.Popen(["xterm", "-geometry", "40x20+100+100"])
assert p is not None

print("Opened")
time.sleep(5)

print("Closing xterm")
p.kill()
print("Closed")
