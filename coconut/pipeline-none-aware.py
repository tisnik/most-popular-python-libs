# Compiled Coconut: -----------------------------------------------------------

(lambda _coconut_x: None if _coconut_x is None else (print)(_coconut_x))(None)  #1 (line in Coconut source)

(lambda _coconut_x: None if _coconut_x is None else (print)(_coconut_x))((lambda _coconut_x: None if _coconut_x is None else (abs)(_coconut_x))(None))  #3 (line in Coconut source)

(lambda _coconut_x: None if _coconut_x is None else (print)(_coconut_x))((lambda _coconut_x: None if _coconut_x is None else (hex)(_coconut_x))((lambda _coconut_x: None if _coconut_x is None else (abs)(_coconut_x))((lambda _coconut_x: None if _coconut_x is None else (ord)(_coconut_x))(None))))  #5 (line in Coconut source)

(lambda _coconut_x: None if _coconut_x is None else (print)(_coconut_x))((lambda _coconut_x: None if _coconut_x is None else (sum)(_coconut_x))(None))  #7 (line in Coconut source)

(lambda _coconut_x: None if _coconut_x is None else (print)(_coconut_x))((lambda _coconut_x: None if _coconut_x is None else (sum)(_coconut_x))((lambda _coconut_x: None if _coconut_x is None else (reversed)(_coconut_x))(None)))  #9 (line in Coconut source)

@_coconut_tco  #11 (line in Coconut source)
def evens(sequence):  #11 (line in Coconut source)
    return _coconut_tail_call(filter, lambda x: x % 2 == 0, sequence)  #12 (line in Coconut source)


(lambda _coconut_x: None if _coconut_x is None else (print)(_coconut_x))((lambda _coconut_x: None if _coconut_x is None else (sum)(_coconut_x))((lambda _coconut_x: None if _coconut_x is None else (evens)(_coconut_x))(None)))  #14 (line in Coconut source)
