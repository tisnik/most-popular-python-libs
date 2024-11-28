import torch

# konstrukce tenzoru, vyplneni sekvenci
v1 = torch.range(1, 12)
print(v1)
print()

# konstrukce prvni matice z puvodniho tenzoru
m1 = torch.reshape(v1, (4, 3))
print(m1)
print()

# konstrukce vektoru
v2 = torch.tensor([1., 2., -1., 0])
print(v2)
print()

# provedeni maticoveho soucinu
m2 = v2 @ m1
print(m2)

