# Strojové učení

---

## Obsah kurzu (1/3)

* Úvod
    - Umělá inteligence
    - Vývoj umělé inteligence
    - Strojové učení
    - Vztah strojového učení a umělé inteligence
* Základní pojmy
* Techniky strojového učení
* Používané nástroje a knihovny
    - NumPy
    - Xarray
    - Pandas

---

## Obsah kurzu (2/3)

* Zpracování dat
* Použití modelů
    - Datové sady pro první seznámení s modely
    - Trénink s učitelem a bez učitele
    - Modely pro klasifikaci
    - Modely pro regresi
    - Lineární regrese a její varianty
    - Křížová validace modelů

---

## Obsah kurzu (3/3)

* Pokročilejší postupy strojového učení
    - Shluková analýza
    - Redukce dimensionality dat
    - Neuronové sítě
    - Konvoluční neuronové sítě
    - Rozpoznávání obrazu

---

# Úvod

* Umělá inteligence
* Vývoj umělé inteligence
* Strojové učení
* Vztah strojového učení a umělé inteligence

---

### Umělá inteligence

* Definice
    - konstrukce strojů, které dokážou provádět činnosti vyžadující inteligenci, pokud by byly prováděny lidmi (Marvin Minsky, 1967)
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

---

## Vývoj umělé inteligence

* 1956
    - McCarthy (LISP)
    - (pravděpodobně) poprvé použil termín AI
    - Newel a Simon: Logic theorist
* velké očekávání pokroku v dalších letech
    - dařilo se částečné řešení různých problémů
    - prakticky každý měsíc nový objev

---

## Vývoj umělé inteligence

* cca 1965
    - vystřízlivění
    - existovala sice spousta vyřešených problémů, ale ty byly triviální
    - nalezeny limity, které se nedařilo překonat
    - první "AI zima"
* sedmdesátá léta
    - systémy založené na znalostech
    - vývoj v mnoha oblastech (hledání ropy atd.)

---

## Vývoj umělé inteligence

* začátek osmdesátých let
    - velké investice do AI
    - očekávání se nenaplnila
    - potom nastává druhá "AI zima"
* druhá polovina osmdesátých let
    - rozvoj neuronových sítí (což nebyla novinka)
* 1995
    - systémy SOAR (State, Operator and Result)

---

## Vývoj umělé inteligence

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

![vztah.png](images/ai_ml_dl.png)

---

## Vztah strojového učení a umělé inteligence

* Umělá inteligence (AI)
    - strojové učení (machine learning, ML)
    - hluboké učení (deep learning, DL)
    - robotika
    - neuronové sítě (NN)
    - zpracování přirozeného jazyka (NLP)
* AI > ML > NN > DL

---

## Vztah strojového učení a umělé inteligence

* Umělá inteligence
    - objevování
    - odvozování
    - odůvodnění
* Strojové učení
    - (sofistikovaná) analýza
    - predikce (!)
    - rozhodování (klasifikace, regrese)

---

### Proč strojové učení?

* Chceme, aby se stroj naučil řešit zadaný problém na základě vzorových řešení:
    - řešení je příliš komplikované
    - problém se často mění, vyvíjí
    - lidská práce je drahá (v porovnání se strojovou)
    - máme k dispozici tolik dat, že je není možné zpracovat "ručně"

---

### Typické aplikace strojového učení

* Rozpoznávání vzorů
    - věci/osoby/výrazy tváře na fotkách
    - mluvená slova
    - spam
    - medicínská diagnóza
* Rozpoznávání anomálií
    - netypické sekvence finančních transakcí
    - netypická data přicházející ze senzorů v atomové elektrárně

---

### Typické aplikace strojového učení

* Předpovídání
    - vývoj ceny akcií na burze / vývoj měnového kurzu
    - jaké filmy bude mít daný člověk rád
    - věk osoby na fotografii
* Shlukování
    - vyhledávání zpráv s podobným obsahem
    - vyhledání skupin zákazníků s podobnými vlastnostmi

---

## Základní pojmy

* Datová sada
    - trénovací data
    - testovací data* Datová sada

![dataset.png](images/dataset.png)

---

### Techniky strojového učení

* Supervised learning
    - také se nazývá "predictive modeling"
    - známe takzvané "kategorie" neboli odpovědi
