import matplotlib.pyplot as plt

from sklearn.cluster import kmeans_plusplus
from sklearn.datasets import make_blobs

# testovací data
n_samples = 20

# počet oblastí, kam se budou data sdružovat
n_components = 6

samples, labels = make_blobs(
    n_samples=n_samples, centers=n_components, cluster_std=0.60, random_state=0
)

print("Before swap:")
print(samples)
print()

print("Labels:")
print(labels)
