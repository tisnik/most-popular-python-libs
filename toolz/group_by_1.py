from toolz.itertoolz import groupby

values = range(100)

grouped = groupby(lambda x:x % 10, values)

for key, values in grouped.items():
    print(key, values)
