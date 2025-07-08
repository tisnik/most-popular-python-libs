import math

import torch
from torch import nn

l = nn.Linear(2, 2)

phi = 90
cos_phi = math.cos(math.radians(phi))
sin_phi = math.sin(math.radians(phi))

rotation_matrix = [
        [cos_phi, -sin_phi],
        [sin_phi,  cos_phi],
        ]

translation_vector = [0.0, 0.0]

l.weight = nn.Parameter(data=torch.tensor(rotation_matrix))
l.bias = nn.Parameter(data=torch.tensor(translation_vector))

x = torch.tensor([1.0, 2.0])
y = l(x)

print(y)
