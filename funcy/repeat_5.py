from funcy import repeat, take

values = repeat(42)

slice = take(20, values)

print(list(slice))
