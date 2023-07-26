data = range(0, 11)

filtered = [value for value in data if value %2 == 1]
print(filtered)

filtered = [value for value in data if value %2 == 0]
print(filtered)
