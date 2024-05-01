from multidict import MultiDict

d = MultiDict({"id": 1, "name": "Eda", "surname": "Wasserfall"})

print(d)

print(d["name"])

d["hra"] = "Svestka"

print(d)
