from torch import nn

l = nn.Linear(1, 1)

print("Weights:", l.weight)
print()
print("Bias:", l.bias)
