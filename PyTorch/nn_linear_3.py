from torch import nn, tensor

l = nn.Linear(1, 1)

l.weight = nn.Parameter(data=tensor([[2.0]]))
l.bias = nn.Parameter(data=tensor([10.0]))

print("Weights:", l.weight)
print()
print("Bias:", l.bias)
