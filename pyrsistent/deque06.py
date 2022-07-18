from pyrsistent import pdeque, v

vec = v("foo")
deque1 = pdeque(vec)

print(deque1)

deque2 = deque1.append("bar")
print(deque2)

deque3 = deque2.append("baz")
print(deque3)
