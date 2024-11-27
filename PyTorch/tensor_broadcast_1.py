import torch

# konstrukce tenzoru, vyplneni sekvenci
v1 = torch.arange(1, 13)
print(v1)
print()

# vytvoreni matice z puvodniho vektoru
m1 = torch.reshape(v1, (4, 3))
print(m1)
print()

# vynasobeni kazdeho prvku matice skalarem
m2 = m1 * 10
print(m2)
print()
