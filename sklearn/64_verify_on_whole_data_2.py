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

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

import numpy as np

# nacteni datove sady
iris = load_iris()


# konstrukce klasifikatoru
# (s hyperparametrem)
classifier = KNeighborsClassifier(n_neighbors=1)

# X je matice (feature matrix)
X = iris.data

# y je vektor (response vector)
y = iris.target

# trening modelu (se vsemi dostupnymi daty)
classifier.fit(X, y)

# očekávané výsledky
expexted_labels = iris.target

# výsledky modelu (predikované výsledky)
predicted_labels = classifier.predict(iris.data)

# jak je náš model úspěšný?
print(metrics.accuracy_score(expexted_labels, predicted_labels))

# finito
