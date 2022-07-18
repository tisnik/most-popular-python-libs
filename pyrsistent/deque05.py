from pyrsistent import dq

deque = dq("foo", "bar", "baz")

print(deque)
print(type(deque))

print(deque.left)
print(deque.right)
