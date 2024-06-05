# Compiled Coconut: -----------------------------------------------------------

import math  #1 (line in Coconut source)


@_coconut_tco  #5 (line in Coconut source)
def _coconut_op_U221a(x):  #5 (line in Coconut source)
    return _coconut_tail_call(math.sqrt, x)  #5 (line in Coconut source)


for i in range(0, 10):  #7 (line in Coconut source)
    print((_coconut_op_U221a)(i))  #8 (line in Coconut source)
