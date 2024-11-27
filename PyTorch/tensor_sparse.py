import torch

m1 = torch.tensor([[0, 1, 0, 0], [1, 2, 0, 0], [0, 0, 1, 0]])
print(m1)
print()

sparse = m1.to_sparse()
print(sparse)