* Unsupervised learning
    - neznáme odpovědi
    - model musí najít struktury/vzory v datech
    - typicky různé varianty clusteringu

---

### Techniky strojového učení

![ml.png](images/ml.png)

---

### Supervised learning

1. trénink na základě vstupních dat
    - model se naučí vztahy mezi daty a očekávanou odpovědí
2. predikce na základě jiných(!) dat
    - problematika rozdělení dat
3. výsledky
    - klasifikace: koupí si A, B nebo C?
    - regrese: vektor příznaků, numerická hodnota nebo hodnoty

---

### Unsupervised learning

1. trénink modelu na základě vstupních dat
    - ovšem bez znalosti správných odpovědí
2. shluková analýza
3. latentní a faktorová analýza

---

### Další možnosti

1. kombinace obou metod (bez/s učitelem)
2. učení se zpětnou vazbou
    - pasivní
    - aktivní

---

### Redukce dat

![reduction.png](images/reduction.png)

---

### Redukce dat

![reduction_supervised.png](images/reduction_supervised.png)

---

### Nedoučení a přeučení

* Nedoučení
    - malá sada dat, na kterých je model trénován
    - příliš složitý model
    - data reprezentují pouze malý vzorek celého spektra hodnot
* Přeučení
    - velká vazba na trénovací data
    - menší flexibilita práce s daty, která model nezná
    - použití polynomu vyššího stupně, když by stačila lineární regrese

---

### Přeučení

![overtrain.png](images/overtraining.png)

---

### Úspěšnost modelu

* Pro zcela nová (neznámá) data!
    - ne pro trénovací množinu
    - častá chyba

---

### Křížová validace (cross validation)

* rozdělení dat do bloků
    - například na 1/10
    - 9/10 pro trénink
    - 1/10 pro otestování

---

## Zpracování dat

* Nástroje pro datovou analýzu
* Transformace dat na informace
* Jupyter Notebook
* Knihovny používané v této oblasti: NumPy, Pandas, Polars, Seaborn, scikit-learn, Dask
* Vizualizace dat: Matplotlib
* Zpracování obrazů a přirozeného jazyka v Pythonu
* Navázání na strojové učení

---

## Praktická část

---

### Python

* Dnes jeden z nejpopulárnějších programovacích jazyků
    - viz například TIOBE programming community index
    - <https://www.tiobe.com/tiobe-index/>
    - popř. statistika dostupná na OpenHubu
    - <https://www.openhub.net/languages/compare>
* Dostupnost na většině platforem
    - na některých MCU jako MicroPython

---

### Typické použití Pythonu

* Nástroje a utility ovládané z příkazového řádku
* Aplikace s grafickým uživatelským rozhraním
* Client-server
    - serverová část (Flask, Django, CherryPy, ...)
    - klient (Brython, spíše technologické demo)
* Numerické výpočty, symbolické výpočty
    - NumPy
    - SciPy
    - Matplotlib

---

### Typické použití Pythonu

* Moderní způsoby využití Pythonu
    - AI
    - Machine Learning (Deep Learning)
    - PyTorch
    - Big data
    - aplikace v prohlížeči
* Tzv. „glue“ jazyk
* Vestavitelný interpret Pythonu

---

### Nástroje pro datovou analýzu

* Data mining
* Data procesing a modelování
    - klasifikace
    - predikce
    - výběr modelu
    - redukce počtu dimenzí
    - pre-processing
    - modelování
* Vizualizace

---

### Jupyter Notebook

* Typický centrální prvek, v němž se odehrává vývoj
* Lze sdílet
* Podporuje různá jádra (kernels)
* Podpora vizualizace přímo na ploše notebooku

---

### Data mining

* Scrapy
* BeautifulSoup

---

### Data processing a modelování

* NumPy
* SciPy
* Xarray
* Pandas
* Polars
* SciKit-learn

---

### Vizualizace dat

* Matplotlib
* Seaborn
* Bokeh
* Plotly
* pydot
* plotnine

---

### Strojové učení

* PyCaret
* H2O
* TPOT
* Auto-sklearn
* Keras
* SciKit-Learn
* PyTorch
* TensorFlow

---

### Zpracování přirozeného jazyka

* NLTK
* spaCy

---

### HPC

* Dask

---

