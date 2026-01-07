import torch
from torch import optim
from torch import nn


class NeuralNetwork(nn.Module):
    """Třída reprezentující neuronovou síť."""

    def __init__(self, input_dim, output_dim):
        super().__init__()
        # vrstvy neuronové sítě
        self.layer_1 = nn.Linear(input_dim, output_dim)
        self.layer_1.weight = nn.Parameter(data=torch.tensor([[0.]]))
        self.layer_1.bias = nn.Parameter(data=torch.tensor([0.]))

    def forward(self, x):
        # propagace hodnot přes neuronovou síť
        x = nn.functional.sigmoid(self.layer_1(x))
        return x


def nn_predictions(nn):
    with torch.no_grad():
        X = torch.reshape(torch.arange(start=0.0, end=1.0, step=0.1), (10, 1))
        output = nn1(X)
        print(output-X)


def nn_max_diff(nn):
    with torch.no_grad():
        X = torch.reshape(torch.arange(start=0.0, end=1.0, step=0.1), (10, 1))
        output = nn1(X)
        max = torch.max(torch.abs(output-X))
        print(max)


def print_layers(nn):
    """Výpis informace o transformační matici a biasech."""
    l1 = nn.layer_1
    print(f"Weight: {l1.weight[0].item()}   Bias: {l1.bias[0].item()}")


def train(nn1, optimizer, loss_fn, X, y):
    optimizer.zero_grad()
    # dopředný tok + zpětný tok + optimalizace
    pred = nn1(X)

    # výpočet účelové funkce
    loss = loss_fn(pred, y)
    loss.backward()
    optimizer.step()

    return loss.item()


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

print_layers(nn1)
nn_max_diff(nn1)
nn_predictions(nn1)

# příprava na trénink neuronové sítě
learning_rate = 0.2
loss_fn = nn.BCELoss()

optimizer = optim.SGD(nn1.parameters(), lr=learning_rate)


X = torch.tensor([1.0])
y = torch.tensor([1.0])

for i in range(4):
    loss = train(nn1, optimizer, loss_fn, X, y)
    print(loss, end="   ")

    print_layers(nn1)
    nn_max_diff(nn1)
    nn_predictions(nn1)
    print()
