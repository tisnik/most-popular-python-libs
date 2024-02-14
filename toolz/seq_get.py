from toolz.itertoolz import get

values = [chr(i) for i in range(ord('A'), ord('Z')+1)]

print(values)
print(get(0, values, "?"))
print(get(25, values, "?"))
print(get(26, values, "?"))
