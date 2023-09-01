from funcy import repeat

values1 = range(10)
values2 = repeat(42)

zipped = zip(values1, values2)

print(list(zipped))
