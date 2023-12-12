eg = ExceptionGroup(
        "Very serious exception",
        [TypeError("Unexpected type detected, expecting integer"),
         ValueError("Invalid value"),
         FileNotFoundError("Can not find file named foo.bar"),
         ZeroDivisionError("Divided by zero")])

import traceback
traceback.print_exception(eg)
