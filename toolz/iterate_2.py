from toolz.itertoolz import iterate, take


sequence = iterate(lambda x: x+1, 0)

sequence = take(10, sequence)
print(list(sequence))
