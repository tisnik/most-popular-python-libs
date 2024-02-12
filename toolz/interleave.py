from toolz.itertoolz import count, interleave, take

values1 = range(1, 11)
values2 = ["odd", "even"]*5
interleaved = interleave((values1, values2))

print(list(interleaved))
