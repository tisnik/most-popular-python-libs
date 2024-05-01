from multidict import MultiDict

d = MultiDict({str(x): x*2 for x in range(11) if x%3 != 0})

print(d)

for i in range(11):
    d.add(str(i), "foobar")

print(d)
