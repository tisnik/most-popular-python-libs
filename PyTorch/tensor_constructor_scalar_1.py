import torch

# konstrukce tenzoru
s1 = torch.Tensor(1)
print(s1)

# pristup k (jedine) slozce tenzoru
s1[0] = 42
print(s1)

# skutecny skalar
s2 = torch.tensor(100)
print(s2)
