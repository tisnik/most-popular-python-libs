import torch
from torch import nn


class NeuralNetwork(nn.Module):
    """Třída reprezentující neuronovou síť."""

    def __init__(self, input_dim, output_dim):
        super().__init__()
        # vrstvy neuronové sítě
        self.layer_1 = nn.Linear(input_dim, output_dim)
        self.layer_1.weight = nn.Parameter(data=torch.tensor([[2.0]]))
        self.layer_1.bias = nn.Parameter(data=torch.tensor([10.0]))

    def forward(self, x):
        # propagace hodnot přes neuronovou síť
        return self.layer_1(x)


# konfigurace vrstev neuronové sítě
input_dim = 1
output_dim = 1

# konstrukce neuronové sítě
nn1 = NeuralNetwork(input_dim, output_dim)

# výpis základních informací o neuronové síti
print("Neural network:", nn1)
print()

# výpis informace o vrstvě neuronové sítě
print("Layer 1:", nn1.layer_1)
print()

# výpis informace o transformační matici a biasech
print("Weights:", nn1.layer_1.weight)
print("Bias:", nn1.layer_1.bias)
print()

with torch.no_grad():
    X = torch.reshape(torch.arange(1.0, 11), (10, 1))
    output = nn1(X)
    print(output)
