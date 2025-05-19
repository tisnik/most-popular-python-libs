# Knihovna PyTorch
#
import torch

# konstrukce tenzoru (matice 4x4 prvky)
m1 = torch.Tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print(m1)

print()

# realizace operace narrow s výběrem dimenze číslo 1
m2 = torch.narrow(m1, 1, 1, 2)
print(m2)

print()

# modifikace puvodni matice pres jeji pohled
m2[0, 0] = 99
print(m1)
print()
print(m2)

