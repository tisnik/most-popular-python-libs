from toolz.itertoolz import unique

values = [chr(i) for i in range(ord('A'), ord('Z')+1)] * 3

print(values)

values2 = unique(values)
print(list(values2))
