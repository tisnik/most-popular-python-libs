import torch

# konstrukce tenzoru
s2 = torch.tensor([-1])
print(s2)

# pristup k (jedine) slozce tenzoru
s2[0] = 42
print(s2)
