from pyrsistent import pdeque, v

vec = v("foo", "bar", "baz")
deque1 = pdeque(vec)

print(deque1)

deque2 = deque1.pop()
print(deque2)

deque3 = deque2.pop()
print(deque3)
