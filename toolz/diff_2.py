from toolz.itertoolz import diff


seq1 = [1, 2, 3, 4, 5, 6, 7, 8]
seq2 = [1, 0, 3, 4, 9, 9, 0, 8]
seq3 = [1, 2, 3, 0, 0, 6, 7, 8]

print(list(diff(seq1, seq2, seq3)))
