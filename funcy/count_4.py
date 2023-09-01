from funcy import count, repeat, take

values1 = count()
values2 = repeat(42)
zipped = zip(values1, values2)

slice = take(10, zipped)

print(list(slice))
