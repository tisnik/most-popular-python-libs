# Knihovna PyTorch
#
# - zjištění, jestli je možné výpočty použít pro platformu MPS

import torch

print("MPS available:", torch.backends.mps.is_available())
