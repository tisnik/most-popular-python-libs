from torch import nn

l = nn.Linear(0, 0)

print("Weights:", l.weight)
print()
print("Bias:", l.bias)
print()

l = nn.Linear(1, 0)

print("Weights:", l.weight)
print()
print("Bias:", l.bias)
print()

l = nn.Linear(0, 1)

print("Weights:", l.weight)
print()
print("Bias:", l.bias)
