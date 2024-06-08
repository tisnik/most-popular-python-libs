# Compiled Coconut: -----------------------------------------------------------

foo = _coconut_forward_compose(ord, abs, hex)  #1 (line in Coconut source)

(print)((_coconut_forward_compose(ord, abs, hex))("B"))  #3 (line in Coconut source)

(print)((foo)("B"))  #5 (line in Coconut source)

bar = _coconut_forward_compose(reversed, sum)  #7 (line in Coconut source)

(print)((_coconut_forward_compose(reversed, sum))(range(11)))  #9 (line in Coconut source)
(print)((bar)(range(11)))  #10 (line in Coconut source)
