from collections import deque

d = deque(["a", "b", "c"])
print(d)

d.insert(1, "bar")
print(d)

d.insert(3, "baz")
print(d)
