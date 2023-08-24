from funcy import takewhile

values = range(1000)

selected = takewhile(lambda x:x < 10, values)

print(selected)
print(list(selected))
