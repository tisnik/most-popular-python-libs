from multidict import MultiDict

d = MultiDict({"id": 1, "name": "Eda", "surname": "Wasserfall"})

del d["id"]
del d["foo"]
del d["bar"]

print(d)
