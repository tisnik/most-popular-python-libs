from box import Box

b = Box({"foo": 1, "bar": 2, "baz": None})

print(b["foo"])
print(b.foo)
print()

print(b["bar"])
print(b.bar)
print()

print(b["baz"])
print(b.baz)
print()

