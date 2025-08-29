def function(level):
    if level < 1:
        raise ValueError("Invalid level!", level)
    print(
        "ok - function was called with parameter level set to {level}".format(
            level=level
        )
    )


try:
    for i in range(10, -10, -1):
        function(i)
except ValueError as value:
    print("Exception in function(): {value}".format(value=value))
else:
    print("Everything is OK")
