# Simplified version of Coconut transpiled into Python

foo = _coconut_forward_compose(ord, abs, hex)

print((_coconut_forward_compose(ord, abs, hex))("B"))

print((foo)("B"))

bar = _coconut_forward_compose(reversed, sum)

print((_coconut_forward_compose(reversed, sum))(range(11)))
print((bar)(range(11)))
