# budeme provádět vykreslování de facto standardní knihovnou Matplotlib
import matplotlib.pyplot as plt

# třída s implementací algoritmu pro clustering
from sklearn.cluster import KMeans

# import funkce, která dokáže vygenerovat množinu bodů v rovině sdružených do oblastí
from sklearn.datasets import make_blobs

# testovací data
n_samples = 10000

# počet oblastí, kam se budou data sdružovat
n_components = 6

# vygenerovat množinu bodů v rovině sdružených do oblastí
samples, labels = make_blobs(
    n_samples=n_samples, centers=n_components, cluster_std=2.00, random_state=0
)

samples = samples[:, ::-1]

plt.figure(1)
colors = ["#4444cc", "#44bb44", "#cc4444", "#cccc44", "#44cccc", "#cc44cc"]

# clustering
kmeans = KMeans(n_clusters=6, random_state=0, n_init="auto").fit(samples)

#print(kmeans.labels_)
#print(kmeans.cluster_centers_)

# vykreslení bodů s jejich přiřazením ke clusteru
for i, color in enumerate(colors):
    selector = kmeans.labels_ == i
    plt.scatter(samples[selector, 0], samples[selector, 1], c=color, marker=".", s=1)

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c="red", s=50)
plt.title("K-Means++")

# uložení grafu do souboru
plt.savefig("k_means_4.png")

# vykreslení na obrazovku
plt.show()
