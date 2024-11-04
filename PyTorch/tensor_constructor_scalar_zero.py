import torch

# toto je skutecny skalar
s1 = torch.tensor(1).zero_()
print(s1)

# konstrukce tenzoru prvniho radu s jednim prvkem
# vynulovani prvku
s2 = torch.Tensor(1).zero_()
print(s2)

# pristup k (jedine) slozce tenzoru
s2[0] = 42
print(s2)

