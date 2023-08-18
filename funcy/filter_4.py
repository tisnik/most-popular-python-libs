from funcy import filter

data = range(0, 11)

filtered = filter(lambda value : value %2 == 1, data)
print(list(filtered))

filtered = filter(lambda value : value %2 == 0, data)
print(list(filtered))
