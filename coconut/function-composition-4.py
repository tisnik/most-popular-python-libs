# Compiled Coconut: -----------------------------------------------------------

foo = _coconut_base_compose(ord, (abs, 0, False), (hex, 0, False))  #1 (line in Coconut source)

(print)((_coconut_base_compose(ord, (abs, 0, False), (hex, 0, False)))(None))  #3 (line in Coconut source)

(print)((foo)(None))  #5 (line in Coconut source)

bar = _coconut_base_compose(reversed, (sum, 0, False))  #7 (line in Coconut source)

(print)((_coconut_base_compose(reversed, (sum, 0, False)))(None))  #9 (line in Coconut source)
(print)((bar)(None))  #10 (line in Coconut source)
