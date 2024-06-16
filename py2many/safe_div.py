def safe_div(x: int, y: int) -> int:
    try:
        return x//y
    except Exception:
        return 0
