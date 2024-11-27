import torch

# konstrukce tenzoru - vektoru s deseti prvky
v1 = torch.Tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(v1)

print()

# realizace operace narrow s výběrem dimenze číslo 0
v2 = torch.narrow(v1, 0, 1, 8)
print(v2)

print()

# modifikace vektoru pres pohled na nej
v2[0] = 99
print(v1)
print()
print(v2)

