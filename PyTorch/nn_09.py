import torch
from torch import nn
from torch import optim
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
import numpy as np

# budeme provádět vykreslování de facto standardní knihovnou Matplotlib
import matplotlib.pyplot as plt


class NeuralNetwork(nn.Module):
    """Třída reprezentující neuronovou síť."""

    def __init__(self, input_dim, hidden_dim, output_dim):
        super().__init__()
        # vrstvy neuronové sítě
        self.layer_1 = nn.Linear(input_dim, hidden_dim)
        self.layer_2 = nn.Linear(hidden_dim, hidden_dim)
        self.layer_3 = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        # propagace hodnot přes neuronovou síť
        x = torch.nn.functional.relu(self.layer_1(x))
        x = torch.nn.functional.sigmoid(self.layer_2(x))
        x = torch.nn.functional.sigmoid(self.layer_3(x))
        return x


# konfigurace vrstev neuronové sítě
input_dim = 2
hidden_dim = 10
output_dim = 1

# konstrukce neuronové sítě
nn9 = NeuralNetwork(input_dim, hidden_dim, output_dim)

# výpis základních informací o neuronové síti
print(nn9)


# příprava na trénink neuronové sítě
learning_rate = 0.1
loss_fn = nn.BCELoss()

optimizer = optim.SGD(nn9.parameters(), lr=learning_rate)

# trénovací data
from compute_train_and_test_data import compute_train_and_test_data

train_data, test_data = compute_train_and_test_data()

# zpracovat trénovací data
batch_size = 64
train_dataloader = DataLoader(dataset=train_data, batch_size=batch_size, shuffle=True)
print("Batches: ", len(train_dataloader))

# vlastní trénink
print("Training started")
num_epochs = 200
loss_values = []
for epoch in range(num_epochs):
    print(f"    Epoch {epoch}: ", end="")
    last_lost_value = None
    for X, y in train_dataloader:
        optimizer.zero_grad()

        # dopředný tok + zpětný tok + optimalizace
        pred = nn9(X)

        # výpočet účelové funkce
        loss = loss_fn(pred, y.unsqueeze(-1))
        loss_values.append(loss.item())
        loss.backward()
        optimizer.step()
        last_lost_value = loss.item()
        print(".", end="")
    print(last_lost_value)

print("Training completed")

test_dataloader = DataLoader(dataset=test_data, batch_size=batch_size, shuffle=True)

import itertools

all_predicts = []
x_coords = []
y_coords = []

with torch.no_grad():
    for X, y in test_dataloader:
        outputs = nn9(X)
        predicted = np.where(outputs.numpy() < 0.5, 0, 1)
        predicted = list(itertools.chain(*predicted))
        all_predicts += predicted
        coords = X.tolist()
        for coord in coords:
            x_coords.append(coord[0])
            y_coords.append(coord[1])

# velikost obrázku s grafem
plt.subplots(figsize=(6.4, 6.4))

# vizualizace
plt.scatter(x_coords, y_coords, s=1.5, c=all_predicts, cmap=plt.cm.Set1)
# 333test_ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=plt.cm.Set1)
plt.title("Predikované výsledky")

# uložení grafu do souboru
plt.savefig("nn_9.png")

# vykreslení na obrazovku
plt.show()
