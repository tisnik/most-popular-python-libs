import torch
from torch.utils.data import DataLoader, Dataset

import numpy as np
from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split


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


batch_size = 64

# testovací data
n_samples = 2000

samples, labels = make_circles(
    n_samples=n_samples, factor=0.5, noise=0.05
)

# rozdělení na trénovací a testovací množinu
X_train, X_test, y_train, y_test = train_test_split(samples, labels, test_size=1/3, random_state=26)

# trénovací a testovací sada

# trénovací sada
train_data = Data(X_train, y_train)
train_dataloader = DataLoader(dataset=train_data, batch_size=batch_size, shuffle=True)

# testovací sada
test_data = Data(X_test, y_test)
test_dataloader = DataLoader(dataset=test_data, batch_size=batch_size, shuffle=True)

# otestování funkcionality
for batch, (X, y) in enumerate(train_dataloader):
    print(f"Dávka: {batch+1}")
    print(f"X shape: {X.shape}")
    print(f"y shape: {y.shape}")
    print()
