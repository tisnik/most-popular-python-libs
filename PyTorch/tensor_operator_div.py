import torch

# konstrukce tenzoru, vyplneni sekvenci
v1 = torch.range(1, 12)
print(v1)
print()

# konstrukce 2D matice z puvodniho vektoru
m1 = torch.reshape(v1, (4, 3))
print(m1)
print()

# vytvořeni druhe matice se stejnym tvarem
m2 = torch.ones(4, 3) + torch.ones(4, 3)
print(m2)
print()

# podil metodou prvek po prvku
m3 = m1 / m2
print(m3)
print()
