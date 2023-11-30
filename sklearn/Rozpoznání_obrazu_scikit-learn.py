#!/usr/bin/env python
# coding: utf-8

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

# # Rozpoznání obrazu s využitím knihovny scikit-learn

# ## Importy všech knihoven

# Vykreslování budeme provádět přes de facto standardní knihovnu Matplotlib

# In[5]:


import matplotlib.pyplot as plt


# Práci s n-dimenzionálními poli zajišťuje knihovna NumPy

# In[6]:


import numpy as np


# ## Vizualizace dvourozměrných polí

# In[8]:


# vytvoření matice, kterou budeme vizualizovat
array = np.random.rand(10, 10)

# vykreslení
plt.matshow(array)

# uložení vizualizované matice do souboru
plt.savefig("random.png")

# vizualizace na obrazovku
plt.show()


# ## Databáze ručně zapsaných číslic

# In[9]:


# import funkce, která vrátí obrázky pro práci
from sklearn.datasets import load_digits


# In[11]:


# načtení obrázků, s nimiž budeme dále pracovat
digits_data = load_digits()


# In[12]:


# zjištění základních informací o obrázcích
print("Description:", digits_data.DESCR)

print("Data:", digits_data.data.shape)
print("Obrázky:", digits_data.images.shape)

# výpis informací o obrázcích
for i in range(0, 10):
    # počet vzorků pro trénink
    for_training = training_set_size

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

    # jak je náš model úspěšný?
    total = 0
    same = 0

    for (expected, predicted) in zip(expexted_labels, predicted_labels):
        if expected==predicted:
            same+=1
        total+=1

    print(f"{for_training:7}        {total:5}       {same:5}        {100.0*same/total:4.1f}%")


print("Pro trénink    Odhadů    Korektních    Přesnost")

for training_size in np.linspace(10, samples-100, 15):
    train_and_predict(int(training_size))
    print(f"Image #{i}:")
    print("Data:\n", digits_data.data[i])
    print("Image:\n", digits_data.images[i])
    print("Target:\n", digits_data.target[i])
    print()


# In[14]:


# další informace, které jsme získali
print("Feature names")
for feature_name in digits_data.feature_names:
    print(feature_name)

print()

print("Target names")
for target_name in digits_data.target_names:
    print(target_name)


# ## Vykreslení několika obrázků z databáze (falešné barvy)

# In[15]:


# vykreslení a uložení prvních deseti obrázků
for i in range(0, 10):
    plt.matshow(digits_data.images[i])
    plt.savefig(f"Image #{i}.png")
    plt.show()


# ## Vizualizace matice bez použití falešných barev

# In[16]:


# vytvoření matice, kterou budeme vizualizovat
array = np.random.rand(10, 10)

# vykreslení
plt.matshow(array)

# použití stupňů šedi
plt.gray()

# uložení vizualizované matice
plt.savefig("random_grayscale.png")

# vizualizace na obrazovku
plt.show()


# ## Vykreslení obrázků z databáze bez použití falešných barev

# In[20]:


# vykreslení a uložení prvních deseti obrázků
for i in range(0, 10):
    plt.matshow(digits_data.images[i], cmap=plt.cm.gray_r)
    # převod na stupně šedi
    # plt.gray()

    plt.savefig(f"Grayscale image #{i}.png")

    # vykreslení na obrazovku
    plt.show()


# ## Více číslic v jediném grafu

# In[18]:


# vytvoření seznamu, které použijeme 
images = list(zip(digits_data.target, digits_data.images))

# vykreslení tréninkových číslic
for i, (label, image) in enumerate(images[:15]):
	plt.subplot(3, 5, i+1)
	plt.imshow(image, cmap=plt.cm.gray_r) #, interpolation='nearest')
	plt.title(f"číslice {label}")

# uložení a vykreslení výsledku
plt.savefig("training_set.png")
plt.show()


# ## Příprava modelu pro trénink

# In[21]:


# nebudeme vypisovat tisíce údajů - postačí prvních dvacet
shortened = images[:20]

# výpis dat použitých pro tvorbu modelu
for i, (label, image) in enumerate(shortened):
    print(f"i={i}  label={label}\n", image, "\n")


# ## Sada trénovacích obrázků

# In[22]:


# celkový počet vzorků
samples = len(digits_data.images)
print("Vzorků celkem:", samples)

# počet vzorků pro trénink
for_training = samples // 2
print("Vzorků pro trénink:", for_training)

# obrázky (ve formě vektoru) a jejich označení
training_images = digits_data.data[:for_training]
training_labels = digits_data.target[:for_training]


# ## Klasifikace

# In[23]:


# provést klasifikaci
from sklearn import svm
classify = svm.SVC(gamma=0.001)
classify.fit(training_images, training_labels)

# očekávané výsledky vs. výsledky modelu
expexted_labels = digits_data.target[for_training:]
predicted_labels = classify.predict(digits_data.data[for_training:])


# ## Jak je model úspěšný?

# In[26]:


total = 0
same = 0

for (expected, predicted) in zip(expexted_labels, predicted_labels):
    print(expected, predicted)
    if expected==predicted:
        same+=1
    total+=1


# In[27]:


print("Total:", total)
print("Same:", same)
print("Precision:", 100.0*same/total)


# ## Ověřovací obrázky s jejich klasifikací

# In[29]:


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

# získat predikce modelu
predictions = list(zip(predicted_labels, digits_data.images[for_training:]))

show_predictions(predictions, 0, "predictions_1.png")
show_predictions(predictions, 15, "predictions_2.png")


# ## Vliv velikosti trénovací množiny na predikce modelu

# In[30]:


def train_and_predict(training_set_size):
    # počet vzorků pro trénink
    for_training = training_set_size

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

    # jak je náš model úspěšný?
    total = 0
    same = 0

    for (expected, predicted) in zip(expexted_labels, predicted_labels):
        if expected==predicted:
            same+=1
        total+=1

    print(f"{for_training:7}        {total:5}       {same:5}        {100.0*same/total:4.1f}%")


print("Pro trénink    Odhadů    Korektních    Přesnost")

for training_size in np.linspace(10, samples-100, 15):
    train_and_predict(int(training_size))


# In[42]:


def train_and_predict(training_set_size):
    # počet vzorků pro trénink
    for_training = training_set_size

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

    # jak je náš model úspěšný?
    total = 0
    same = 0

    for (expected, predicted) in zip(expexted_labels, predicted_labels):
        if expected==predicted:
            same+=1
        total+=1

    return 100.0*same/total

training_sizes = np.linspace(10, samples-100, 15, dtype=int)
vectorised = np.vectorize(train_and_predict)
precisions = vectorised(training_sizes)
plt.plot(training_sizes, precisions)
plt.savefig("precisions.png")


# In[ ]:




