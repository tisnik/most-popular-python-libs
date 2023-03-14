from pympler import asizeof

for item in dir(asizeof):
    if item[0] != "_":
        print(item)
