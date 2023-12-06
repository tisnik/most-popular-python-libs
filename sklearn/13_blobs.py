#!/usr/bin/env python

#
#  (C) Copyright 2021  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

# import funkce, která dokáže vygenerovat množinu bodů v rovině sdružených do oblastí
from sklearn.datasets import make_blobs

# testovací data
n_samples = 20

# počet oblastí, kam se budou data sdružovat
n_components = 6

# vygenerovat množinu bodů v rovině sdružených do oblastí
samples, labels = make_blobs(
    n_samples=n_samples, centers=n_components, cluster_std=0.60, random_state=0
)

print("Before swap:")
print(samples)
print()

print("Labels:")
print(labels)
