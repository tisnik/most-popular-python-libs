import torch
from torch import nn
from torch import optim
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
import numpy as np


class NeuralNetwork4(nn.Module):
    """Třída reprezentující neuronovou síť."""

    def __init__(self, input_dim, output_dim):
        super().__init__()
        # vrstvy neuronové sítě
        self.layer_1 = nn.Linear(input_dim, output_dim)

    def forward(self, x):
        # propagace hodnot přes neuronovou síť
        x = nn.functional.sigmoid(self.layer_1(x))
        return x


class NeuralNetwork5(nn.Module):
    """Třída reprezentující neuronovou síť."""

    def __init__(self, input_dim, hidden_dim, output_dim):
        super().__init__()
        # vrstvy neuronové sítě
        self.layer_1 = nn.Linear(input_dim, hidden_dim)
        self.layer_2 = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        # propagace hodnot přes neuronovou síť
        x = torch.nn.functional.relu(self.layer_1(x))
        x = torch.nn.functional.sigmoid(self.layer_2(x))
        return x


# konstrukce dvou neuronových sítí
nn4 = NeuralNetwork4(2, 1)
nn5 = NeuralNetwork5(2, 10, 1)

# příprava na trénink neuronové sítě
learning_rate = 0.1
loss_fn = nn.BCELoss()

optimizer4 = optim.SGD(nn4.parameters(), lr=learning_rate)
optimizer5 = optim.SGD(nn5.parameters(), lr=learning_rate)

# trénovací data
from compute_train_and_test_data import compute_train_and_test_data

train_data, _ = compute_train_and_test_data()

# zpracovat trénovací data
batch_size = 64
train_dataloader = DataLoader(dataset=train_data, batch_size=batch_size, shuffle=True)
print("Batches: ", len(train_dataloader))

# vlastní trénink
print("Training started")
num_epochs = 100
loss_values_4 = []
loss_values_5 = []
for epoch in range(num_epochs):
    print(f"    Epoch {epoch}: ", end="")
    for X, y in train_dataloader:
        optimizer4.zero_grad()

        # dopředný tok + zpětný tok + optimalizace
        pred = nn4(X)

        # výpočet účelové funkce
        loss = loss_fn(pred, y.unsqueeze(-1))
        loss_values_4.append(loss.item())
        loss.backward()
        optimizer4.step()

        optimizer5.zero_grad()

        # dopředný tok + zpětný tok + optimalizace
        pred = nn5(X)

        # výpočet účelové funkce
        loss = loss_fn(pred, y.unsqueeze(-1))
        loss_values_5.append(loss.item())
        loss.backward()
        optimizer5.step()
        print(".", end="")
    print()

print("Training completed")

step = range(len(loss_values_4))

# příprava na vykreslení grafu
fig, ax = plt.subplots(figsize=(6.4, 4.8))
plt.plot(step, np.array(loss_values_4), label="nn4")
plt.plot(step, np.array(loss_values_5), label="nn5")
plt.title("Průběh tréninku neuronové sítě")
plt.xlabel("Epocha")
plt.ylabel("Účelová funkce")
plt.legend(loc="best")

# uložení do souboru
plt.savefig("nn_4_5.png")

# vykreslení grafu
plt.show()
