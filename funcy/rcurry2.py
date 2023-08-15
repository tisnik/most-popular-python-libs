from funcy import rcurry


def div(x, y):
    return x / y


curried = rcurry(div)

print(curried)
print(curried(1))
print(curried(1)(2))  # pozor na umístění závorek!
