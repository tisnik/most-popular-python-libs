import numpy as np
from sklearn.model_selection import KFold

k_fold = KFold(n_splits=3, shuffle=False)

print(k_fold)

X = 1000 * np.linspace(1, 10, 10)
print(f"Original X: {X}")

for i, (train_index, test_index) in enumerate(k_fold.split(X)):
    print(f"Fold {i}:")
    print(f"  Train data: index={X[train_index]}")
    print(f"  Test data:  index={X[test_index]}")
