import torch

# konstrukce tenzoru druheho radu
# s vynulovanim vsech prvku
m1 = torch.Tensor(5, 5).zero_()
print(m1)
print()

# vyplneni radku matice
m1.narrow(0, 2, 1).fill_(3)
print(m1)
print()

# vyplneni sloupce matice
m1.narrow(1, 2, 1).fill_(9)
print(m1)
print()

# vyplneni strednich 3x3 prvku matice
m1.narrow(1, 1, 3).narrow(0, 1, 3).fill_(1)
print(m1)
print()

