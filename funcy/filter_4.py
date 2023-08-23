from funcy import filter, lfilter

data = range(0, 11)

print("filter")

filtered = filter(lambda value : value %2 == 1, data)
print(list(filtered))

filtered = filter(lambda value : value %2 == 0, data)
print(list(filtered))

print()
print("lfilter")

filtered = lfilter(lambda value : value %2 == 1, data)
print(filtered)

filtered = lfilter(lambda value : value %2 == 0, data)
print(filtered)
