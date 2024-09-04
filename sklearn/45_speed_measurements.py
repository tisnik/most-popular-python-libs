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

from time import perf_counter

import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs


def run_k_means(n_samples, std):
    # počet oblastí, kam se budou data sdružovat
    n_components = 8

    samples, _ = make_blobs(
        n_samples=n_samples, n_features=3, centers=n_components,
        cluster_std=std, random_state=0
    )

    # clustering
    kmeans = KMeans(n_clusters=n_components, random_state=0, n_init="auto").fit(samples)
    assert kmeans is not None


x = []
y = []

for i in range(100):
    std = i / 10.0
    started = perf_counter()
    run_k_means(20000, std)
    finished = perf_counter()
    duration = finished - started
    x.append(std)
    y.append(duration)
    print(std, duration)

plt.figure(1)
plt.plot(x, y, marker="o")
plt.savefig("benchmark4.png")
plt.show()
