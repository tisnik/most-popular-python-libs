from toolz.curried import take

sequence = range(1, 1000)

head = take(10)

first10 = head(sequence)
print(list(first10))
