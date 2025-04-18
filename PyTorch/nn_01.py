from torch import nn


class NeuralNetwork(nn.Module):
    """Třída reprezentující neuronovou síť."""

    def __init__(self):
        super().__init__()


# konstrukce neuronové sítě
nn1 = NeuralNetwork()

# výpis základních informací o neuronové síti
print(nn1)
