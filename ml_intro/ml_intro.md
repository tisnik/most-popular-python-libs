# Strojové učení

## Obsah

* Úvod
    - Umělá inteligence
    - Vývoj umělé inteligence
    - Strojové učení
    - Vztah strojového učení a umělé inteligence
* Základní pojmy
* Techniky strojového učení
* Zpracování dat
* Použití modelů
* Datové sady pro první seznámení s modely
* Trénink s učitelem a bez učitele
* Modely pro klasifikaci
* Modely pro regresi
* Lineární regrese a její varianty
* Křížová validace modelů
* Shluková analýza
* Redukce dimensionality dat
* Neuronové sítě
* Konvoluční neuronové sítě
* Rozpoznávání obrazu

---

# Úvod

* Umělá inteligence
* Vývoj umělé inteligence
* Strojové učení
* Vztah strojového učení a umělé inteligence

---

### Umělá inteligence

* Definice
    - konstrukce strojů, které dokážou provádět činnosti vyžadující inteligenci, pokud by byly prováděny lidmi
    - (Marvin Minsky, 1967)
    - existují i alternativní definice
* Modelování lidské mysli
    - shora dolů (psychologie)
    - zdola nahoru (neurověda)
    - zprostředka (informatika)
* Inteligentní chování může vzniknout ze spojení velkého množství jednoduchých systémů
    - koncept neuronových sítí

---

## Vývoj umělé inteligence

* 1943-1955
    - první myšlenky, že něco podobného může reálně vzniknout
    - booleovský model neuronu
    - A. Turing: Computing Machinery and Intelligence
* 1956
    - McCarthy (LISP)
    - (pravděpodobně) poprvé použil termín AI
    - Newel a Simon: Logic theorist
* velké očekávání pokroku v dalších letech
    - dařilo se částečné řešení různých problémů
    - prakticky každý měsíc nový objev
* cca 1965
    - vystřízlivění
    - existovala sice spousta vyřešených problémů, ale ty byly triviální
    - nalezeny limity, které se nedařilo překonat
    - první "AI zima"
* sedmdesátá léta
    - systémy založené na znalostech
    - vývoj v mnoha oblastech (hledání ropy atd.)
* začátek osmdesátých let
    - velké investice do AI
    - očekávání se nenaplnila
    - potom nastává druhá "AI zima"
* druhá polovina osmdesátých let
    - rozvoj neuronových sítí (což nebyla novinka)
* 1995
    - systémy SOAR (State, Operator and Result)
* 2000
    - big data (v tom pokračujeme i dnes)
    - ale prozatím žádné větší objemy
    - "wow" efekt na úrovni AI
* 2010
    - deep learning
* 2020
    - LLM (prompt engineering, ne fine tuning)
* současnost
    - LLM
    - generativní AI

---

## Strojové učení

* podoblast umělé inteligence
* změna interního stavu systému při tréninku
* několik způsobů realizace strojového učení
* "statistické učení"
* typicky se nejedná o plně automatizovanou činnost
    - vyžaduje chytrá (strategická) rozhodnutí
    - výběr modelu
    - výběr hyperparametrů modelu
    - rozdělení vstupních dat
    - filtrace dat
* nalézají se skryté vzorky a vazby v datech

---

## Vztah strojového učení a umělé inteligence

* Umělá inteligence (AI)
    - strojové učení (machine learning, ML)
    - hluboké učení (deep learning, DL)
    - robotika
    - neuronové sítě (NN)
    - zpracování přirozeného jazyka (NLP)
* AI > ML > NN > DL
* Umělá inteligence
    - objevování
    - odvozování
    - odůvodnění
* Strojové učení
    - (sofistikovaná) analýza
    - predikce (!)
    - rozhodování (klasifikace, regrese)
---

## Základní pojmy

---

## Techniky strojového učení

* Supervised learning
    - také se nazývá "predictive modeling"
    - známe takzvané "kategorie" neboli odpovědi
* Unsupervised learning
    - neznáme odpovědi
    - model musí najít struktury/vzory v datech
    - typicky různé varianty clusteringu

---

### Supervised learning

1. trénink na základě vstupních dat
    - model se naučí vztahy mezi daty a očekávanou odpovědí
2. predikce na základě jiných(!) dat
    - problematika rozdělení dat

---

### Unsupervised learning

1. trénink modelu na základě vstupních dat
    - ovšem bez znalosti správných odpovědí

---

## Zpracování dat

---

## Datové sady pro první seznámení s modely

---

### Datová sada Iris

