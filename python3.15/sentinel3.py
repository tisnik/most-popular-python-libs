NOBODY = sentinel("NOBODY")


def login(x):
    print(x == NOBODY)


login(42)
login("ROOT")
login(NOBODY)
