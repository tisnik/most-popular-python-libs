from multiset import Multiset

m = Multiset({"foo": 0, "bar": 1, "baz": 2, "baf": 3})
print(m)

m2 = m.combine(["foo"])
print(m2)

m3 = m.combine(["bar"])
print(m3)

m4 = m.combine(["xyzzy"])
print(m4)
