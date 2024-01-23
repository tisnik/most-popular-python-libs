#!/usr/bin/env python

from time import perf_counter

import matplotlib.pyplot as plt

import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs


def run_k_means(n_samples):
    # počet oblastí, kam se budou data sdružovat
    n_components = 8

    samples, _ = make_blobs(
        n_samples=n_samples, n_features=3, centers=n_components,
        cluster_std=0.80, random_state=0
    )

    # clustering
    kmeans = KMeans(n_clusters=n_components, random_state=0, n_init="auto").fit(samples)


x = []
y = []

for i in range(10000, 1000000, 10000):
    started = perf_counter()
    run_k_means(i)
    finished = perf_counter()
    duration = finished - started
    x.append(i)
    y.append(duration)
    print(i, duration)

plt.figure(1)
plt.plot(x, y, marker="o")
plt.savefig("benchmark1.png")
plt.show()
