from funcy import split

values = range(50)

selected, unselected = split(lambda x:x < 25, values)

print(list(selected))
print(list(unselected))
