from toolz.itertoolz import sliding_window

values = range(10)

print(values)

for window in sliding_window(5, values):
    print(window)
