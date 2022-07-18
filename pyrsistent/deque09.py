from pyrsistent import pdeque, v

vec = v("foo", "bar", "baz")
deque1 = pdeque(vec)

print(deque1)

deque2 = deque1.popleft()
print(deque2)

deque3 = deque2.popleft()
print(deque3)
