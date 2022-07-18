from pyrsistent import pbag

bag1 = pbag(["foo", "bar", "baz"])

print(bag1)
print(type(bag1))

bag2 = bag1.add("bar")

print(bag2)
print(type(bag2))

bag3 = bag2.remove("baz")

print(bag3)
print(type(bag3))