```python
# modul s datovou sadou Iris
from sklearn.datasets import load_iris

# nacteni datove sady
iris = load_iris()

# jakeho typu je vlastne datova sada?
print(type(iris))

print("-" * 100)

# dostupne atributy a metody
print(dir(iris))
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro//iris_dataset.py)

Výstup

```
<class 'sklearn.utils._bunch.Bunch'>
----------------------------------------------------------------------------------------------------
['DESCR', 'data', 'data_module', 'feature_names', 'filename', 'frame', 'target', 'target_names']
```

```python
# modul s datovou sadou Iris
from sklearn.datasets import load_iris

# nacteni datove sady
iris = load_iris()

print(dir(iris))

print("-" * 100)

# podrobny popis datove sady
print(iris["DESCR"])
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro//iris_description.py)

```python
# modul s datovou sadou Iris
from sklearn.datasets import load_iris

# nacteni datove sady
iris = load_iris()

# precteni dat z datove sady
# urcenych pro trenink, validaci atd.
data = iris["data"]

print("Feature data:")
print(data)
print("-" * 100)

# typ a "tvar" n-dimenzionalniho pole
print("Data type:")
print(type(data))
print()

print("Data shape:")
print(data.shape)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro//iris_data.py)

---

### Datová sada California Housings

---

## Použití modelů

---

## Trénink s učitelem a bez učitele

---

## Modely pro klasifikaci

---

## Modely pro regresi

---

## Lineární regrese a její varianty

```python
import numpy as np
import matplotlib.pyplot as plt

from sklearn import linear_model

# počet vzorků ve vektorech x i y
VALUES = 50

# x je vektor
x = np.linspace(0, 10, VALUES)

# y je vektor
y = np.linspace(-1, 1, VALUES) + 0.5*np.random.rand(VALUES)

# převod vektoru na 2D matici
X = x.reshape(-1, 1)

# tvar matice X a vektoru y
print("X shape:", X.shape)
print("y shape:", y.shape)

# konstrukce modelu
lr = linear_model.LinearRegression()

# trénink modelu (X musí být maticí)
lr.fit(X, y)

# predikce modelu
y_pred = lr.predict(X)

# výpis vypočtených koeficientů modelu
print("Coefficients: \n", lr.coef_)
print("Intercept: \n", lr.intercept_)

# vykreslení výsledku
plt.scatter(x, y, color="black", s=2)
plt.plot(x, y_pred, color="blue", linewidth=2)

# titulek grafu
plt.title("Linear regression")

# osy
plt.xticks()
plt.yticks()

# ulozeni diagramu do souboru
plt.savefig("112.png")

# zobrazeni diagramu
plt.show()
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro//linear_regression_gen_data.py)

---

### Použití modelu lineární regrese

* California housings

### Trénink modelu se všemi daty

* Což obecně není vhodné

```python
from sklearn import linear_model
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import mean_squared_error, r2_score

# nacteni datove sady
housings = fetch_california_housing()

# precteni dat z datove sady
# urcenych pro trenink, validaci atd.
data = housings["data"]

# ceny bloku
targets = housings["target"]

# trening bude proveden se VSEMI zaznamy
# testovani taktez (prozatim)
X = data
y = targets

# konstrukce modelu
lr = linear_model.LinearRegression()

# trénink modelu
lr.fit(X, y)

# predikce modelu
y_pred = lr.predict(X)

# výpis vypočtených koeficientů modelu
print("Coefficients: \n", lr.coef_)
print("Intercept: \n", lr.intercept_)

# chyba predikce
print("Mean squared error: %.2f" % mean_squared_error(y, y_pred))

# 1 = nejlepší predikce modelu
print("Coefficient of determination: %.2f" % r2_score(y, y_pred))
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro//housings_prediction_1.py)

```python
from sklearn import linear_model
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# nacteni datove sady
housings = fetch_california_housing()

# precteni dat z datove sady
# urcenych pro trenink, validaci atd.
data = housings["data"]

# ceny bloku
targets = housings["target"]

# X je matice, y je vektor
X = data
y = targets

# rozdeleni dat na treninkovou a testovaci mnozinu
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.6)

# konstrukce modelu
lr = linear_model.LinearRegression()

# trénink modelu
lr.fit(X_train, y_train)

# predikce modelu
y_pred = lr.predict(X_test)

# výpis vypočtených koeficientů modelu
print("Coefficients: \n", lr.coef_)
print("Intercept: \n", lr.intercept_)

# chyba predikce
print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))

# 1 = nejlepší predikce modelu
print("Coefficient of determination: %.2f" % r2_score(y_test, y_pred))
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro//housings_prediction_2.py)

---

## Křížová validace modelů

---

## Shluková analýza

---

## Redukce dimensionality dat

---

## Neuronové sítě

---

## Konvoluční neuronové sítě

---

## Rozpoznávání obrazu

---

