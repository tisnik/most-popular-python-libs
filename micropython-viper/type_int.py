@micropython.viper
def bar() -> int:
    return int(0xffffffff)


print(bar())
