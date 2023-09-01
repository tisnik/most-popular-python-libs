from funcy import iterate, take


sequence = iterate(lambda x: x+1, 0)

slice = take(10, sequence)
print(slice)
