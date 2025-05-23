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
m2 = torch.Tensor([[[ 1,  1], [ 1,  1], [ 1,  1]],
                   [[ 2,  2], [ 2,  2], [ 2,  2]],
                   [[-1, -1], [-1, -2], [-1, -1]]])
print(m2)
print()

# pokus o provedeni maticoveho soucinu s broadcastem
m3 = m1 @ m2
print(m3)
