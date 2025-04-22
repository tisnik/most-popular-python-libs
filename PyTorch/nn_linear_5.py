import torch
from torch import nn

l = nn.Linear(1, 1)

l.weight = nn.Parameter(data=torch.tensor([[2.0]]))
l.bias = nn.Parameter(data=torch.tensor([10.0]))

x = torch.reshape(torch.arange(1.0, 11), (10, 1))
y = l(x)

print(y)
