from toolz.itertoolz import interleave

values1 = range(1, 11)
values2 = ["odd", "even"]*5
interleaved = interleave((values1, values2))

print(list(interleaved))
