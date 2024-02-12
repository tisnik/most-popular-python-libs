from toolz.itertoolz import partition

values = [chr(i) for i in range(ord('A'), ord('Z')+1)]

print(values)
print(list(partition(3, values)))
print(list(partition(3, values, "*")))
