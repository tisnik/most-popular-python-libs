from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split
import torch
import numpy as np
from torch.utils.data import Dataset, DataLoader


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


def compute_train_and_test_data(
    n_samples=2000, factor=0.5, noise=0.05, test_size=1 / 3
):
    samples, labels = make_circles(n_samples=n_samples, factor=factor, noise=noise)

    # rozdělení na trénovací a testovací množinu
    X_train, X_test, y_train, y_test = train_test_split(
        samples, labels, test_size=test_size, random_state=26
    )

    # trénovací a testovací sada

    # trénovací sada
    train_data = Data(X_train, y_train)

    # testovací sada
    test_data = Data(X_test, y_test)

    return train_data, test_data
