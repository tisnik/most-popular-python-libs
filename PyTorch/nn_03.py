from torch import nn
from torch import optim
from torch.utils.data import DataLoader


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
nn3 = NeuralNetwork(input_dim, output_dim)

# výpis základních informací o neuronové síti
print(nn3)


# příprava na trénink neuronové sítě
learning_rate = 0.1
loss_fn = nn.BCELoss()

optimizer = optim.SGD(nn3.parameters(), lr=learning_rate)

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
        pred = nn3(X)

        # výpočet účelové funkce
        loss = loss_fn(pred, y.unsqueeze(-1))
        loss_values.append(loss.item())
        loss.backward()
        optimizer.step()
        last_lost_value = loss.item()
        print(".", end="")
    print(last_lost_value)

print("Training completed")

print("Loss values")
for i, loss_value in enumerate(loss_values):
    print(i, loss_value)
