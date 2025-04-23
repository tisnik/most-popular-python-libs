from torch import tensor, nn

l = nn.Linear(2, 2)

print("Weights:", l.weight)
print()
print("Bias:", l.bias)
