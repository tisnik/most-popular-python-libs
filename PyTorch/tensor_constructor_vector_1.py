import torch

# konstrukce tenzoru
v1 = torch.Tensor(3)
print(v1)

# pristup k (jedine) slozce tenzoru
v1[0] = 10
v1[1] = 20
v1[2] = 30
print(v1)
