from toolz import curry
from toolz.itertoolz import take

sequence = range(1, 1000)

curried = curry(take)

head = curried(10)

first10 = head(sequence)
print(list(first10))
