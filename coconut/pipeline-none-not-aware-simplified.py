# Simplified version of Coconut transpiled into Python

print(None)

print(abs(None))

print(hex(abs(ord(None))))

print(sum(None))

print(sum(reversed(None)))

@_coconut_tco
def evens(sequence):
    return _coconut_tail_call(filter, lambda x: x % 2 == 0, sequence)


print(sum(evens(None)))
