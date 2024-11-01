import torch

# konstrukce tenzoru
s3 = torch.Tensor(1).zero_()
print(s3)

# pristup k (jedine) slozce tenzoru
s3[0] = 42
print(s3)

# toto je skutecny skalar
s4 = torch.tensor(1).zero_()
print(s4)
