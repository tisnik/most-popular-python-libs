from box import Box

b = Box({0: "foo", 1: "bar", 2: "baz"}, box_safe_prefix="index_")

print(b[0])
print(b[1])
print(b[2])

print(b.index_0)
print(b.index_1)
print(b.index_2)
