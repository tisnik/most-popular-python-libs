# Compiled Coconut: -----------------------------------------------------------

(print)(None)  #1 (line in Coconut source)

(print)((abs)(None))  #3 (line in Coconut source)

(print)((hex)((abs)((ord)(None))))  #5 (line in Coconut source)

(print)((sum)(None))  #7 (line in Coconut source)

(print)((sum)((reversed)(None)))  #9 (line in Coconut source)

@_coconut_tco  #11 (line in Coconut source)
def evens(sequence):  #11 (line in Coconut source)
    return _coconut_tail_call(filter, lambda x: x % 2 == 0, sequence)  #12 (line in Coconut source)


(print)((sum)((evens)(None)))  #14 (line in Coconut source)
