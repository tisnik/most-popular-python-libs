from multidict import MultiDict

d = MultiDict({str(x): x*2 for x in range(10) if x%3 != 0})

for i in range(10):
    d.add(str(i), "foo")
    d.add(str(i), "bar")

print(d)
print()

keys = sorted(d.keys())
print(keys)
print()

for key in keys:
    print(key, d.getone(key))
