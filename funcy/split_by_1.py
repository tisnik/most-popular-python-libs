from funcy import split_by

values = range(100)

selected, rest = split_by(lambda x:x < 10, values)

print(list(selected))
print(list(rest))
