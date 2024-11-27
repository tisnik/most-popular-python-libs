import torch

# konstrukce tenzoru, vyplneni sekvenci
v1 = torch.arange(1, 13)
print(v1)
print()

# tenzor druhého řádu
m1 = torch.reshape(v1, (4, 3))
print(m1)
print()

# tenzor třetího řádu
c1 = torch.ones(5, 4, 3)
print(c1)
print()

print(m1 + c1)
