# Knihovna PyTorch
#
# - konstrukce řezu s jeho následnou modifikací (odlišné operace od předchozího příkladu)

import torch

# konstrukce tenzoru
m1 = torch.Tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print(m1)

print()

# konstrukce rezu - pres radky i sloupce
m2 = m1[::2, ::2]
print(m2)

print()

# konstrukce rezu - pres radky i sloupce
m3 = m1[1::2, 1::2]
print(m3)

print()

# modifikace rezu
m2[0,0] = 99
m2[0,1] = 99
m2[1,0] = 99
m2[1,1] = 99
print(m2)

print()

# vypis puvodniho tenzoru
print(m1)

print()

# modifikace rezu
m3[0,0] = -99
m3[0,1] = -99
m3[1,0] = -99
m3[1,1] = -99
print(m3)

print()

# vypis puvodniho tenzoru
print(m1)
