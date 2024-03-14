from toolz.itertoolz import take

sequence = range(1, 1000)

def head(s):
    return take(10, s)

first10 = head(sequence)
print(list(first10))
