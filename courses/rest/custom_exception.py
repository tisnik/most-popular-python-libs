class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


class E(D):
    pass


for cls in [B, C, D, E]:
    try:
        raise cls()
    except E:
        print("E")
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
