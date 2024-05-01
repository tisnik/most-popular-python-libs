from multiset import Multiset

m = Multiset({"foo": 0, "bar": 1, "baz": 2, "baf": 3})
print(m)

m.update(["foo"])
print(m)

m.update(["bar"])
print(m)
