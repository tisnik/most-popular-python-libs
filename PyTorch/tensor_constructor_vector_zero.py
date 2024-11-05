import torch

# konstrukce tenzoru prvniho radu
# s vynulovanim vsech prvku
v1 = torch.Tensor(3).zero_()
print(v1)

# pristup k (jedine) slozce tenzoru
v1[0] = 10
v1[1] = 20
v1[2] = 30
print(v1)
