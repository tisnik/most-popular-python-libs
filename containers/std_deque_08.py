from collections import deque

d = deque(["foo", "bar", "baz"])
print(d)

d.popleft()
print(d)

d.popleft()
print(d)
