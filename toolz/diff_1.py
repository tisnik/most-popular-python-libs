from toolz.itertoolz import diff

seq1 = [1, 2, 3, 4, 5, 6, 7]
seq2 = [1, 0, 3, 4, 9, 9, 0]

print(list(diff(seq1, seq2)))
