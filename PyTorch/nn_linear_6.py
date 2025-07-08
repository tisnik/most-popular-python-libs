from torch import nn

l = nn.Linear(2, 2)

print("Weights:", l.weight)
print()
print("Bias:", l.bias)
