import random
from sklearn.model_selection import train_test_split
import torch
from torch import nn
from torch import optim
from torch.utils.data import Dataset, DataLoader
import numpy as np
import matplotlib.pyplot as plt


class NeuralNetwork(nn.Module):
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


# konfigurace vrstev neuronové sítě
input_dim = 64
hidden_dim = 10
output_dim = 10

nn_64_10_10 = NeuralNetwork(input_dim, hidden_dim, output_dim)

# výpis základních informací o neuronové síti
print("Neural network:")
print(nn_64_10_10)


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


# číslice reprezentované v masce 8x8 pixelů
digits = (
    (0x00, 0x3C, 0x66, 0x76, 0x6E, 0x66, 0x3C, 0x00),
    (0x00, 0x18, 0x1C, 0x18, 0x18, 0x18, 0x7E, 0x00),
    (0x00, 0x3C, 0x66, 0x30, 0x18, 0x0C, 0x7E, 0x00),
    (0x00, 0x7E, 0x30, 0x18, 0x30, 0x66, 0x3C, 0x00),
    (0x00, 0x30, 0x38, 0x3C, 0x36, 0x7E, 0x30, 0x00),
    (0x00, 0x7E, 0x06, 0x3E, 0x60, 0x66, 0x3C, 0x00),
    (0x00, 0x3C, 0x06, 0x3E, 0x66, 0x66, 0x3C, 0x00),
    (0x00, 0x7E, 0x60, 0x30, 0x18, 0x0C, 0x0C, 0x00),
    (0x00, 0x3C, 0x66, 0x3C, 0x66, 0x66, 0x3C, 0x00),
    (0x00, 0x3C, 0x66, 0x7C, 0x60, 0x30, 0x1C, 0x00),
)


def digit_to_array(digits, n):
    digit = digits[n]
    rows = []
    # převod jednotlivých řádků na osmici bitů
    for scanline in digit:
        row = []
        # převod bitmapy představující řádek na osmici bitů
        for _ in range(8):
            bit = scanline & 0x01
            row.append(float(bit))
            scanline >>= 1
        rows.append(row)
    # transformace na n-dimenzionální pole
    return np.array(rows)


def add_noise(array, level):
    return (1.0 - level) * array + level * np.random.rand(8, 8)


def shift(arr, x_shift, y_shift):
    # horizontální posun
    arr = np.roll(arr, x_shift, axis=1)

    # výplně těch částí, které byly orotovány na druhou stranu
    if x_shift < 0:
        arr[:, x_shift:] = 0.0
    elif x_shift > 0:
        arr[:, :x_shift] = 0.0

    # vertikální posun
    arr = np.roll(arr, y_shift, axis=0)

    # výplně těch částí, které byly orotovány na druhou stranu
    if y_shift < 0:
        arr[y_shift:] = 0.0
    elif y_shift > 0:
        arr[:y_shift] = 0.0
    return arr


def prepare_data(digits, length, noise_level=0.0, x_shift_amount=0, y_shift_amount=0, test_size=1/3):
    # příprava dat pro trénink a testování
    X = []
    y = []

    for i in range(length):
        # cislice
        digit = i % 10
        # vstupy
        array = digit_to_array(digits, digit)
        # zasumeni
        array = add_noise(array, noise_level)
        # posuny
        x_shift = random.randint(-x_shift_amount, x_shift_amount)
        y_shift = random.randint(-y_shift_amount, y_shift_amount)
        array = shift(array, x_shift, y_shift)
        # prevod na vektor
        x_vector = array.flatten()
        X.append(x_vector)
        # očekávané výstupy
        y_vector = [0.0] * 10
        y_vector[digit] = 1.0
        y.append(y_vector)

    X_train, X_test, y_train, y_test = train_test_split(
        np.array(X), np.array(y),
        test_size=test_size, random_state=26
    )

    # trénovací sada
    train_data = Data(X_train, y_train)

    # testovací sada
    test_data = Data(X_test, y_test)

    return train_data, test_data


train_data, test_data = prepare_data(digits, 1000, noise_level=0.0, x_shift_amount=3, y_shift_amount=3)
print("Train data:")
print(len(train_data))
print("Test data:")
print(len(test_data))

# příprava na trénink neuronové sítě
learning_rate = 0.1
loss_fn = nn.BCELoss()

optimizer = optim.SGD(nn_64_10_10.parameters(), lr=learning_rate)

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
        pred = nn_64_10_10(X)

        # výpočet účelové funkce
        loss = loss_fn(pred, y)

        #loss = loss_fn(pred, y.unsqueeze(-1))
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
plt.ylabel("Chyba")

# uložení do souboru
plt.savefig("nn_18_.png")

# vykreslení grafu
plt.show()
