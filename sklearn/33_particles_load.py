# budeme provádět vykreslování de facto standardní knihovnou Matplotlib
import matplotlib.pyplot as plt

# knihovnu Pandas využijeme pro načtení datového rámce
import pandas as pd

df = pd.read_csv("particles.csv")

# vykreslení bodů v rovině
plt.scatter(df["x"], df["y"], s=1)

# uložení grafu do souboru
plt.savefig("particles.png")

# vykreslení na obrazovku
plt.show()
