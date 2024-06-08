# Compiled Coconut: -----------------------------------------------------------

(print)((hex)((abs)((ord)("B"))))  #1 (line in Coconut source)

(print)((_coconut_forward_compose(ord, abs, hex))("B"))  #3 (line in Coconut source)

(print)((sum)((reversed)(range(11))))  #5 (line in Coconut source)

(print)((_coconut_forward_compose(reversed, sum))(range(11)))  #7 (line in Coconut source)

@_coconut_tco  #9 (line in Coconut source)
def evens(sequence):  #9 (line in Coconut source)
    return _coconut_tail_call(filter, lambda x: x % 2 == 0, sequence)  #10 (line in Coconut source)


(print)((_coconut_forward_compose(evens, sum))([1, 2, 3, 4, 5, 6, 30]))  #12 (line in Coconut source)
