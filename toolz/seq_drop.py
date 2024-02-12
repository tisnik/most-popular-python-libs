from toolz.itertoolz import drop

values = [chr(i) for i in range(ord('A'), ord('Z')+1)]

print(values)
print(list(drop(10, values)))
