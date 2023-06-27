def add(a:int, b:int) -> int:
    reveal_locals()
    return a+b

reveal_type(add)
reveal_type(add(1, 2))
