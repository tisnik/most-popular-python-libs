eg = ExceptionGroup(
    "one", [TypeError(1), ValueError(3), OSError(4)])

import traceback
traceback.print_exception(eg)
