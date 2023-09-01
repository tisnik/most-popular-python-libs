from funcy import count, repeat

values1 = count()
values2 = repeat(42, 10)

zipped = zip(values1, values2)

print(list(zipped))
