#!/usr/bin/env python

# vykreslování budeme provádět s využitím knihovny Matplotlib
import matplotlib.pyplot as plt

# import funkce, která vrátí obrázky pro práci
from sklearn.datasets import load_digits

# načtení obrázků, s nimiž budeme dále pracovat
digits_data = load_digits()

# celkový počet vzorků
samples = len(digits_data.images)
print("Vzorků celkem:", samples)

# vytvoření seznamu, které použijeme
images = list(zip(digits_data.target, digits_data.images))

# počet vzorků pro trénink
for_training = samples // 2
print("Vzorků pro trénink:", for_training)

# obrázky (ve formě vektoru) a jejich označení
training_images = digits_data.data[:for_training]
training_labels = digits_data.target[:for_training]

# provést klasifikaci
from sklearn import svm
classify = svm.SVC(gamma=0.001)
classify.fit(training_images, training_labels)

# očekávané výsledky vs. výsledky modelu
expexted_labels = digits_data.target[for_training:]
predicted_labels = classify.predict(digits_data.data[for_training:])

# získat predikce modelu
predictions = list(zip(predicted_labels, digits_data.images[for_training:]))


def show_predictions(predictions, from_index, filename):
    # zobrazit patnáct výsledků
    for i, (predicted_digit, image) in enumerate(predictions[from_index:from_index+15]):
        plt.subplot(3,5, i+1)
        plt.axis('off')
        # zobrazení obrázku
        plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
        # a přidání predikce - o jakou číslici se jedná
        plt.title("Predict: %i" % predicted_digit)

    # nakonec vše uložíme a zobrazíme
    plt.savefig(filename)
    plt.show()


show_predictions(predictions, 0, "predictions_1.png")
show_predictions(predictions, 15, "predictions_2.png")

# finito
