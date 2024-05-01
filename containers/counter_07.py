from collections import Counter

c1 = Counter({"foo": 0, "bar": 1, "baz": 2})
print(c1)

c2 = Counter(["foo", "bar", "baz", "baf"])
print(c2)

c3 = c1 - c2
print(c3)

c4 = c2 - c1
print(c4)
