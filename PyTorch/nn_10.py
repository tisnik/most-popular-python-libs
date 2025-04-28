import torch
from torch import nn
from torch import optim
from torch.utils.data import Dataset, DataLoader
import numpy as np



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
        x = torch.nn.functional.sigmoid(self.layer_1(x))
        x = torch.nn.functional.sigmoid(self.layer_2(x))
        x = torch.nn.functional.sigmoid(self.layer_3(x))
        return x


# konfigurace vrstev neuronové sítě
input_dim = 2
hidden_dim = 4
output_dim = 2

# konstrukce neuronové sítě
nn1 = NeuralNetwork(input_dim, hidden_dim, output_dim)

# výpis základních informací o neuronové síti
print(nn1)


# příprava na trénink neuronové sítě
learning_rate = 0.1
loss_fn = nn.BCELoss()

optimizer = optim.SGD(nn1.parameters(), lr=learning_rate)


# konverze původních dat z NumPy do tenzorů
class Data(Dataset):
    def __init__(self, X, y):
        self.X = torch.from_numpy(X.astype(np.float32))
        self.y = torch.from_numpy(y.astype(np.float32))
        self.len = self.X.shape[0]

    def __getitem__(self, index):
        return self.X[index], self.y[index]

    def __len__(self):
        return self.len


# příprava trénovacích dat
X_train = []
y_train = []

for a in np.linspace(0, 1.0, 101):
    for b in np.linspace(0, 1.0, 101):
        # vstupy
        X_train.append([a, b])
        # očekávané výstupy
        y_train.append([1.0 if a>b else 0.0, 1.0 if abs(a-b)<0.2 else 0.0])

train_data = Data(np.array(X_train), np.array(y_train))

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
        pred = nn1(X)

        # výpočet účelové funkce
        loss = loss_fn(pred, y)#.unsqueeze(-1))
        loss_values.append(loss.item())
        loss.backward()
        optimizer.step()
        last_lost_value = loss.item()
        print(".", end="")
    print(last_lost_value)

print("Training completed")

# naivní otestování neuronové sítě
for x in np.linspace(0, 1, 11):
    X = torch.tensor([float(x), 1.0-float(x)])
    y = nn1(X)
    gt = y[0] >= 0.5
    eq = y[1] >= 0.5
    relation = "?"
    if eq:
        relation = "=="
    elif gt:
        relation = "> "
    else:
        relation = "< "
    print(f"{x:4.3} {relation} {1.0-x:4.3}")
