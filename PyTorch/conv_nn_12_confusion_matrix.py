import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

y_pred = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y_test = [0, 1, 2, 8, 4, 5, 6, 7, 6, 9, 0, 1, 2, 2, 4, 5, 8, 7, 8, 9]

# výpočet matice záměn
disp = ConfusionMatrixDisplay.from_predictions(
    y_test, y_pred,
    cmap=plt.cm.Blues,
    normalize=None,
)

# zobrazení matice záměn
print(disp.confusion_matrix)

# uložení výsledků
plt.savefig("confusion_matrix.png")

# vykreslení matice záměn
plt.show()
