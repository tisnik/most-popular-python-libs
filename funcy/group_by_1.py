from funcy import group_by

values = range(100)

grouped = group_by(lambda x:x % 10, values)

for key, values in grouped.items():
    print(key, values)
