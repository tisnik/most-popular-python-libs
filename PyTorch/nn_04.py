from torch import nn, optim
from torch.utils.data import DataLoader

import matplotlib.pyplot as plt
import numpy as np


class NeuralNetwork(nn.Module):
    """Třída reprezentující neuronovou síť."""

    def __init__(self, input_dim, output_dim):
        super().__init__()
        # vrstvy neuronové sítě
        self.layer_1 = nn.Linear(input_dim, output_dim)

    def forward(self, x):
        # propagace hodnot přes neuronovou síť
        x = nn.functional.sigmoid(self.layer_1(x))
        return x


# konfigurace vrstev neuronové sítě
input_dim = 2
output_dim = 1

# konstrukce neuronové sítě
nn4 = NeuralNetwork(input_dim, output_dim)

# výpis základních informací o neuronové síti
print(nn4)


# příprava na trénink neuronové sítě
learning_rate = 0.1
loss_fn = nn.BCELoss()

optimizer = optim.SGD(nn4.parameters(), lr=learning_rate)

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
loss_values = []
for epoch in range(num_epochs):
    print(f"    Epoch {epoch}: ", end="")
    last_lost_value = None
    for X, y in train_dataloader:
        optimizer.zero_grad()

        # dopředný tok + zpětný tok + optimalizace
        pred = nn4(X)

        # výpočet účelové funkce
        loss = loss_fn(pred, y.unsqueeze(-1))
        loss_values.append(loss.item())
        loss.backward()
        optimizer.step()
        last_lost_value = loss.item()
        print(".", end="")
    print(last_lost_value)

print("Training completed")

step = range(len(loss_values))

# příprava na vykreslení grafu
fig, ax = plt.subplots(figsize=(6.4, 4.8))
plt.plot(step, np.array(loss_values))
plt.title("Průběh tréninku neuronové sítě")
plt.xlabel("Epocha")
plt.ylabel("Účelová funkce")

# uložení do souboru
plt.savefig("nn_4.png")

# vykreslení grafu
plt.show()
