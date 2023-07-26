values = range(-10, 11)

converted = ["negative" if x < 0 else "positive" if x > 0 else "zero" for x in values]

for c in converted:
    print(c)
