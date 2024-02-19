from toolz.itertoolz import sliding_window

values = range(10)

print(values)

for window in sliding_window(3, values):
    print(window)

print()

for window in sliding_window(7, values):
    print(window)
