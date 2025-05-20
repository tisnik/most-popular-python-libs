# Knihovna PyTorch
#
import torch

# konstrukce tenzoru, vyplneni sekvenci
v1 = torch.range(1, 12)
print(v1)
print()

# konstrukce prvni matice z puvodniho tenzoru
m1 = torch.reshape(v1, (4, 3))
print(m1)
print()

# konstrukce druhe matice z puvodniho tenzoru
m2 = torch.reshape(v1, (3, 4))
print(m2)
print()

# provedeni maticoveho soucinu
# v opacnem poradi
m3 = m2 @ m1
print(m3)
