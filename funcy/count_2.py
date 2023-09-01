from funcy import count, take

values = count()

slice = take(20, values)

print(list(slice))
