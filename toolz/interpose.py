from toolz.itertoolz import interpose

values = [chr(i) for i in range(ord('A'), ord('Z')+1)]

print(values)
print("".join(interpose("*", values)))
