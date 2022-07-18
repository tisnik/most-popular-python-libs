from pyrsistent import pdeque, v

vec = v("foo", "bar", "baz")
deque = pdeque(vec)

print(vec)
print(type(vec))

print()

print(deque)
print(type(deque))
