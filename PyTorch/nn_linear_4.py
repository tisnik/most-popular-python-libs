from torch import tensor, nn

l = nn.Linear(1, 1)

l.weight = nn.Parameter(data=tensor([[2.0]]))
l.bias = nn.Parameter(data=tensor([10.0]))

x = tensor([1.0])
y = l(x)

print(y)
