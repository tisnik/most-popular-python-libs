from funcy import count, takewhile

values = count()

filtered = takewhile(lambda x:x<10, values)

print(filtered)
print(list(filtered))
