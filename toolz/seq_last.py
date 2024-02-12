from toolz.itertoolz import last

values = [chr(i) for i in range(ord('A'), ord('Z')+1)]

print(values)
print(last(values))
