from frozendict import frozendict

d: frozendict = frozendict(x=1, y=2, z="foo")
print(d)

d["a"] = "bar"

del d["z"]
