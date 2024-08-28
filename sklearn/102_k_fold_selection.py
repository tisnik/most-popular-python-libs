#
#  (C) Copyright 2024  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

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
