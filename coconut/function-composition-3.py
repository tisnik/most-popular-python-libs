# Compiled Coconut: -----------------------------------------------------------

foo = _coconut_base_compose(ord, (abs, 0, False), (hex, 0, False))  #1 (line in Coconut source)

(print)((_coconut_base_compose(ord, (abs, 0, False), (hex, 0, False)))("B"))  #3 (line in Coconut source)

(print)((foo)("B"))  #5 (line in Coconut source)

bar = _coconut_base_compose(reversed, (sum, 0, False))  #7 (line in Coconut source)

(print)((_coconut_base_compose(reversed, (sum, 0, False)))(range(11)))  #9 (line in Coconut source)
(print)((bar)(range(11)))  #10 (line in Coconut source)
