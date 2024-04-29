from box import Box

b = Box({"foo": 1, "bar": 2, "baz": None})

for key, value in b.items():
    print(key, value)
