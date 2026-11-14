NOBODY = sentinel("NOBODY")


def login(x: str | NOBODY = NOBODY):
    print("Performing login for:", x)


login(42)
login("ROOT")
login(NOBODY)
login()
