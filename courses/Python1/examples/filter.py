x = range(20)

print(x)

y = filter(lambda value: value % 3 == 0, x)
print(list(y))
