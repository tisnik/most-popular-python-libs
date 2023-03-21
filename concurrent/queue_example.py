#!/usr/bin/env python3

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

import queue

q = queue.Queue(500)

for item in range(10):
    print("Size", q.qsize())
    print("Empty?", q.empty())
    print("Full?", q.full())
    q.put("prvek # {}".format(item))

while not q.empty():
    print("Read item:", q.get())
