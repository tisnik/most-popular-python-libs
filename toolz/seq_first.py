from toolz.itertoolz import first

values = [chr(i) for i in range(ord("A"), ord("Z")+1)]

print(values)
print(first(values))
