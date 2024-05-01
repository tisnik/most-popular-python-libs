from multiset import Multiset

m1 = Multiset(["foo", "bar", "baz", "baf", "xyzzy"])
print(m1)

m2 = Multiset({"foo": 0, "bar": 1, "baz": 2, "baf": 3})
print(m2)

m3 = m1 + m2
print(m3)
