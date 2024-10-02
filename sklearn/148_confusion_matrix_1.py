import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import ConfusionMatrixDisplay

# nacteni datove sady
iris = load_iris()

# X je matice (feature matrix)
X = iris.data

# y je vektor (response vector)
y = iris.target

# rozdělení dat
trainX, testX, trainY, testY = train_test_split(X, y, test_size = 0.7)

# konstrukce klasifikatoru
# (s hyperparametrem)
classifier = LogisticRegression(max_iter=1000)

# trening modelu (se vsemi dostupnymi daty)
classifier.fit(trainX, trainY)

y_pred = classifier.predict(testX)

print(classification_report(testY, y_pred))

class_names = iris.target_names

# absolutni hodnoty
disp = ConfusionMatrixDisplay.from_estimator(
    classifier,
    testX,
    testY,
    display_labels=class_names,
    cmap=plt.cm.Blues,
    normalize=None,
)

# zobrazeni matice
print(disp.confusion_matrix)

# ulozeni vysledku
plt.savefig("148_1.png")

# vizualizace matice
plt.show()

# relativni hodnoty
disp = ConfusionMatrixDisplay.from_estimator(
    classifier,
    testX,
    testY,
    display_labels=class_names,
    cmap=plt.cm.Blues,
    normalize="true",
)

# zobrazeni matice
print(disp.confusion_matrix)

# ulozeni vysledku
plt.savefig("148_2.png")

# vizualizace matice
plt.show()