from funcy import dropwhile

values = range(1000)

selected = dropwhile(lambda x:x < 990, values)

print(selected)
print(list(selected))
