NOBODY = sentinel("NOBODY")


def login(x):
    print(x is NOBODY)


login(42)
login("ROOT")
login(NOBODY)
