values = range(-10, 11)

converted = map(lambda x: "negative" if x < 0 else "positive" if x > 0 else "zero", values)

for c in converted:
    print(c)
