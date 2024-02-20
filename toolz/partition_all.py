from toolz.itertoolz import partition, partition_all

values = [chr(i) for i in range(ord('A'), ord('Z')+1)]

print(values)
print(list(partition(3, values)))
print(list(partition_all(3, values)))
