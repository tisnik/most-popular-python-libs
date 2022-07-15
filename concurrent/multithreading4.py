#!/usr/bin/env python3
# vim: set fileencoding=utf-8

#
#  (C) Copyright 2022  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

"""Multithreading."""

import threading
import time


class X:
    def __init__(self):
        print("X constructed")

    def __del__(self):
        print("X destructed")


def worker():
    print("thread started")
    time.sleep(10)
    print("thread finished")


print("main started")

x = X()

# vytvoření a spuštění trojice vláken
threading.Thread(target=worker).start()
threading.Thread(target=worker).start()
threading.Thread(target=worker).start()

print("main finished")
