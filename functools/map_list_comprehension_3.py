def sign(value):
    if value < 0:
        return "negative"
    elif value > 0:
        return "positive"
    else:
        return "zero"


values = range(-10, 11)

converted = [sign(value) for value in values]

for c in converted:
    print(c)
