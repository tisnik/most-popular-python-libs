from funcy import cycle, take

values = cycle(["foo", "bar"])

slice = take(10, values)
print(slice)
