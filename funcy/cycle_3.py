from funcy import count, cycle, take

values1 = count(start=1)
values2 = cycle(["odd", "even"])
zipped = zip(values1, values2)

slice = take(10, zipped)

for key, val in slice:
    print(key, val)
