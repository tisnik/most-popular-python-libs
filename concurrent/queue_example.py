#!/usr/bin/env python3

import queue

q = queue.Queue(500)

for item in range(10):
    print("Size", q.qsize())
    print("Empty?", q.empty())
    print("Full?", q.full())
    q.put("prvek # {}".format(item))

while not q.empty():
    print("Read item:", q.get())
