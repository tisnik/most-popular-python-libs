from toolz.itertoolz import nth

values = [chr(i) for i in range(ord("A"), ord("Z")+1)]

print(values)
print(nth(0, values))
print(nth(25, values))
print(nth(26, values))
