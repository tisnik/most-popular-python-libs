from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans

iris = load_iris()

data = iris.data

plt.figure(1)
colors = ["#4444cc", "#cc4444", "#cccc44", "#44cccc", "#cc44cc"]

# clustering
kmeans = KMeans(n_clusters=3, random_state=0, n_init="auto").fit(data)

# vykreslení bodů s jejich přiřazením ke clusteru
for i, color in enumerate(colors):
    selector = kmeans.labels_ == i
    plt.scatter(data[selector, 0], data[selector, 1], c=color, marker=".", s=20)

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c="red", s=100)
plt.title("K-Means++")

# uložení grafu do souboru
plt.savefig("iris_kmeans_1.png")

# vykreslení na obrazovku
plt.show()
