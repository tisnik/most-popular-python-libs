# Knihovna PyTorch
#
# - zjištění, jestli je možné výpočty použít pro platformu CUDA

import torch

print("CUDA available:", torch.cuda.is_available())
