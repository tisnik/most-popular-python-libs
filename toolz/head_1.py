from toolz.itertoolz import take

sequence = range(1, 1000)

first10 = take(10, sequence)
print(list(first10))
