eg = ExceptionGroup(
        "Very serious exception",
        [
            TypeError("Unexpected type detected, expecting integer"),
            ExceptionGroup(
                "First sub-group",
                [ValueError("Invalid value"),
                 FileNotFoundError("Can not find file named foo.bar"),
                 ZeroDivisionError("Divided by zero")]
            ),
            ExceptionGroup(
                "Second sub-group",
                [TypeError("Unexpected type detected again, expecting integer"),
                 ZeroDivisionError("Divided by zero")]
            )
        ]
)

try:
    print("Let's raise exception group")
    print()
    raise eg
except* FileNotFoundError as fnf:
    print("FileNotFoundError")
    print(fnf.exceptions)
    print()
except* ValueError as ve:
    print("ValueError")
    print(ve.exceptions)
    print()
except* ZeroDivisionError as zde:
    print("ZeroDivisionError")
    print(zde.exceptions)
    print()
except* Exception as ex:
    print("Something else")
    print(ex)
    print()
