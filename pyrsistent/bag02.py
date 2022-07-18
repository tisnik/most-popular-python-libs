from pyrsistent import pbag

bag1 = pbag(["foo", "bar", "baz"])

print(bag1)

l = list(bag1)
print(l)

bag2 = bag1 + pbag(["baz", "alpha", "omega"])

print(bag2)
