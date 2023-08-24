from funcy import lsplit

values = range(50)

selected, unselected = lsplit(lambda x:x < 25, values)

print(selected)
print(unselected)
