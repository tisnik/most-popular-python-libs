# Zjisteni, jestli je mozne pro vypocty pouzit platformu MPS

import torch

print("MPS available:", torch.backends.mps.is_available())