### NumPy

![numpy_arrays.png](images/numpy_logo.png)

---

#### Knihovna NumPy

- Výslovnosti
    - [nəmpᴧɪ]
    - [nəmpi]
- Historie
    - matrix package
    - Numeric
    - NumPy
- Podpora pro n-dimenzionální pole
    - + nové funkce
    - + nové (přetížené) operátory

---

#### Knihovna NumPy

- Kooperace s dalšími knihovnami a frameworky
    - SciPy
    - Matplotlib
    - OpenCV
    - Xarray
- Interně použito i ve scikit-learn

---

#### NumPy

* n-dimenzionální pole jako základní datový typ
    - ideově vychází z APL
    - nové funkce
    - nové (přetížené) operátory
* mnoho typů konstruktorů
* broadcasting
* (re)shaping
    - změna tvaru pole (počet dimenzí, tvar)

---
#### Skalární datové typy
- <https://docs.scipy.org/doc/numpy/user/basics.types.html>
```
╔════════════╤═══════════════════════════╤═══════════════════════════════╗
║ Formát     │ Popis                     │ Rozsah                        ║
╟────────────┼───────────────────────────┼───────────────────────────────╢
║ bool       │ uloženo po bajtech        │  True/False                   ║
╟────────────┼───────────────────────────┼───────────────────────────────╢
║ int8       │ celočíselný se znaménkem  │ -128..127                     ║
║ int16      │ celočíselný se znaménkem  │ -32768..32767                 ║
║ int32      │ celočíselný se znaménkem  │ -2147483648..2147483647       ║
║ int64      │ celočíselný se znaménkem  │ -9223372036854775808..        ║
║            │                           │  9223372036854775807          ║
╟────────────┼───────────────────────────┼───────────────────────────────╢
║ uint8      │ celočíselný bez znaménka  │  0..255                       ║
║ uint16     │ celočíselný bez znaménka  │  0..65535                     ║
║ uint32     │ celočíselný bez znaménka  │  0..4294967295                ║
║ uint64     │ celočíselný bez znaménka  │  0..18446744073709551615      ║
╟────────────┼───────────────────────────┼───────────────────────────────╢
║ float16    │ plovoucí řádová čárka     │  poloviční přesnost (half)    ║
║ float32    │ plovoucí řádová čárka     │  jednoduchá přesnost (single) ║
║ float64    │ plovoucí řádová čárka     │  dvojitá přesnost (double)    ║
╟────────────┼───────────────────────────┼───────────────────────────────╢
║ complex64  │ komplexní číslo (dvojice) │  2×float32                    ║
║ complex128 │ komplexní číslo (dvojice) │  2×float64                    ║
╚════════════╧═══════════════════════════╧═══════════════════════════════╝
```

---

#### Kódy skalárních datových typů
- jednoznakové kódy je možné použít namísto jména typu
```
╔════════════╤══════╗
║  Formát    │ Kód  ║
╟────────────┼──────╢
║ formát     │ kód  ║
║ bool       │ '?'  ║
║ int8       │ 'b'  ║
║ int16      │ 'h'  ║
║ int32      │ 'i'  ║
║ int64      │ 'l'  ║
║ uint8      │ 'B'  ║
║ uint16     │ 'H'  ║
║ uint32     │ 'I'  ║
║ uint64     │ 'L'  ║
║ float16    │ 'e'  ║
║ float32    │ 'f'  ║
║ float64    │ 'd'  ║
║ complex64  │ 'F'  ║
║ complex128 │ 'D'  ║
╚════════════╧══════╝
```

---

#### Datový typ single
```
Celkový počet bitů (bytů):   32 (4)
Bitů pro znaménko:            1
Bitů pro exponent:            8
Bitů pro mantisu:            23
```

---

#### Datový typ double
```
Celkový počet bitů (bytů):   64 (8)
Bitů pro znaménko:            1
Bitů pro exponent:           11
Bitů pro mantisu:            52
```

---

#### Datový typ float16
```
Celkový počet bitů (bytů):   16 (2)
Bitů pro znaménko:            1
Bitů pro exponent:            5
Bitů pro mantisu:            10
BIAS (offset exponentu):     15
Přesnost:                    5-6 číslic
Maximální hodnota:           65504
Minimální hodnota:          -65504
Nejmenší kladná nenulová hodnota:      5,960×10⁻⁸
Nejmenší kladná normalizovaná hodnota: 6,104×10⁻⁵
```

