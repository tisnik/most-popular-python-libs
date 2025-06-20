import torch
from torch.utils.data import Dataset

import numpy as np


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


def prepare_data(digits, length):
    # příprava dat pro trénink a testování
    X = []
    y = []

    for i in range(length):
        # cislice
        digit = i % 10
        # vstupy
        array = digit_to_array(digits, digit)
        # prevod na vektor
        x_vector = array.flatten()
        X.append(x_vector)
        # očekávané výstupy
        y_vector = [0.0] * 10
        y_vector[digit] = 1.0
        y.append(y_vector)

    return Data(np.array(X), np.array(y))


data = prepare_data(digits, 1000)
print(len(data))

for i in range(10):
    print(data[i])
