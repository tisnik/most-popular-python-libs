from pyrsistent import pdeque, v

vec = v("foo", "bar", "baz")
deque1 = pdeque(vec)

deque2 = deque1.reverse()
print(deque2)

deque3 = deque1.rotate(1)
print(deque3)
