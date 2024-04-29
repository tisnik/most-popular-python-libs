from box import Box

b = Box({"foo": 1, "bar": 2, "baz": None})

print(b["unknown"])
