import itertools

import torch
from torch import nn, optim
from torch.utils.data import DataLoader

import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import ConfusionMatrixDisplay


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
nn10 = NeuralNetwork(input_dim, hidden_dim, output_dim)

# výpis základních informací o neuronové síti
print(nn10)


# příprava na trénink neuronové sítě
learning_rate = 0.1
loss_fn = nn.BCELoss()

optimizer = optim.SGD(nn10.parameters(), lr=learning_rate)

# trénovací data
from compute_train_and_test_data import compute_train_and_test_data

train_data, test_data = compute_train_and_test_data()

# zpracovat trénovací data
batch_size = 64
train_dataloader = DataLoader(dataset=train_data, batch_size=batch_size, shuffle=True)
print("Batches: ", len(train_dataloader))

# vlastní trénink
print("Training started")
num_epochs = 75
loss_values = []
for epoch in range(num_epochs):
    print(f"    Epoch {epoch}: ", end="")
    last_lost_value = None
    for X, y in train_dataloader:
        optimizer.zero_grad()

        # dopředný tok + zpětný tok + optimalizace
        pred = nn10(X)

        # výpočet účelové funkce
        loss = loss_fn(pred, y.unsqueeze(-1))
        loss_values.append(loss.item())
        loss.backward()
        optimizer.step()
        last_lost_value = loss.item()
        print(".", end="")
    print(last_lost_value)

print("Training completed")
print()

test_dataloader = DataLoader(dataset=test_data, batch_size=batch_size, shuffle=True)


# otestování neuronové sítě
y_pred = []
y_test = []

with torch.no_grad():
    for X, y in test_dataloader:
        outputs = nn10(X)
        # hodnoty 0 nebo 1
        predicted = np.where(outputs.numpy() < 0.5, 0, 1)
        predicted = list(itertools.chain(*predicted))
        y_pred.append(predicted)
        y_test.append(y.numpy())

# převod na běžné seznamy
y_pred = list(itertools.chain(*y_pred))
y_test = list(itertools.chain(*y_test))

# výpočet matice záměn
disp = ConfusionMatrixDisplay.from_predictions(
    y_test, y_pred,
    cmap=plt.cm.Blues,
    normalize=None,
)

# zobrazení matice záměn
print(disp.confusion_matrix)

# uložení výsledků
plt.savefig("confusion_matrix.png")

# vykreslení matice záměn
plt.show()
