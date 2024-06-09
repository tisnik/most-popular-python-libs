# Simplified version of Coconut transpiled into Python

print((lambda _coconut_x: None if _coconut_x is None else abs(_coconut_x))(None))

print((lambda _coconut_x: None if _coconut_x is None else hex(_coconut_x))((lambda _coconut_x: None if _coconut_x is None else abs(_coconut_x))((lambda _coconut_x: None if _coconut_x is None else ord(_coconut_x))(None))))

print((lambda _coconut_x: None if _coconut_x is None else sum(_coconut_x))(None))

print((lambda _coconut_x: None if _coconut_x is None else sum(_coconut_x))((lambda _coconut_x: None if _coconut_x is None else reversed(_coconut_x))(None)))

@_coconut_tco
def evens(sequence):
    return _coconut_tail_call(filter, lambda x: x % 2 == 0, sequence)


print((lambda _coconut_x: None if _coconut_x is None else sum(_coconut_x))((lambda _coconut_x: None if _coconut_x is None else evens(_coconut_x))(None)))
