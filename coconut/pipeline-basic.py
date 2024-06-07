# Compiled Coconut: -----------------------------------------------------------

(print)((abs)(-42))  #1 (line in Coconut source)

(print)((hex)((abs)((ord)("B"))))  #3 (line in Coconut source)

(print)((sum)(range(11)))  #5 (line in Coconut source)

(print)((sum)((reversed)(range(11))))  #7 (line in Coconut source)

@_coconut_tco  #9 (line in Coconut source)
def evens(sequence):  #9 (line in Coconut source)
    return _coconut_tail_call(filter, lambda x: x % 2 == 0, sequence)  #10 (line in Coconut source)


(print)((sum)((evens)([1, 2, 3, 4, 5, 6, 30])))  #12 (line in Coconut source)
