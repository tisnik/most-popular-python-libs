import torch

# konstrukce tenzoru (matice 4x4 prvky)
m1 = torch.Tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print(m1)
print()

# pohled na původní matici
m2 = torch.narrow(m1, 1, 1, 2)
print(m2)
print()

# pohled na pohled
m3 = torch.narrow(m2, 0, 1, 2)
print(m3)
print()
