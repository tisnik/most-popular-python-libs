from collections import deque

d = deque(["a", "b", "c"])
print(d)

d.appendleft("bar")
print(d)

d.appendleft("baz")
print(d)