---

#### N-dimenzionální pole

![numpy_arrays.png](images/numpy_arrays.png)

---

#### Datová struktura ndarray
- Představuje obecné n-dimenzionální pole
- Interní způsob uložení dat zcela odlišný od Pythonovských seznamů či n-tic
    - „pohled“ na kontinuální blok hodnot
- Homogenní datová struktura
    - menší flexibilita
    - menší paměťové nároky
    - vyšší výpočetní rychlost díky použití nativního kódu
    - obecně lepší využití cache a rychlejší přístup k prvkům
- Základní strukturovaný datový typ knihovny NumPy
- Volitelný počet dimenzí
    - vektory
    - matice
    - pole s větším počtem dimenzí
- Volitelný typ prvků
- Volitelné uspořádání prvků
    - podle zvyklostí jazyka Fortran
    - podle zvyklostí jazyka C

#### Tvar (shape) n-dimenzionálního pole
- Popisuje organizaci a uspořádání prvků v poli
    - n-tice obsahující rozměry pole v jednotlivých dimenzích
- Příklady tvarů
    - `(10,)` - vektor s deseti prvky
    - `(2, 3)` - dvourozměrná matice se dvěma řádky a třemi sloupci
    - `(2, 3, 4)` - trojrozměrné pole
- Tvar je možné zjistit
    - atribut „shape“
    - funkce `numpy.shape()`
- Tvar je možné změnit
    - funkce `numpy.reshape()`

#### Konstrukce n-dimenzionálních polí
- Několik typů konstruktorů
    - `numpy.array()`
    - `numpy.zeros()`
    - `numpy.ones()`
    - `numpy.full()`
    - `numpy.eye()`
    - `numpy.arange()`
    - `numpy.linspace()`
    - `numpy.geomspace()`
    - `numpy.logspace()`
- Konverzní funkce
    - `numpy.matrix()`

#### Konstruktor numpy.array
- parametry
`array(object, dtype=None, copy=True, order=None, subok=False, ndmin=0)`

#### Order
```
╔═════════╤════════════════════════════════════╗
║ Hodnota │ Význam                             ║
╟─────────┼────────────────────────────────────╢
║ 'C'     │ prvky jsou interně uspořádány jako ║
║         │ v programovacím jazyku C           ║
║         │                                    ║
║ 'F'     │ prvky jsou interně uspořádány jako ║
║         │ v programovacím jazyku Fortran     ║
║         │                                    ║
║ 'A'     │ ponecháme na implementaci, který   ║
║         │ způsob uspořádání interně zvolit   ║
╚═════════╧════════════════════════════════════╝
```

#### Order - rozdíl v uspořádání
- 2D matice tak, jak ji vidí uživatel (logická struktura)
```
| 1 2 3 |
| 4 5 6 |
| 7 8 9 |
```

- Uložení v operační paměti
```
1 2 3 4 5 6 7 8 9 - 'C'
1 4 7 2 5 8 3 6 9 - 'F'
```

---

### Xarray

![xarray](images/xarray1.png)

---

#### Xarray

* n-dimensionální pole s metadaty
    - jméno
    - dimenze (osy)
    - koordináty na osách
    - uživatelské atributy

---

#### Přednosti použití Xarray

* intuitivní práce s poli
* založeno na metadatech, ne na kódu
* stručnost
* dnes de facto standardní řešení
* méně chyb při zpracování dat
    - operace nad nekorektními osami
* broadcasting založený na jménu osy
* velmi jednoduchá operace typu `groupby`

---

#### Množina polí

![xarray](images/xarray2.png)

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

* Jeden z nejjednodušších a nejužitečnějších modelů
    - interně velmi jednoduchý
    - lze odvodit, co se model naučil
    - typicky nedochází k přeučení
* Typicky metoda nejmenších čtverců
* Lze použít v libovolném počtu rozměrů
* Lineární regrese v oblasti parametrů, nikoli vstupních hodnot
    - polynomická regrese

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

```python
import numpy as np

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
X = np.delete(data, 0, axis=1) # smazat jeden sloupec
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

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro//housings_prediction_3.py)

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

