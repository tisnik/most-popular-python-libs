from toolz.itertoolz import interleave

values1 = range(1, 16)
values2 = ["odd", "even"]*3
interleaved = interleave((values1, values2))

print(list(interleaved))
