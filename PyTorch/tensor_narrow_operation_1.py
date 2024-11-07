import torch

# konstrukce tenzoru
m1 = torch.Tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print(m1)

print()

m2 = torch.narrow(m1, 0, 1, 2)
print(m2)

print()

m2[0, 0] = 99
print(m1)
print()
print(m2)

