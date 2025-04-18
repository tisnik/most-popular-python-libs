from torch import nn


class NeuralNetwork(nn.Module):
    """Třída reprezentující neuronovou síť."""

    def __init__(self, input_dim, output_dim):
        super().__init__()
        # vrstvy neuronové sítě
        self.layer_1 = nn.Linear(input_dim, output_dim)

    def forward(self, x):
        # propagace hodnot přes neuronvou síť
        x = nn.functional.sigmoid(self.layer_1(x))
        return x


# konfigurace vrstev neuronové sítě
input_dim = 2
output_dim = 1

# konstrukce neuronové sítě
nn2 = NeuralNetwork(input_dim, output_dim)

# výpis základních informací o neuronové síti
print(nn2)
