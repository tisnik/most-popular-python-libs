NOBODY = sentinel("NOBODY")


def login(x = NOBODY):
    print(x is NOBODY)


login(42)
login("ROOT")
login(NOBODY)
login()
