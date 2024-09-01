# Strojové učení

## Obsah

* Strojové učení
* Vztah strojového učení a umělé inteligence
* Vývoj umělé inteligence
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

## Strojové učení

---

## Vztah strojového učení a umělé inteligence

---

## Vývoj umělé inteligence

---

## Základní pojmy

---

## Techniky strojového učení

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

## Použití modelů

---

## Trénink s učitelem a bez učitele

---

## Modely pro klasifikaci

---

## Modely pro regresi

---

## Lineární regrese a její varianty

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

