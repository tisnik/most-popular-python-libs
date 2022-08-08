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

print("Opening xterm")

# otevření terminálu
p = subprocess.Popen(["xterm", "-geometry", "40x20+100+100"])
assert p is not None

print("Opened")
time.sleep(5)

print("Closing xterm")
p.kill()
print("Closed")
