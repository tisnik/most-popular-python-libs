# Knihovna PyTorch
#
import torch

# konstrukce tenzoru tretiho radu
# vynulovanim vsech prvku
c = torch.Tensor(2, 3, 4).zero_()
print(c)
