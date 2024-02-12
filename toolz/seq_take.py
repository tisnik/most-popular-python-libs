from toolz.itertoolz import take

values = [chr(i) for i in range(ord('A'), ord('Z')+1)]

print(values)
print(list(take(10, values)))
