from box import Box

b = Box({0: "foo", 1: "bar", 2: "baz"})

print(b[0])
print(b[1])
print(b[2])

print(b.0)
print(b.1)
print(b.2)
