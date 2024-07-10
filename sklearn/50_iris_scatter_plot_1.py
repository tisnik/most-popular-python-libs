from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris = load_iris()

data = iris.data

plt.scatter(data[:, 0], data[:, 1], c=iris.target)
plt.title("Classes")
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.show()
