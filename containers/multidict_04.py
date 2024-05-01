from multidict import MultiDict

d1 = MultiDict({"id": 1, "name": "Eda", "surname": "Wasserfall"})
d2 = MultiDict({"foo": "F", "bar": "B", "baz": "Z"})

d = {**d1, **d2}

print(d)
