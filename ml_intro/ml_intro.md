# Strojové učení

Pavel Tišnovský
tisnik@centrum.cz

---

## Obsah kurzu (1/4)

* Úvod
    - Umělá inteligence
    - Vývoj umělé inteligence
    - Strojové učení
    - Vztah strojového učení a umělé inteligence
* Základní pojmy
* Techniky strojového učení

---

## Obsah kurzu (2/4)
* Používané nástroje a knihovny
    - NumPy
    - Xarray
    - Pandas
    - Polars
    - Matplotlib
    - Plotnine
    - scikit-learn
    - NLTK

---

## Obsah kurzu (3/4)

* Zpracování dat
* Použití modelů
    - Datové sady pro první seznámení s modely
    - Trénink s učitelem a bez učitele
    - Modely pro klasifikaci
    - Modely pro regresi
    - Lineární regrese a její varianty
    - Křížová validace modelů

---

## Obsah kurzu (4/4)

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
    - A. Turing
        - Computing Machinery and Intelligence

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
    - testovací data

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

### ML modely

* ANN
* Desicion trees
* Support-vector machine
* Regresní analýza
* Bayesovské sítě
* Genetické algoritmy
* NN

---

### Jak začít?

1. jaké atributy použít z dat?
2. jaký model vybrat
3. jak optimalizovat pro větší výkon
4. jak vytvořit model, který bude vhodný pro pro něj neznámá data?
5. jak odhadnout vhodnost modelu pro neznámá data?


---

### Komprimace dat
* souvislost mezi ML a komprimací dat
* predikce
* tzv. optimální komprese
    - při predikci lze použít aritmetické kódování

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
* Knihovny používané v této oblasti
    - NumPy, Pandas, Polars, Seaborn, scikit-learn, Dask
* Vizualizace dat
    - Matplotlib
* Zpracování obrazů a přirozeného jazyka v Pythonu
* Navázání na strojové učení

---

## Neuronové sítě

* Propojení takzvaných neuronů
    - Model neuronu
    - Způsob propojení neuronů
    - Vstupy a výstupy

---

### Model neuronu

![neuron.png](images/neuron.png)

* libovolný počet vstupů
* typicky jeden výstup
* váhy vstupů
* aktivační funkce

y = f(w_1x_1 + w_2x_2 + … + w_nx_n)

---

### Bias

![bias.png](images/bias.png)

y = f(w_0 + w_1x_1 + w_2x_2 + … + w_nx_n)

---

### Aktivační funkce

* Jediná nelinearita v modelu
* Mnoho typů aktivačních funkcí

---

### Aktivační funkce

![akt1.png](images/akt_1.png)

---

### Aktivační funkce

![akt2.png](images/akt_2.png)

---

### Feed-forward síť

* Vstupní vrstva
* Skryté vrstvy
* Výstupní vrstva

---

### Feed-forward síť

![ff.png](images/ff.png)

---

### Příliš mnoho vrstev

* Model se přestane učit nebo se učí velmi pomalu
    - vanishing gradient problem
    - "méně je někdy více"

---

### Konvoluční neuronové sítě

* Typicky pro rastrové obrázky
    - mírné posunutí, zkosení atd.
    - lze sice řešit klasickými NN
    - ovšem je to zbytečně složité (RAM, CPU čas)
    - příliš mnoho stejných, ale samostatně uložených vah
    - konvoluční a subsamplingové vrstvy

---

### Konvoluční neuronové sítě

* Typická konfigurace
    - vstupní vrstva
    - konvoluční vrstva #1
    - subsamplingová vrstva #1
    - konvoluční vrstva #2
    - subsamplingová vrstva #2
    - ...
    - ...
    - klasická skrytá vrstva
    - výstupní vrstva

---

### Konvoluční vrstva

* Získání lokálních informací z rastru
* Malé oblasti, například 3x3, 5x5 pixelů
* Každá oblast vstup do jednoho neuronu
    - 9 resp. 25 vstupů
* Jednotlivé oblasti se překrývají
    - pro rastr x*y máme (x-k+1)*(y-k+1) oblastí
    - počet neuronů odpovídá počtu pixelů

---

### Konvoluční vrstva
* Obecně získáváme n rovin
    - zdánlivě obrovská spotřeba RAM
    - (pro rastr x*y máme (x-k+1)*(y-k+1) oblastí)
* Ovšem váhy mezi neurony se sdílí!
    - 26 vah pro oblast 5x5 (včetně biasu)

---

### Subsamplingová vrstva

* Za konvolučními vrstvami
* Nepřekrývající se oblasti
    - dochází ke zmenšování počtu výstupů
    - pro 2x2 oblasti na čtvrtinu

---

### Příklad konvoluční sítě

```
Vrstva          Vstup          Výstup
konvoluční      32 × 32        64 × (32–5+1) × (32–5+1) = 64 × 28 × 28
subsampling     64 × 28 × 28   64 × 28/2 × 28/2 = 64 × 14 × 14
konvoluční      64 × 14 × 14   64 × (14–5+1) × (14–5+1) = 64 × 10 × 10
subsampling     64 × 10 × 10   64 × 10/2 × 10/2 = 64 × 5 × 5 = 1600
```

* následovat může běžná skrytá vrstva s dejme tomu 10 výstupy

---

## Od teorie k praxi

![python.png](images/python.png)

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
    - mezi jinými i interpret Pythonu
* Podpora vizualizace přímo na ploše notebooku
* Varianta nazvaná JupyterLite

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

### Knihovna NumPy

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

### Knihovna NumPy

- Kooperace s dalšími knihovnami a frameworky
    - SciPy
    - Matplotlib
    - OpenCV
    - Xarray
- Interně použito i ve scikit-learn

---

### NumPy

* n-dimenzionální pole jako základní datový typ
    - ideově vychází z APL
    - nové funkce
    - nové (přetížené) operátory
* mnoho typů konstruktorů
* broadcasting
* (re)shaping
    - změna tvaru pole (počet dimenzí, tvar)

---
### Skalární datové typy
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

### Kódy skalárních datových typů
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

### Datový typ single
```
Celkový počet bitů (bytů):   32 (4)
Bitů pro znaménko:            1
Bitů pro exponent:            8
Bitů pro mantisu:            23
```

---

### Datový typ double
```
Celkový počet bitů (bytů):   64 (8)
Bitů pro znaménko:            1
Bitů pro exponent:           11
Bitů pro mantisu:            52
```

---

### Datový typ float16
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

### N-dimenzionální pole

![numpy_arrays.png](images/numpy_arrays.png)

---

### Datová struktura ndarray

- Představuje obecné n-dimenzionální pole
- Interní způsob uložení dat zcela odlišný od Pythonovských seznamů či n-tic
    - „pohled“ na kontinuální blok hodnot
- Homogenní datová struktura
    - menší flexibilita
    - menší paměťové nároky
    - vyšší výpočetní rychlost díky použití nativního kódu
    - obecně lepší využití cache a rychlejší přístup k prvkům
- Základní strukturovaný datový typ knihovny NumPy

---

### Datová struktura ndarray

- Volitelný počet dimenzí
- Tedy například:
    - vektory
    - matice
    - pole s větším počtem dimenzí
- Volitelný typ prvků
- Volitelné uspořádání prvků
    - podle zvyklostí jazyka Fortran
    - podle zvyklostí jazyka C

---

### Tvar (shape) n-dimenzionálního pole

- Popisuje organizaci a uspořádání prvků v poli
    - n-tice obsahující rozměry pole v jednotlivých dimenzích
- Příklady tvarů
    - `(10,)` - vektor s deseti prvky
    - `(2, 3)` - dvourozměrná matice se dvěma řádky a třemi sloupci
    - `(2, 3, 4)` - trojrozměrné pole

---

### Tvar (shape) n-dimenzionálního pole
- Tvar je možné zjistit
    - atribut „shape“
    - funkce `numpy.shape()`
- Tvar je možné změnit
    - funkce `numpy.reshape()`

---

### Konstrukce n-dimenzionálních polí

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

---

### Konstruktor numpy.array

- parametry
`array(object, dtype=None, copy=True, order=None, subok=False, ndmin=0)`

---

### Order

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

---

### Order - rozdíl v uspořádání

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

### Xarray

* n-dimensionální pole s metadaty
    - jméno
    - dimenze (osy)
    - koordináty na osách
    - uživatelské atributy

---

### Přednosti použití Xarray

* intuitivní práce s poli
* založeno na metadatech, ne na kódu
* stručnost
* dnes de facto standardní řešení
* méně chyb při zpracování dat
    - operace nad nekorektními osami
* broadcasting založený na jménu osy
* velmi jednoduchá operace typu `groupby`

---

### Množina polí

![xarray](images/xarray2.png)

---

### Pandas

![pandas](images/pandas.png)

---

### Pandas

* Načtení dat z různých datových zdrojů do datových rámců
    - CSV
    - TSV
    - databáze
    - tabulkové procesory
* Programová konstrukce datových rámců
* Prohlížení obsahu datových rámců

---

### Pandas

* Iterace nad daty, řazení a další podobné operace
* Spojování, seskupování a změna tvaru dat
* Práce s takzvanými sériemi
    - většinou získanými z datových rámců
* Vykreslování grafů z údajů získaných z datových rámců

---

### Práce s datovými rámci

* Knihovna Pandas podporuje využití různých datových zdrojů, především pak:
  - Souborů CSV (Comma-Separated Values)
  - Souborů TSV (Tab-Separated Values)
  - Textových souborů s volitelným oddělovačem a formátem sloupců
  - Tabulek z tabulkových procesorů (xls, xlsx, xlsm, xlsb, odf, ods, odt)
  - Souborů JSON se strukturovanými daty
  - Načítání z relačních databází s využitím SQL
  - Načítání z Parquet souborů

---

### Zpracování souborů s nestandardním formátem

* https://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt
* Evidentně se jedná o tabulková a velmi dobře strukturovaná data, která by bylo vhodné umět automaticky zpracovat

---

### Zpracování souborů s nestandardním formátem

```
13.11.2023 #219
země|měna|množství|kód|kurz
Austrálie|dolar|1|AUD|14,683
Brazílie|real|1|BRL|4,672
Bulharsko|lev|1|BGN|12,573
Čína|žen-min-pi|1|CNY|3,162
Dánsko|koruna|1|DKK|3,296
EMU|euro|1|EUR|24,590
Filipíny|peso|100|PHP|41,117
Hongkong|dolar|1|HKD|2,952
Indie|rupie|100|INR|27,682
Indonesie|rupie|1000|IDR|1,468
Island|koruna|100|ISK|16,040
Izrael|nový šekel|1|ILS|5,964
Japonsko|jen|100|JPY|15,186
Jižní Afrika|rand|1|ZAR|1,228
Kanada|dolar|1|CAD|16,664
Korejská republika|won|100|KRW|1,740
Maďarsko|forint|100|HUF|6,514
Malajsie|ringgit|1|MYR|4,896
Mexiko|peso|1|MXN|1,303
MMF|ZPČ|1|XDR|30,319
Norsko|koruna|1|NOK|2,069
Nový Zéland|dolar|1|NZD|13,550
Polsko|zlotý|1|PLN|5,552
Rumunsko|leu|1|RON|4,947
Singapur|dolar|1|SGD|16,936
Švédsko|koruna|1|SEK|2,118
Švýcarsko|frank|1|CHF|25,471
Thajsko|baht|100|THB|64,040
Turecko|lira|1|TRY|0,806
USA|dolar|1|USD|23,050
Velká Británie|libra|1|GBP|28,230
```

---

### Polars

![polars](images/polars.png)

---

### Polars

* Alternativa ke knihovně Pandas
* Podporuje multithreading
* SIMD operace (ne vždy)
* Optimalizace dotazů
* Líné vyhodnocování

---

### Polars

* Datové rámce rozsáhlejší než dostupná RAM
* Naprogramováno v Rustu
* Vazby s dalšími knihovnami
    - pyarrow, NumPy, Pandas etc.
* Rozhraní pro Python a NodeJS

---

### Datové řady a datové rámce

* Podobné těm v Pandas
    - funkce a metody se stejnými jmény
    - ovšem ne zcela kompatibilní

---

### Načtení z SQL

```python
import polars

connection_string = "postgresql://postgres:postgres@localhost:5432/testdb"

query = """
    SELECT org_id, cluster_id, rule_fqdn
      FROM rule_hit
     ORDER by org_id, cluster_id
"""

df = polars.read_sql(query, connection_string)

print(df)
print()
```

---

### Klíč k úspěchu: být líný!

* FP programování
* Architektura založená na Kafce atd.
* Dask atd.
* Líné datové rámce v Polars

---

### Líné datové rámce

```python
import polars

df = polars.read_csv("hall_of_fame.csv").lazy()

df2 = df.groupby("Winner", maintain_order=True).agg([polars.col("Year").len()]). \
      sort("Year"). \
      reverse(). \
      head(5)

print(df2.describe_plan())
print(df2.describe_optimized_plan())
```

---

### Matplotlib

![Matplotlib](images/matplotlib.png)

---

### Matplotlib

* zaměřena explicitně na tvorbu grafů
* právě vzájemnou kombinací obou knihoven NumPy+matplotlib lze relativně
* snadno dosáhnout velmi pěkných výsledků plně porovnatelných s výsledky
  vytvořenými komerčními balíky.

---

### Možnosti knihovny Matplotlib

* grafy funkcí typu y = f(x)
* parametrické zadání 2D průběhu x, y = f(t)
* grafy funkcí typu z = f(x,y)
* parametrické zadání 3D průběhu x, y, z = f(t)

---

### Zobrazení grafů

* na obrazovce
* do plochy Jupyter Notebooku
* do rastrových obrázků
* do vektorových kreseb
* do PDF

---

### Plotnine

* Řešení podobné jazyku R
* "A Grammar of Graphics for Python"

```python
from plotnine import ggplot, geom_point, aes, stat_smooth, facet_wrap
from plotnine.data import mtcars

(
    ggplot(mtcars, aes("wt", "mpg", color="factor(gear)"))
    + geom_point()
    + stat_smooth(method="lm")
    + facet_wrap("gear")
)
```

---

### Plotnine

![plotnine1.png](images/plotnine1.png)

---

### Plotnine

![plotnine2.png](images/plotnine2.png)

---

### Plotnine

![plotnine3.png](images/plotnine3.png)

---

### Plotnine

![plotnine4.png](images/plotnine4.png)

---

### Zpracování obrazů a přirozeného jazyka v Pythonu

* Zpracování obrazů
    - OpenCV-Python
* Zpracování přirozeného jazyka
    - NLTK
    - TikToken
    - Langchain

---

### Strojové učení

* scikit-learn
    - stejné rozhraní pro různé ML modely
    - dobře zvolené výchozí parametry modelu
    - možnost doladění parametrů modelu
    - poměrně dobra dokumentace
        - (i když chybí různé howto...)

---

### Užitečné odkazy

* 15 Python Libraries for Data Science You Should Know
    - https://www.dataquest.io/blog/15-python-libraries-for-data-science/
* Top Python Libraries for Data Science in 2022
    - https://www.datacamp.com/blog/top-python-libraries-for-data-science

---

# Praktická část

---

## Jupyter Notebook

![jupyter.png](images/jupyter.jpg)

* Lokální instalace
* Centrální instalace se vzdáleným přístupem

---

## JupyterLite

![jupyterlite.jpg](images/jupyterlite.png)

* Jupyter Notebook v prohlížeči
* Založeno na technologii WASM
* https://jupyter.org/try-jupyter/lab/

---

## NumPy

![numpy_arrays.png](images/numpy_logo.png)

---

```python
# Konstrukce jednorozměrného pole konstruktorem numpy.array()
#
# vytvoření pole se čtyřmi prvky

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.array([1, 2, 3, 4])

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_01_array.py)

---

```python
# Konstrukce jednorozměrného pole konstruktorem numpy.array()
#
# vytvoření pole s deseti prvky

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.array(range(10))

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_02_array_range.py)

---

```python
# Konstrukce jednorozměrného pole konstruktorem numpy.array()
#
# explicitní specifikace typu všech prvků pole
# (interně se provádí přetypování)

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.array(range(10), dtype=numpy.float)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_03_array_dtype.py)

---

```python
# Konstrukce jednorozměrného pole konstruktorem numpy.array()
#
# explicitní specifikace uspořádání prvků pole
# (nemá velký význam pro 1D pole=vektory)

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.array(range(10), order="C")

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_04_array_order_c.py)

---

```python
# Konstrukce jednorozměrného pole konstruktorem numpy.array()
#
# explicitní specifikace uspořádání prvků pole
# (nemá velký význam pro 1D pole=vektory)

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.array(range(10), order="F")

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_05_array_order_f.py)

---

```python
# Příklady použití funkce numpy.array
#
# vytvoření dvourozměrné matice

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.array([[1, 2, 3], [4, 5, 6]])

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_06_2D_array.py)

---

```python
# Příklady použití konstruktoru numpy.zeros
#
# jednorozměrný vektor s jediným prvkem

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.zeros(1)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_07_zeros_1D_array.py)

---

```python
# Příklady použití konstruktoru numpy.zeros
#
# jednorozměrný vektor s deseti prvky

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.zeros(10)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_08_zeros_1D_array.py)

---

```python
# Příklady použití konstruktoru numpy.zeros
#
# matice o velikosti 5x5 prvků, každý prvek je typu float

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.zeros((5, 5))

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_09_zeros_2D_array.py)

---

```python
# Příklady použití konstruktoru numpy.zeros
#
# matice o velikosti 3x3x3 prvků, každý prvek je typu float

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.zeros((3, 3, 3))

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_10_zeros_3D_array.py)

---

```python
# Příklady použití konstruktoru numpy.zeros
#
# matice o velikosti 5x5 prvků, každý prvek je typu int

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.zeros((5, 5), dtype=int)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_11_zeros_specify_type.py)

---

```python
# Příklady použití konstruktoru numpy.zeros
#
# použití komplexních čísel

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.zeros((3, 2), dtype=numpy.complex)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_12_zeros_complex_numbers.py)

---

```python
# Příklady použití konstruktoru numpy.ones
#
# jednorozměrný vektor s deseti prvky

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.ones(10)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_13_ones_1D_array.py)

---

```python
# Příklady použití konstruktoru numpy.ones
#
# matice se třemi řádky a čtyřmi sloupci

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.ones((3, 4))

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_14_ones_2D_array.py)

---

```python
# Příklady použití konstruktoru numpy.ones
#
# matice se třemi řádky a čtyřmi sloupci
# s explicitní specifikací typu prvků

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.ones((3, 4), dtype=int)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_15_ones_specify_type.py)

---

```python
# Příklady použití konstruktoru numpy.ones
#
# trojrozměrné pole s prvky typu int

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.ones((3, 4, 5), dtype=int)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_16_ones_3D_array.py)

---

```python
# Příklady použití konstruktoru numpy.ones
#
# použití komplexních čísel

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.ones((3, 2), dtype=numpy.complex)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_17_ones_complex_numbers.py)

---

```python
# Příklady použití konstruktoru numpy.eye
#
# matice s jediným prvkem

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.eye(1)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_18_eye_1D_array.py)

---

```python
# Příklady použití konstruktoru numpy.eye
#
# jednotková matice s rozměry 5x5 prvků

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.eye(5)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_19_eye_2D_array.py)

---

```python
# Příklady použití konstruktoru numpy.eye
#
# jednotková matice s rozměry 2x10 prvků

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.eye(2, 10)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_20_eye_2D_array.py)

---

```python
# Příklady použití konstruktoru numpy.eye
#
# jednotková matice s rozměry 10x10 prvků

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.eye(10, 10, dtype=numpy.float)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_21_eye_2D_array_dtype.py)

---

```python
# Příklady použití konstruktoru numpy.eye
#
# jednotková matice s rozměry 10x10 prvků

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.eye(10, 10, k=1)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_22_eye_2D_array_k_positive.py)

---

```python
# Příklady použití konstruktoru numpy.eye
#
# jednotková matice s rozměry 10x10 prvků

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.eye(10, 10, k=-1)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_23_eye_2D_array_k_negative.py)

---

```python
# Příklady použití konstruktoru numpy.eye
#
# jednotková matice s rozměry 10x10 prvků

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.eye(10, 10, k=10)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_24_eye_2D_array_k_10.py)

---

```python
# Příklady použití konstruktoru numpy.full
#
# matice s rozměry 1x10 prvků

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.full((10), 100)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_25_full_1D_array.py)

---

```python
# Příklady použití konstruktoru numpy.full
#
# matice s rozměry 3x4 prvků

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.full((3, 4), 100)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_26_full_2D_array.py)

---

```python
# Příklady použití konstruktoru numpy.full
#
# matice s rozměry 3x4x5 prvků

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.full((3, 4, 5), 100)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_27_full_3D_array.py)

---

```python
# Příklady použití konstruktoru numpy.full
#
# matice s rozměry 3x4x5 prvků

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.full((3, 4, 5), 100, dtype=numpy.float)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_28_full_dtype.py)

---

```python
# Příklady použití konstruktoru numpy.full
#
# matice s rozměry 3x4x5 prvků

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.full((3, 4, 5), numpy.inf)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_29_full_inf.py)

---

```python
# Příklady použití konstruktoru numpy.full
#
# matice s rozměry 3x4x5 prvků

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.full((3, 4, 5), numpy.inf, dtype=numpy.complex)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_30_full_inf_complex.py)

---

```python
# Funkce numpy.arange
#
# při použití jednoho parametru má tento parametr význam hodnoty „stop“
# vytvoří se vektor s prvky od 0 do „stop“ (kromě)

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.arange(10)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_31_arange_10.py)

---

```python
# Funkce numpy.arange
#
# specifikace hodnot „start“ (včetně) a „stop“ (kromě)

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.arange(10, 20)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_32_arange_10_20.py)

---

```python
# Funkce numpy.arange
#
# třetí nepovinný parametr určuje krok použitý při generování prvků vektoru

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.arange(10, 20, 2)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_33_arange_positive_step.py)

---

```python
# Funkce numpy.arange
#
# třetí nepovinný parametr určuje krok použitý při generování prvků vektoru

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.arange(20, 10, -2)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_34_arange_negative_step.py)

---

```python
# Funkce numpy.arange
#
# použít lze i hodnoty typu float

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.arange(0, 5.5, 0.5)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_35_arange_floats.py)

---

```python
# Funkce numpy.arange
#
# nemusíme zůstat pouze u celých čísel, protože pracovat je možné i s hodnotami
# typu float a complex

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.arange(0 + 0j, 10 + 10j, 2 + 0j)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_36_arange_complex.py)

---

```python
# Funkce numpy.arange
#
# nemusíme zůstat pouze u celých čísel, protože pracovat je možné i s hodnotami
# typu float a complex

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole - pozor na krok v reálné složce
a = numpy.arange(0 + 0j, 10 + 10j, 0 + 2j)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_37_arange_complex.py)

---

```python
# Použití funkce numpy.linspace
#
# pokud se nespecifikuje počet prvků, bude se předpokládat, že výsledný
# vektor má mít padesát prvků

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.linspace(1, 99)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_38_linspace_default_number_of_items.py)

---

```python
# Použití funkce numpy.linspace
#
# zde explicitně specifikujeme, že výsledný vektor má mít deset prvků
# (tím, že se začíná od nuly, získáme krok 0.11111111...)

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.linspace(0, 1, 10)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_39_linspace_specific_number_of_items.py)

---

```python
# Použití funkce numpy.linspace
#
# zde explicitně specifikujeme, že výsledný vektor má mít jedenáct prvků
# (tím, že se začíná od nuly, získáme krok 0.1)

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.linspace(0, 1, 11)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_40_linspace_specific_number_of_items.py)

---

```python
# Použití funkce numpy.linspace
#
# sekvence hodnot samozřejmě může i klesat

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.linspace(1, 0, 11)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_41_linspace_decrementing.py)

---

```python
# Použití funkce numpy.linspace
#
# použít je možné i komplexní čísla

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.linspace(0 + 0j, 1 + 0j, 10)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_42_linspace_complex_real_part.py)

---

```python
# Použití funkce numpy.linspace
#
# použít je možné i komplexní čísla

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.linspace(0 + 0j, 0 + 1j, 10)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_43_linspace_complex_imaginary_part.py)

---

```python
# Použití funkce numpy.linspace
#
# další možnost použití komplexních čísel

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.linspace(0 + 0j, 1 + 1j, 10)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_44_linspace_complex_both_parts.py)

---

```python
# Použití funkce numpy.geomspace
#
# pokud se nespecifikuje počet prvků, bude se předpokládat, že výsledný
# vektor má mít padesát prvků

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.geomspace(1, 100)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_45_geomspace_default_number_of_items.py)

---

```python
# Použití funkce numpy.geomspace
#
# zde explicitně specifikujeme, že výsledný vektor má mít deset prvků

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.geomspace(1, 1000, 10)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_46_geomspace_specific_number_of_items.py)

---

```python
# Použití funkce numpy.geomspace
#
# zde explicitně specifikujeme, že výsledný vektor má mít šest prvků

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.geomspace(1, 100000, 6)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_47_geomspace_specific_number_of_items.py)

---

```python
# Použití funkce numpy.geomspace
#
# zde explicitně specifikujeme, že výsledný vektor má mít šest prvků

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.geomspace(1, 100000, 6, dtype="I")

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_48_geomspace_dtype.py)

---

```python
# Použití funkce numpy.logspace
#
# pokud se nespecifikuje počet prvků, bude se předpokládat, že výsledný
# vektor má mít padesát prvků

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.logspace(1, 100)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_49_logspace_default_number_of_items.py)

---

```python
# Použití funkce numpy.logspace
#
# zde explicitně specifikujeme, že výsledný vektor má mít deset prvků

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.logspace(1, 10, 10)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_50_logspace_specific_number_of_items.py)

---

```python
# Použití funkce numpy.logspace
#
# zde explicitně specifikujeme, že výsledný vektor má mít pět prvků

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.logspace(1, 3, 5)

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_51_logspace_specific_number_of_items.py)

---

```python
# Použití funkce numpy.logspace
#
# zde explicitně specifikujeme, že výsledný vektor má mít pět prvků

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.logspace(1, 3, 5, dtype="I")

# tisk obsahu pole na standardní výstup
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_52_logspace_dtype.py)

---

```python
# Přetypování
#
# konstrukce pole přetypováním seznamu

# import hlavního balíčku knihovny Numpy
import numpy

# vytvoření běžného seznamu
lst = [1, 2, 3, 4]

# přetypování (konstrukce pole daného typu)
a = numpy.int64(lst)

# tisk typu a obsahu vytvořeného pole
print(type(a))
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_53_retype_int64_array.py)

---

```python
# Přetypování
#
# konstrukce pole přetypováním seznamu

# import hlavního balíčku knihovny Numpy
import numpy

# vytvoření běžného seznamu
lst = [1, "foo", 3, False, None]

# přetypování (konstrukce pole daného typu)
a = numpy.int64(lst)

# tisk typu a obsahu vytvořeného pole
print(type(a))
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_54_retype_int64_array_wrong_input.py)

---

```python
# Přetypování
#
# konstrukce pole přetypováním seznamu

# import hlavního balíčku knihovny Numpy
import numpy

# vytvoření běžného seznamu
lst = [1, 2, 3, 4]

# přetypování (konstrukce pole daného typu)
a = numpy.float16(lst)

# tisk typu a obsahu vytvořeného pole
print(type(a))
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_55_retype_float16_array.py)

---

```python
# Přetypování
#
# konstrukce pole přetypováním jiného pole

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce zdrojového pole
a = numpy.linspace(0, 1, 10)

# přetypování na vektor celých čísel (povšimněte si výsledků)
b = numpy.int32(a)

# tisk typu a obsahu původního pole
print(type(a))
print(a)

# tisk typu a obsahu vytvořeného pole
print(type(b))
print(b)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_56_retype_array_to_array.py)

---

```python
# Přetypování
#
# konstrukce pole přetypováním jiného pole

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce zdrojového pole
a = numpy.arange(0, 10)

# konverze
b = a.astype(numpy.complex64)

# tisk typu a obsahu původního pole
print(type(a))
print(a.dtype)
print(a)

# tisk typu a obsahu zkonvertovaného pole
print(type(b))
print(b.dtype)
print(b)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_57_astype1.py)

---

```python
# Příklady použití konstruktoru numpy.matrix
#
# matice s rozměry 1x4 prvky

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce matice
a = numpy.matrix("1 2 3 4")

# vytvoření pole z matice
b = numpy.array(a)

# tisk obsahu matice na standardní výstup
print(type(a))
print(a)

# tisk obsahu pole na standardní výstup
print(type(b))
print(b)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_58_matrix_string.py)

---

```python
# Příklady použití konstruktoru numpy.matrix
#
# matice s rozměry 2x2 prvky

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce matice
a = numpy.matrix("1 2; 3 4")

# vytvoření pole z matice
b = numpy.array(a)

# tisk obsahu matice na standardní výstup
print(type(a))
print(a)

# tisk obsahu pole na standardní výstup
print(type(b))
print(b)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_59_matrix_string_2D_array.py)

---

```python
# Příklady použití konstruktoru numpy.matrix
#
# matice s rozměry 2x2 prvky

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce matice
a = numpy.matrix("1 2 3; 4 5; 6")

# vytvoření pole z matice
b = numpy.array(a)

# tisk obsahu matice na standardní výstup
print(type(a))
print(a)

# tisk obsahu pole na standardní výstup
print(type(b))
print(b)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_60_matrix_string_2D_array_error.py)

---

```python
# Zjištění počtu dimenzí tvaru 1D pole

# import hlavního balíčku knihovny Numpy
import numpy

# jednorozměrný vektor
a = numpy.array([1, 2, 3])

# počet dimenzí vektoru
print(a.ndim)

# tvar vektoru
print(a.shape)

# typ prvků
print(a.dtype.name)

# velikost prvků v bajtech
print(a.itemsize)

# velikost pole (počet prvků)
print(a.size)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_61_info_about_1D_array.py)

---

```python
# Zjištění počtu dimenzí tvaru 2D pole

# import hlavního balíčku knihovny Numpy
import numpy

# dvourozměrné pole
a = numpy.eye(5)

# počet dimenzí vektoru
print(a.ndim)

# tvar vektoru
print(a.shape)

# typ prvků
print(a.dtype.name)

# velikost prvků v bajtech
print(a.itemsize)

# velikost pole (počet prvků)
print(a.size)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_62_info_about_2D_array.py)

---

```python
# Zjištění počtu dimenzí tvaru 3D pole

# import hlavního balíčku knihovny Numpy
import numpy

# trojrozměrné pole
a = numpy.ones((3, 4, 5), dtype=int)

# počet dimenzí vektoru
print(a.ndim)

# tvar vektoru
print(a.shape)

# typ prvků
print(a.dtype.name)

# velikost prvků v bajtech
print(a.itemsize)

# velikost pole (počet prvků)
print(a.size)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_63_info_about_3D_array.py)

---

```python
# Tisk velkých polí

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce velkého pole
a = numpy.arange(10000).reshape(100, 100)

# tisk velkého pole
print(a)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_64_print_big_array.py)

---

```python
# Změna tvaru pole

# import hlavního balíčku knihovny Numpy
import numpy

# běžná matice se dvěma řádky a třemi sloupci
a = numpy.array([[1, 2, 3], [4, 5, 6]])

# změna tvaru matice na 3x2 prvky
b = numpy.reshape(a, (3, 2))

# tisk původní matice
print(a)

# tisk nové matice
print(b)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_65_reshape1.py)

---

```python
# Změna tvaru pole
# zde vlastně dostaneme původní matici

# import hlavního balíčku knihovny Numpy
import numpy

# běžná matice se dvěma řádky a třemi sloupci
a = numpy.array([[1, 2, 3], [4, 5, 6]])

# změna tvaru matice na 3x2 prvky
b = numpy.reshape(a, (2, 3))

# tisk původní matice
print(a)

# tisk nové matice
print(b)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_66_reshape2.py)

---

```python
# Změna tvaru pole - vytvoření matice s jediným řádkem

# import hlavního balíčku knihovny Numpy
import numpy

# běžná matice se dvěma řádky a třemi sloupci
a = numpy.array([[1, 2, 3], [4, 5, 6]])

# změna tvaru matice na jediný řádek
b = numpy.reshape(a, (1, 6))

# tisk původní matice
print(a)

# tisk nové matice
print(b)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_67_reshape3.py)

---

```python
# Změna tvaru pole - vytvoření matice s jediným sloupcem

# import hlavního balíčku knihovny Numpy
import numpy

# běžná matice se dvěma řádky a třemi sloupci
a = numpy.array([[1, 2, 3], [4, 5, 6]])

# změna tvaru matice na jediný sloupec
b = numpy.reshape(a, (6, 1))

# tisk původní matice
print(a)

# tisk nové matice
print(b)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_68_reshape4.py)

---

```python
# Výběr prvků v poli

# import hlavního balíčku knihovny Numpy
import numpy

# jednorozměrná pole - vektory
a = numpy.arange(12)

# tisk původního pole
print(a)

# indexování prvků od nuly
print(a[0])

# indexování prvků od nuly
print(a[5])

# indexovat lze i od konce pole
print(a[-1])

# indexovat lze i od konce pole
print(a[-5])
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_69_selectors_1D_array.py)

---

```python
# Výběr prvků v poli

# import hlavního balíčku knihovny Numpy
import numpy

# dvourozměrná pole - matice
a = numpy.reshape(numpy.arange(12), (3, 4))

# tisk původního pole
print(a)

# přístup k prvkům: řádek/sloupec
print(a[0][2])

# přístup k prvkům: řádek/sloupec
print(a[2][0])
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_70_selectors_2D_array.py)

---

```python
# Výběr prvků pomocí indexů uložených v jiném poli
# (kladné indexy)

# import hlavního balíčku knihovny Numpy
import numpy

# jednorozměrná pole - vektory
a = numpy.arange(12)

# tisk původního pole
print(a)

# pole indexů
b = numpy.array([1, 2, 9, 8, 5])

# výběr celým polem
print(a[b])
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_71_select_by_other_array.py)

---

```python
# Výběr prvků pomocí indexů uložených v jiném poli
# (záporné indexy)

# import hlavního balíčku knihovny Numpy
import numpy

# jednorozměrná pole - vektory
a = numpy.arange(12)

# tisk původního pole
print(a)

# pole indexů
b = numpy.array([-1, -2, -9, -8, -5])

# výběr celým polem
print(a[b])
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_72_select_by_other_array_negative_indexes.py)

---

```python
# Výběr řádku pole

# import hlavního balíčku knihovny Numpy
import numpy

# dvourozměrné pole - matice
a = numpy.reshape(numpy.arange(12), (3, 4))

# tisk původního pole
print(a)

# první řádek pole
b = a[0]
print(b)

# druhý řádek pole
b = a[1]
print(b)

# poslední řádek pole
b = a[-1]
print(b)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_73_select_rows.py)

---

```python
# Výběr prvků pomocí indexů uložených v jiném poli
# dtto ale s dvourozměrným polem

# import hlavního balíčku knihovny Numpy
import numpy

a = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# pro nové pole s prohozenými řádky
b = numpy.array([0, 2, 1])

# tisk pole
print(a[b])
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_74_select_from_2D_array.py)

---

```python
# Slicing - vynechání indexu/indexů

# import hlavního balíčku knihovny Numpy
import numpy

# původní pole
a = numpy.arange(12)

# tisk původního pole
print(a)

# slicing
b = a[3:7]

# tisk nového pole
print(b)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_75_slicing.py)

---

```python
# Slicing - vynechání indexu/indexů

# import hlavního balíčku knihovny Numpy
import numpy

# původní pole
a = numpy.arange(12)

# tisk původního pole
print(a)

# slicing
b = a[:7]

# tisk nového pole
print(b)

# slicing
c = a[5:]

# tisk nového pole
print(c)

# slicing
d = a[:]

# tisk nového pole
print(d)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_76_slicing.py)

---

```python
# Prázdný řez polem

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.arange(12)

# provedení řezu polem
print(a[-4:-6])
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_77_empty_slice.py)

---

```python
# Řezy a záporné indexy

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.arange(12)

# provedení prvního řezu polem
print(a[-6:-4])

# provedení druhého řezu polem
print(a[-6:])

# provedení třetího řezu polem
print(a[:-4])
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_78_slicing_negative_indexes.py)

---

```python
# Řezy vícerozměrných polí

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.reshape(numpy.arange(25), (5, 5))

# řez dvojrozměrným polem
print(a[2:4, 3])

# další řez dvojrozměrným polem
print(a[2:4, 3:5])

# třetí řez dvojrozměrným polem
print(a[1:4, 1:4])

# čtvrtý řez dvojrozměrným polem
print(a[-4:-2, -4:-2])
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_79_slicing_2d_arrays.py)

---

```python
# Specifikace kroku při provádění řezů - vektory

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.arange(1, 11)

# první řez polem: krok=1
print(a[1:10:1])

# druhý řez polem: krok=2
print(a[1:10:2])

# třetí řez polem: krok=3
print(a[1:10:3])

# čtvrtý řez polem - pouze uvedení kroku
a[::3]
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_80_slicing_specify_steps.py)

---

```python
# Specifikace kroku při provádění řezů - matice

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.reshape(numpy.arange(0, 25), (5, 5))

# tisk původního pole
print(a)

# řez s uvedením kroku
print(a[0:5:2])
print(a[1::2])
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_81_slicing_matrix_steps.py)

---

```python
# Přičtení hodnoty ke všem prvkům matice

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# provedení operace
b = a + 100

# tisk původního pole
print(a)

# tisk nového pole
print(b)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_82_add_item_by_scalar.py)

---

```python
# Vynásobení prvků matice dvěma

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# provedení operace
b = a * 2

# tisk původního pole
print(a)

# tisk nového pole
print(b)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_83_mul_item_by_scalar.py)

---

```python
# Podíl prvek po prvku

# import hlavního balíčku knihovny Numpy
import numpy

# konstrukce pole
a = numpy.reshape(numpy.arange(25), (5, 5))

# provedení operace
b = a % 2

# tisk původního pole
print(a)

# tisk nového pole
print(b)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_84_div_item_by_scalar.py)

---

```python
# Operátory
# pole op pole

# import hlavního balíčku knihovny Numpy
import numpy

# první pole
a1 = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# druhé pole
a2 = numpy.eye(3)

# součet prvek po prvku
c = a1 + a2

# tisk nového pole
print(c)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_85_add_item_by_item.py)

---

```python
# Modifikace matice s využitím operátorů += atd.

# import hlavního balíčku knihovny Numpy
import numpy

# původní matice
a1 = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# tisk matice
print(a1)

# provedení operace
a1 += 100

# tisk výsledku operace
print(a1)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_86_operator_pluseq.py)

---

```python
# Násobení matic
# - Operátor @, nikoli *

# import hlavního balíčku knihovny Numpy
import numpy

# původní matice
a1 = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# původní matice
a2 = numpy.eye(3)

# - Násobení prvek po prvku
c = a1 * a2

# tisk výsledku operace
print(c)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_87_not_matrix_multiplication.py)

---

```python
# Násobení matic
# - Maticový součin

# import hlavního balíčku knihovny Numpy
import numpy

# původní matice
a1 = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# původní matice
a2 = numpy.eye(3)

# maticový součin
c = a1 @ a2

# tisk výsledku operace
print(c)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_88_matrix_multiplication.py)

---

```python
# Násobení matic
# - Maticový součin

# import hlavního balíčku knihovny Numpy
import numpy

# původní matice
a1 = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# původní matice
a2 = numpy.eye(3)

# - Změna prvku původně jednotkové matice
a2[1][1] = -1

# tisk výsledku operace
print(a1 @ a2)

# maticový součin
c = a1 @ a2

# tisk výsledku operace
print(c)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//numpy_89_check_matrix_multiplication.py)

---

## Matplotlib

![Matplotlib](images/matplotlib.png)

---

```python
# - vykreslení průběhu funkce sin

import numpy as np
import matplotlib.pyplot as plt

# hodnoty na x-ové ose
x = np.linspace(0, 2 * np.pi, 100)

# hodnoty na y-ové ose
y = np.sin(x)

# vykreslit průběh funkce
plt.plot(x, y)

# popis os
plt.xlabel("x")
plt.ylabel("sin(x)")

# zobrazení grafu
plt.show()
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//matplotlib_example01.py)

---

```python
# - vykreslení průběhu funkce sin

import numpy as np
import matplotlib.pyplot as plt

# hodnoty na x-ové ose
x = np.linspace(0, 2 * np.pi, 100)

# hodnoty na y-ové ose
y = np.sin(x)

# vykreslit průběh funkce
plt.plot(x, y)

# popis os
plt.xlabel("x")
plt.ylabel("sin(x)")

# zobrazení grafu
plt.show()
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//matplotlib_example01.py)

---

```python
# - vykreslení průběhu funkce sin
# - uložení grafu do různých typů souboru

import numpy as np
import matplotlib.pyplot as plt

# hodnoty na x-ové ose
x = np.linspace(0, 2 * np.pi, 100)

# hodnoty na y-ové ose
y = np.sin(x)

# vykreslit průběh funkce
plt.plot(x, y)

# popis os
plt.xlabel("x")
plt.ylabel("sin(x)")

# vykreslení a uložení grafu do různých typů souborů
plt.savefig("example02.png")
plt.savefig("example02.pdf")
plt.savefig("example02.eps")
plt.savefig("example02.ps")
plt.savefig("example02.svg")

# zobrazení grafu
plt.show()
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//matplotlib_example02.py)

---

```python
# - vykreslení průběhů funkcí sin a cos
#   do jediného grafu

import numpy as np
import matplotlib.pyplot as plt

# hodnoty na x-ové ose
x = np.linspace(0, 2 * np.pi, 100)

# hodnoty na y-ové ose: první funkce
y1 = np.sin(x)

# hodnoty na y-ové ose: druhá funkce
y2 = np.cos(x)

# vykreslit průběh obou funkcí
plt.plot(x, y1, x, y2)

# popis os
plt.xlabel("x")
plt.ylabel("sin(x) a cos(x)")

# zobrazení grafu
plt.show()
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//matplotlib_example03.py)

---

```python
# - vykreslení průběhů funkcí sin a cos a sinc
#   do jediného grafu
# - změna stylu vykreslování průběhů funkcí

import numpy as np
import matplotlib.pyplot as plt

# hodnoty na x-ové ose
x = np.linspace(0.01, 2 * np.pi, 100)

# hodnoty na y-ové ose: první funkce
y1 = np.sin(x)

# hodnoty na y-ové ose: druhá funkce
y2 = np.cos(x)

# hodnoty na y-ové ose: třetí funkce
y3 = np.sin(x) / x

# vykreslit průběh všech tří funkcí
# se změnou stylu vykreslování
plt.plot(x, y1, "b-", label="sin")
plt.plot(x, y2, "r.", label="cos")
plt.plot(x, y3, "g--", label="sinc")

# přidání legendy
plt.legend(loc="lower left")

# popis os
plt.xlabel("x")
plt.ylabel("sin(x), cos(x) a sinc(x)")

# zobrazení grafu
plt.show()
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//matplotlib_example04.py)

---

```python
# - vykreslení průběhů funkcí sin a sinc
#   do jediného grafu
#   s vyplněním plochy pod průběhu

import numpy as np
import matplotlib.pyplot as plt

# hodnoty na x-ové ose
x = np.linspace(0, 2 * np.pi, 100)

# hodnoty na y-ové ose: první funkce
y1 = np.sin(x)

# hodnoty na y-ové ose: druhá funkce
y2 = np.sin(3 * x) / (x + 1)

# vykreslit průběh obou funkcí
# se změnou stylu vykreslování
plt.fill(x, y1, "red", x, y2, "yellow", alpha=0.3)

# popis os
plt.xlabel("x")
plt.ylabel("sin(x) a sinc(3x)")

# zobrazení grafu
plt.show()
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//matplotlib_example05.py)

---

```python
# - vykreslení průběhů čtyř různých funkcí
#   do jediného grafu
#   s vyplněním plochy pod průběhu
# - kombinace různých stylů vykreslení

import numpy as np
import matplotlib.pyplot as plt

# hodnoty na x-ové ose
x = np.linspace(0.001, 2 * np.pi, 100)

# hodnoty na y-ové ose: první funkce
y1 = np.sin(5 * x)

# hodnoty na y-ové ose: druhá funkce
y2 = np.sin(5 * x) / (x + 1 / 2)

# hodnoty na y-ové ose: třetí čtvrtá funkce
y3 = 1 / (x + 1 / 2)
y4 = -y3

# vykreslit průběh obou funkcí
# se změnou stylu vykreslování
plt.fill(x, y1, "yellow", alpha=0.3, label="sin x")
plt.fill(x, y2, "r.", alpha=1.0, label="sinc 5x")
plt.plot(x, y3, "g--", label="obalka sinc")
plt.plot(x, y4, "g--", label="obalka sinc")

# přidání legendy
plt.legend(loc="upper right")

# popis os
plt.xlabel("x")
plt.ylabel("sin(x) a sinc(3x)")

# zobrazení grafu
plt.show()
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//matplotlib_example06.py)

---

```python
# - vykreslení průběhů funkcí sin a cos
# - nastavení mřížky
# - nastavení rozsahů na obou osách

import numpy as np
import matplotlib.pyplot as plt

# hodnoty na x-ové ose
x = np.linspace(0, 2 * np.pi, 100)

# hodnoty na y-ové ose: první funkce
y1 = np.sin(x)

# hodnoty na y-ové ose: druhá funkce
y2 = np.cos(x)

# vykreslit průběh obou funkcí
# se změnou stylu vykreslování
plt.plot(x, y1, "b-", label="sin")
plt.plot(x, y2, "r-", label="cos")

# přidání legendy
plt.legend(loc="lower left")

# nastavení rozsahů na obou osách
plt.axis([-1, 8, -1.5, 1.5])

# povolení zobrazení mřížky
plt.grid(True)

# popis os
plt.xlabel("x")
plt.ylabel("sin(x) a cos(x)")

# zobrazení grafu
plt.show()
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//matplotlib_example07.py)

---

```python
# - vykreslení průběhů funkcí sin a cos
# - nastavení mřížky
# - nastavení rozsahů na obou osách
# - přidání popisku přímo do grafu

import numpy as np
import matplotlib.pyplot as plt

# hodnoty na x-ové ose
x = np.linspace(0, 2 * np.pi, 100)

# hodnoty na y-ové ose: první funkce
y1 = np.sin(x)

# hodnoty na y-ové ose: druhá funkce
y2 = np.cos(x)

# vykreslit průběh obou funkcí
# se změnou stylu vykreslování
plt.plot(x, y1, "b-", label="sin")
plt.plot(x, y2, "r-", label="cos")

# přidání legendy
plt.legend(loc="lower left")

# nastavení rozsahů na obou osách
plt.axis([-1, 8, -1.5, 1.5])

# povolení zobrazení mřížky
plt.grid(True)

# popis os
plt.xlabel("x")
plt.ylabel("sin(x) a cos(x)")

# vložit první popisek do grafu
plt.annotate(
    "maximální hodnota sin(x)",
    xy=(np.pi / 2, 1.0),
    xytext=(1, 1.3),
    arrowprops=dict(arrowstyle="->"),
)

# vložit druhý popisek do grafu
plt.annotate(
    "minimální hodnota cos(x)",
    xy=(np.pi, -1.0),
    xytext=(2, -1.3),
    arrowprops=dict(arrowstyle="->"),
)

# zobrazení grafu
plt.show()
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//matplotlib_example08.py)

---

```python
# - základní polární graf

import numpy as np
import matplotlib.pyplot as plt

# úhel v polárním grafu
theta = np.linspace(0.01, 2 * np.pi, 150)

# vzdálenost od středu
radius = np.log(theta)

ax = plt.subplot(111, projection="polar")

# vykreslit průběh funkce
# v polárním grafu
ax.plot(theta, radius)

# zobrazení grafu
plt.show()
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//matplotlib_example09.py)

---

```python
# - vykreslení průběhů několika funkcí
# - do polárního grafu

import numpy as np
import matplotlib.pyplot as plt

# úhel v polárním grafu
theta = np.linspace(0.01, 2 * np.pi, 150)

# první funkce: vzdálenost od středu
radius1 = theta

# druhá funkce: vzdálenost od středu
radius2 = 2 * np.abs(theta - np.pi)

# třetí funkce: vzdálenost od středu
radius3 = 2 * np.log(theta)

ax = plt.subplot(111, projection="polar")

# vykreslit průběh první funkce
# v polárním grafu
ax.plot(theta, radius1, "r.", label="f1")

# vykreslit průběh druhé funkce
# v polárním grafu
ax.plot(theta, radius2, "g", label="f2")

# vykreslit průběh třetí funkce
# v polárním grafu
ax.plot(theta, radius3, "b--", label="f3")

# přidání legendy
plt.legend(loc="lower left")

# zobrazení grafu
plt.show()
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//matplotlib_example10.py)

---

```python
# - vykreslení průběhů několika funkcí
# - do polárního grafu

import numpy as np
import matplotlib.pyplot as plt

# úhel v polárním grafu
theta = np.linspace(0.01, 4 * np.pi, 150)

# první funkce: vzdálenost od středu
radius1 = theta

# druhá funkce: vzdálenost od středu
radius2 = 3 * np.abs(theta - 2 * np.pi)

ax = plt.subplot(111, projection="polar")

# vykreslit průběh první funkce
# v polárním grafu
ax.plot(theta, radius2, "b", label="f1")

# vykreslit průběh druhé funkce
# v polárním grafu
ax.fill(theta, radius1, "yellow", alpha=0.3, label="f1")

# přidání legendy
plt.legend(loc="lower left")

# zobrazení grafu
plt.show()
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//matplotlib_example11.py)

---

```python
# - vykreslení průběhu funkce sinc
# - při vykreslování se jednotlivé body spojí úsečkami

import numpy as np
import matplotlib.pyplot as plt

# hodnoty na x-ové ose
x = np.linspace(0.2, 2 * np.pi, 100)

# hodnoty na y-ové ose
y = np.sin(5 * x) / x
y2 = 1 / x
y3 = -y2

# vykreslit průběh funkce
plt.plot(x, y2, color="red", label="obalka sinc")
plt.plot(x, y3, color="red", label="obalka sinc")
plt.plot(x, y, color="blue", label="sinc(x)")

# povolení zobrazení mřížky
plt.grid(True)

# popis os
plt.xlabel("x")
plt.ylabel("sinc(x)")

# přidání legendy
plt.legend(loc="lower right")

# zobrazení grafu
plt.show()
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//matplotlib_example12.py)

---

```python
# - vykreslení průběhu funkce sinc
# - při vykreslování se použijí "schodky"

import numpy as np
import matplotlib.pyplot as plt

# hodnoty na x-ové ose
x = np.linspace(0.2, 2 * np.pi, 100)

# hodnoty na y-ové ose
y = np.sin(5 * x) / x
y2 = 1 / x
y3 = -y2

# vykreslit průběh funkce
plt.plot(x, y2, color="red", label="obalka sinc", drawstyle="default")
plt.plot(x, y3, color="red", label="obalka sinc", drawstyle="default")
plt.plot(x, y, color="blue", label="sinc(x)", drawstyle="steps")

# povolení zobrazení mřížky
plt.grid(True)

# popis os
plt.xlabel("x")
plt.ylabel("sinc(x)")

# přidání legendy
plt.legend(loc="lower right")

# zobrazení grafu
plt.show()
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//matplotlib_example13.py)

---

```python
# - jednoduchý sloupcový graf

import numpy as np
import matplotlib.pyplot as plt

# historické ceny ropy
cena_ropy = [
    46.68,
    44.68,
    46.90,
    47.15,
    44.59,
    44.00,
    44.63,
    45.92,
    44.15,
    45.94,
    46.05,
    46.75,
    46.25,
    45.41,
    49.20,
    45.22,
    42.56,
    38.60,
    39.31,
    38.24,
    40.45,
    41.32,
    40.80,
    42.62,
    41.87,
    42.50,
    42.23,
    43.30,
    43.08,
    44.96,
    43.87,
    44.66,
    45.15,
    47.12,
    48.52,
    48.79,
    47.98,
    47.39,
    48.14,
    48.45,
]

# počet prvků
N = len(cena_ropy)

# indexy prvků
indexes = np.arange(N)

# šířka sloupců
width = 1.00

# sloupcový graf
plt.bar(indexes, cena_ropy, width, color="yellow", edgecolor="black", label="Cena ropy")

# povolení zobrazení mřížky
plt.grid(True)

# přidání legendy
plt.legend(loc="lower right")

# zobrazení grafu
plt.show()
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//matplotlib_example14.py)

---

```python
# - sloupcový graf se dvěma skupinami sloupců

import numpy as np
import matplotlib.pyplot as plt

# první pole hodnot
vals1 = [10, 15, 20, 12, 14, 8]

# druhé pole hodnot
vals2 = [19, 18, 6, 11, 6, 14]

# počet prvků
N = len(vals1)

# indexy prvků
indexes = np.arange(N)

# šířka sloupců
width = 0.30

# sloupcový graf se dvěma skupinami sloupců
plt.bar(indexes, vals1, width, color="gray", edgecolor="black", label="CPU#1")
# posunuté sloupce
plt.bar(indexes + width, vals2, width, color="red", edgecolor="black", label="CPU#2")

# povolení zobrazení mřížky
plt.grid(True)

# přidání legendy
plt.legend(loc="lower right")

# zobrazení grafu
plt.show()
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//matplotlib_example15.py)

---

```python
# - jednoduchý histogram

import numpy as np
import matplotlib.pyplot as plt

# náhodné hodnoty
y = np.random.normal(0, 0.1, 10000)

plt.hist(y, bins=30, range=None, density=True)

# zobrazení grafu
plt.show()
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//matplotlib_example16.py)

---

```python
# - koláčový graf

from matplotlib import pyplot as plt

# make a square figure and axes
fig = plt.figure(1, figsize=(6, 6), dpi=50)
ax = fig.add_axes([0.16, 0.16, 0.68, 0.68])

plt.title("Scripting languages")
ax.title.set_fontsize(30)

# popisky jednotlivých výřezů
labels = ["Perl", "Python", "Ruby"]

# šířky jednotlivých výřezů
fracs = [90, 150, 70]

# vytvoření koláčového grafu
ax.pie(fracs, labels=labels, autopct="%1.1f%%", shadow=True)

# zobrazení grafu
plt.show()
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//matplotlib_example17.py)

---

```python
# - změna stylu koláčových grafů

from matplotlib import pyplot as plt
from matplotlib import font_manager as fm


# make a square figure and axes
fig = plt.figure(1, figsize=(6, 6), dpi=50)
ax = fig.add_axes([0.16, 0.16, 0.68, 0.68])

plt.title("Scripting languages")
ax.title.set_fontsize(30)

# popisky jednotlivých výřezů
labels = ["Perl", "Python", "Ruby"]

# šířky jednotlivých výřezů
fracs = [90, 150, 70]

# vytáhnutí výřezů
explode = (0.0, 0.0, 0.15)

# barvy
colors = ("yellow", "#60ff60", "red")

# vytvoření koláčového grafu
patches, texts, autotexts = ax.pie(
    fracs, explode=explode, colors=colors, labels=labels, autopct="%1.1f%%", shadow=True
)

# změna stylu písma
proptease = fm.FontProperties()
proptease.set_size("xx-large")
plt.setp(autotexts, fontproperties=proptease)
plt.setp(texts, fontproperties=proptease)

# zobrazení grafu
plt.show()
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//matplotlib_example18.py)

---

```python
# - sloupcový graf se dvěma skupinami sloupců
#   a se zobrazením odchylek

import numpy as np
import matplotlib.pyplot as plt

# první pole hodnot a pole odchylek
vals1 = [10, 15, 20, 12, 14, 8]
delta1 = [1, 2, 3, 4, 5, 0]

# druhé pole hodnot a pole odchylek
vals2 = [19, 18, 6, 11, 6, 14]
delta2 = [4, 2, 3, 2, 2, 4]

# počet prvků
N = len(vals1)

# indexy prvků
indexes = np.arange(N)

# šířka sloupců
width = 0.30

# sloupcový graf se dvěma skupinami sloupců
plt.bar(
    indexes, vals1, width, color="gray", edgecolor="black", label="CPU#1", yerr=delta1
)

# posunuté sloupce
plt.bar(
    indexes + width,
    vals2,
    width,
    color="red",
    edgecolor="black",
    label="CPU#2",
    yerr=delta2,
)

# povolení zobrazení mřížky
plt.grid(True)

# přidání legendy
plt.legend(loc="lower right")

# zobrazení grafu
plt.show()
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//matplotlib_example19.py)

---

```python
# - sloupcový graf se dvěma skupinami sloupců
#   a se zobrazením odchylek

import numpy as np
import matplotlib.pyplot as plt

# první pole hodnot a pole odchylek
vals1 = [10, 15, 20, 12, 14, 8]
delta1 = [1, 2, 3, 4, 5, 0]

# druhé pole hodnot a pole odchylek
vals2 = [19, 18, 6, 11, 6, 14]
delta2 = [4, 2, 3, 2, 2, 4]

# počet prvků
N = len(vals1)

# indexy prvků
indexes = np.arange(N)

# šířka sloupců
width = 0.30

# sloupcový graf se dvěma skupinami sloupců
plt.bar(
    indexes,
    vals1,
    width,
    color="gray",
    edgecolor="black",
    label="CPU#1",
    yerr=delta1,
    error_kw=dict(elinewidth=2, ecolor="red"),
)

# posunuté sloupce
plt.bar(
    indexes + width,
    vals2,
    width,
    color="red",
    edgecolor="black",
    label="CPU#2",
    yerr=delta2,
    error_kw=dict(elinewidth=2, ecolor="black"),
)

# povolení zobrazení mřížky
plt.grid(True)

# přidání legendy
plt.legend(loc="lower right")

# zobrazení grafu
plt.show()
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//matplotlib_example20.py)

---

```python
# - zobrazení kontur funkce typu z=f(x,y)

import numpy as np
import matplotlib.pyplot as plt


delta = 0.1

# průběh nezávislé proměnné x
x = np.arange(-10.0, 10.0, delta)

# průběh nezávislé proměnné y
y = np.arange(-10.0, 10.0, delta)

# vytvoření dvou polí se souřadnicemi [x,y]
X, Y = np.meshgrid(x, y)

# vzdálenost od bodu [0,0]
R1 = np.sqrt(X * X + Y * Y)

# vzdálenost od bodu [3,3]
R2 = np.sqrt((X - 3) * (X - 3) + (Y - 3) * (Y - 3))

# výpočet funkce, kterou použijeme při vykreslování grafu
Z = np.sin(R1) - np.cos(R2)

# povolení zobrazení mřížky
plt.grid(True)

# vytvoření grafu s konturami funkce z=f(x,y)
plt.contour(X, Y, Z)

# zobrazení grafu
plt.show()
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//matplotlib_example21.py)

---

```python
# - zobrazení kontur funkce typu z=f(x,y)
# - zobrazení hodnot u jednotlivých "vrstevnic"

import numpy as np
import matplotlib.pyplot as plt


delta = 0.1

# průběh nezávislé proměnné x
x = np.arange(-10.0, 10.0, delta)

# průběh nezávislé proměnné y
y = np.arange(-10.0, 10.0, delta)

# vytvoření dvou polí se souřadnicemi [x,y]
X, Y = np.meshgrid(x, y)

# vzdálenost od bodu [0,0]
R1 = np.sqrt(X * X + Y * Y)

# vzdálenost od bodu [3,3]
R2 = np.sqrt((X - 3) * (X - 3) + (Y - 3) * (Y - 3))

# výpočet funkce, kterou použijeme při vykreslování grafu
Z = np.sin(R1) - np.cos(R2)

# povolení zobrazení mřížky
plt.grid(True)

# vytvoření grafu s konturami funkce z=f(x,y)
CS = plt.contour(X, Y, Z)

# popisky "vrstevnic"
plt.clabel(CS, inline=1, fontsize=10)

# zobrazení grafu
plt.show()
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//matplotlib_example22.py)

---

```python
# - zobrazení kontur funkce typu z=f(x,y)
# - zobrazení hodnot u jednotlivých "vrstevnic"
# - přidání legendy

import numpy as np
import matplotlib.pyplot as plt


delta = 0.1

# průběh nezávislé proměnné x
x = np.arange(-10.0, 10.0, delta)

# průběh nezávislé proměnné y
y = np.arange(-10.0, 10.0, delta)

# vytvoření dvou polí se souřadnicemi [x,y]
X, Y = np.meshgrid(x, y)

# vzdálenost od bodu [0,0]
R1 = np.sqrt(X * X + Y * Y)

# vzdálenost od bodu [3,3]
R2 = np.sqrt((X - 3) * (X - 3) + (Y - 3) * (Y - 3))

# výpočet funkce, kterou použijeme při vykreslování grafu
Z = np.sin(R1) - np.cos(R2)

# povolení zobrazení mřížky
plt.grid(True)

# vytvoření grafu s konturami funkce z=f(x,y)
CS = plt.contour(X, Y, Z)

# přidání legendy (colorbar)
CB = plt.colorbar(CS, shrink=0.7, extend="both")

# popisky "vrstevnic"
plt.clabel(CS, inline=1, fontsize=10)

# zobrazení grafu
plt.show()
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//matplotlib_example23.py)

---

```python
# - zobrazení 3D grafu funkce typu z=f(x,y)

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

delta = 0.1

# průběh nezávislé proměnné x
x = np.arange(-10.0, 10.0, delta)

# průběh nezávislé proměnné y
y = np.arange(-10.0, 10.0, delta)

# vytvoření dvou polí se souřadnicemi [x,y]
X, Y = np.meshgrid(x, y)

# vzdálenost od bodu [0,0]
R = np.sqrt(X * X + Y * Y)

# výpočet funkce, kterou použijeme při vykreslování grafu
Z = np.sin(R) / R

# zobrazení 3D grafu
ax.plot_wireframe(X, Y, Z, rstride=7, cstride=7)

# zobrazení grafu
plt.show()
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//matplotlib_example24.py)

---

```python
# - zobrazení 3D grafu funkce typu z=f(x,y)

from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection="3d")

delta = 0.1

# průběh nezávislé proměnné x
x = np.arange(-10.0, 10.0, delta)

# průběh nezávislé proměnné y
y = np.arange(-10.0, 10.0, delta)

# vytvoření dvou polí se souřadnicemi [x,y]
X, Y = np.meshgrid(x, y)

# vzdálenost od bodu [0,0]
R = np.sqrt(X * X + Y * Y)

# výpočet funkce, kterou použijeme při vykreslování grafu
Z = np.sin(R) / R

# zobrazení 3D grafu formou plochy
ax.plot_surface(
    X, Y, Z, rstride=2, cstride=2, cmap=cm.coolwarm, linewidth=0, antialiased=False
)

# zobrazení grafu
plt.show()
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//matplotlib_example25.py)

---

```python
# - zobrazení 3D grafu funkce typu z=f(x,y)
# - pomocná legenda - colorbar

from matplotlib import cm
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

fig = plt.figure()
ax = fig.gca(projection="3d")

delta = 0.1

# průběh nezávislé proměnné x
x = np.arange(-10.0, 10.0, delta)

# průběh nezávislé proměnné y
y = np.arange(-10.0, 10.0, delta)

# vytvoření dvou polí se souřadnicemi [x,y]
X, Y = np.meshgrid(x, y)

# vzdálenost od bodu [0,0]
R = np.sqrt(X * X + Y * Y)

# výpočet funkce, kterou použijeme při vykreslování grafu
Z = np.sin(R) / R

# zobrazení 3D grafu formou plochy
surface = ax.plot_surface(
    X, Y, Z, rstride=2, cstride=2, cmap=cm.coolwarm, linewidth=0, antialiased=False
)

ax.set_zlim(-1.01, 1.01)

# styl formátování popisků
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter("%.02f"))

# přidání pomocné legendy
fig.colorbar(surface, shrink=0.7, aspect=5)

# zobrazení grafu
plt.show()
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//matplotlib_example26.py)

---

```python
# - zobrazení 3D grafu funkce typu z=f(x,y)
# - pomocná legenda - colorbar
# - promítnutí grafu na ploch kolmých na osy

from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection="3d")

delta = 0.1

# průběh nezávislé proměnné x
x = np.arange(-10.0, 10.0, delta)

# průběh nezávislé proměnné y
y = np.arange(-10.0, 10.0, delta)

# vytvoření dvou polí se souřadnicemi [x,y]
X, Y = np.meshgrid(x, y)

# vzdálenost od bodu [0,0]
R = np.sqrt(X * X + Y * Y)

# výpočet funkce, kterou použijeme při vykreslování grafu
Z = np.sin(R) / R

# zobrazení 3D grafu formou plochy
surface = ax.plot_surface(
    X, Y, Z, rstride=2, cstride=2, cmap=cm.coolwarm, linewidth=0, antialiased=False
)

# kontutra: průmět na rovinu x-y
cset = ax.contour(X, Y, Z, zdir="z", offset=-5, cmap=cm.coolwarm)

# kontutra: průmět na rovinu y-z
cset = ax.contour(X, Y, Z, zdir="x", offset=-15, cmap=cm.coolwarm)

# kontutra: průmět na rovinu x-z
cset = ax.contour(X, Y, Z, zdir="y", offset=15, cmap=cm.coolwarm)

# rozměry grafu ve směru osy x
ax.set_xlabel("X")
ax.set_xlim(-15, 15)

# rozměry grafu ve směru osy y
ax.set_ylabel("Y")
ax.set_ylim(-15, 15)

# rozměry grafu ve směru osy z
ax.set_zlabel("Z")
ax.set_zlim(-5, 5)

# zobrazení grafu
plt.show()
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//matplotlib_example27.py)

---

```python
# - zobrazení 3D grafu funkce typu [x,y,z]=f(t)

import matplotlib.pyplot as plt
import numpy as np

# nezávislá proměnná
t = np.arange(0, 8 * np.pi, 0.1)

# vzdálenost od osy spirály
r = 10.0 / (t + 4)

# výpočet souřadnic [x,y,z]) pro každé t
x = r * np.cos(t)
y = r * np.sin(t)
z = t

fig = plt.figure()
ax = fig.gca(projection="3d")

# vykreslení grafu
ax.plot(x, y, z)

# zobrazení grafu
plt.show()
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//matplotlib_example28.py)

---

```python
# - Lorenzův atraktor

import matplotlib.pyplot as plt
import numpy as np


# funkce pro výpočet dalšího bodu Lorenzova atraktoru
def lorenz(x, y, z, s=10, r=28, b=2.667):
    x_dot = s * (y - x)
    y_dot = r * x - y - x * z
    z_dot = x * y - b * z
    return x_dot, y_dot, z_dot


# krok (změna času)
dt = 0.01

# celkový počet vypočtených bodů na Lorenzově atraktoru
n = 10000

# prozatím prázdné pole připravené pro výpočet
x = np.zeros((n,))
y = np.zeros((n,))
z = np.zeros((n,))

# počáteční hodnoty
x[0], y[0], z[0] = (0.0, 1.0, 1.05)

# vlastní výpočet atraktoru
for i in range(n - 1):
    x_dot, y_dot, z_dot = lorenz(x[i], y[i], z[i])
    x[i + 1] = x[i] + x_dot * dt
    y[i + 1] = y[i] + y_dot * dt
    z[i + 1] = z[i] + z_dot * dt

fig = plt.figure()
ax = fig.gca(projection="3d")

# vykreslení grafu
ax.plot(x, y, z)

# zobrazení grafu
plt.show()
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//matplotlib_example29.py)

---

```python
# - vykreslení průběhu funkce sinc
# - při vykreslování se jednotlivé body spojí úsečkami
# - použití logaritmického měřítka v ose x

import numpy as np
import matplotlib.pyplot as plt

# hodnoty na x-ové ose
x = np.linspace(0.2, 2 * np.pi, 100)

# hodnoty na y-ové ose
y = np.sin(5 * x) / x
y2 = 1 / x
y3 = -y2

# vykreslit průběh funkce
plt.plot(x, y2, color="red", label="obalka sinc")
plt.plot(x, y3, color="red", label="obalka sinc")
plt.plot(x, y, color="blue", label="sinc(x)")

# logaritmické měřítko v ose x
plt.xscale("log")

# povolení zobrazení mřížky
plt.grid(True)

# popis os
plt.xlabel("x")
plt.ylabel("sinc(x)")

# přidání legendy
plt.legend(loc="lower right")

# zobrazení grafu
plt.show()
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//matplotlib_example30.py)

---

```python
# - vykreslení průběhu exponenciální funkce
# - při vykreslování se jednotlivé body spojí úsečkami

import numpy as np
import matplotlib.pyplot as plt

# hodnoty na x-ové ose
x = np.linspace(0.0, 10.0, 1000)

# hodnoty na y-ové ose
y = 2 ** x

# vykreslit průběh funkce
plt.plot(x, y, color="blue", label="exp(x)")

# povolení zobrazení mřížky
plt.grid(True)

# popis os
plt.xlabel("x")
plt.ylabel("exp(x)")

# přidání legendy
plt.legend(loc="upper left")

# zobrazení grafu
plt.show()
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//matplotlib_example31.py)

---

```python
# - vykreslení průběhu exponenciální funkce
# - při vykreslování se jednotlivé body spojí úsečkami
# - v ose y se použije logaritmické měřítko

import numpy as np
import matplotlib.pyplot as plt

# hodnoty na x-ové ose
x = np.linspace(0.0, 10.0, 1000)

# hodnoty na y-ové ose
y = 2 ** x

# vykreslit průběh funkce
plt.plot(x, y, color="blue", label="exp(x)")

# logaritmické měřítko v ose y
plt.yscale("log")

# povolení zobrazení mřížky
plt.grid(True)

# popis os
plt.xlabel("x")
plt.ylabel("exp(x)")

# přidání legendy
plt.legend(loc="upper left")

# zobrazení grafu
plt.show()
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//matplotlib_example32.py)

---

```python
# - vykreslení průběhu exponenciální funkce
# - při vykreslování se jednotlivé body spojí úsečkami
# - v ose x i y se použije logaritmické měřítko

import numpy as np
import matplotlib.pyplot as plt

# hodnoty na x-ové ose
x = np.linspace(0.0, 10.0, 1000)

# hodnoty na y-ové ose
y = 2 ** x

# vykreslit průběh funkce
plt.plot(x, y, color="blue", label="exp(x)")

# logaritmické měřítko v ose x
plt.xscale("log")

# logaritmické měřítko v ose y
plt.yscale("log")

# povolení zobrazení mřížky
plt.grid(True)

# popis os
plt.xlabel("x")
plt.ylabel("exp(x)")

# přidání legendy
plt.legend(loc="upper left")

# zobrazení grafu
plt.show()
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//matplotlib_example33.py)

---

## Trénink s učitelem a bez učitele

* S učitelem
    - klasifikace
    - regrese
* Bez učitele
    - clustering

---

## Datové sady pro první seznámení s modely

* Budeme je používat společně s knihovnou scikit-learn

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

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//iris_dataset.py)

---

### Datová sada Iris

Výstup

```
<class 'sklearn.utils._bunch.Bunch'>
----------------------------------------------------------------------------------------------------
['DESCR', 'data', 'data_module', 'feature_names', 'filename', 'frame', 'target', 'target_names']
```

---

### Datová sada Iris

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

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//iris_description.py)

---

### Datová sada Iris

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

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//iris_data.py)

---

### Datová sada California Housings

```python
import numpy as np

# import funkce pro nacteni datove sady, kterou pouzijeme
from sklearn.datasets import fetch_california_housing

# nacteni datove sady
housings = fetch_california_housing()

# precteni dat z datove sady
data = housings["data"]

# nadpis tabulky
print("Feature              Min         Max           Avg         Std         Var")

# zakladni statisticke informace o jednotlivych atributech
for i in range(len(housings["feature_names"])):
    column = data[:, i]
    feature = housings.feature_names[i]
    print(f"{feature:12}   {column.min():10.3f}   {column.max():10.3f}   {np.mean(column):10.3f}  {np.std(column):10.3f}  {np.var(column):11.3f}")
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//california_housings.py)

---

### Umělá data pro clustering

* Blobs atd.
    - nabízí přímo scikit-learn

---

## Modely pro klasifikaci

```python
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

# nacteni datove sady
iris = load_iris()

# X je matice (feature matrix)
X = iris.data

# y je vektor (response vector)
y = iris.target

# konstrukce klasifikatoru
# (s hyperparametrem)
classifier = KNeighborsClassifier(n_neighbors=1)

# trening modelu (se vsemi dostupnymi daty)
classifier.fit(X, y)

# parametry jedne rostliny
unknown = [[3, 5, 4, 2]]
print(unknown)

# predikce modelu pro jednu sadu dat
prediction = classifier.predict(unknown)
print(prediction)

# model predikuje hodnoty 0-3, ty si prevedeme na druhy rostlin
print(iris.target_names[prediction])

print()

# parametry vice rostlin
unknown = [[3, 5, 4, 2], [5, 4, 3, 2]]
print(unknown)

# predikce modelu pro vice sad dat
predictions = classifier.predict(unknown)
print(predictions)

# model predikuje hodnoty 0-3, ty si prevedeme na druhy rostlin
print(iris.target_names[predictions])
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//iris_basic_classifier.py)

---

```python
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# nacteni datove sady
iris = load_iris()

# X je matice (feature matrix)
X = iris.data

# y je vektor (response vector)
y = iris.target

# konstrukce klasifikatoru
# (s hyperparametrem)
classifier = LogisticRegression(max_iter=1000)
classifier.fit(X, y)

# trening modelu (se vsemi dostupnymi daty)
classifier.fit(X, y)

# parametry jedne rostliny
unknown = [[3, 5, 4, 2]]
print(unknown)

# predikce modelu pro jednu sadu dat
prediction = classifier.predict(unknown)
print(prediction)

# model predikuje hodnoty 0-3, ty si prevedeme na druhy rostlin
print(iris.target_names[prediction])

print()

# parametry vice rostlin
unknown = [[3, 5, 4, 2], [5, 4, 3, 2]]
print(unknown)

# predikce modelu pro vice sad dat
predictions = classifier.predict(unknown)
print(predictions)

# model predikuje hodnoty 0-3, ty si prevedeme na druhy rostlin
print(iris.target_names[predictions])
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//iris_different_model.py)

---

```python
import matplotlib.pyplot as plt

import numpy as np
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

# nacteni datove sady
iris = load_iris()

# X je matice (feature matrix)
X = iris.data

# y je vektor (response vector)
y = iris.target

feature_names = np.array(iris.feature_names)

print("n", "selectors", "features")

attributes = []
final_scores = []

for i in range(1, 2**len(feature_names)):
    indexes = []
    n = i
    for j in range(len(feature_names)):
        if n % 2 == 1:
            indexes.append(j)
        n //= 2
    selectors = np.array(indexes, dtype=int)
    knn_classifier = KNeighborsClassifier(n_neighbors=5)
    selected_features = X[:, selectors]
    scores = cross_val_score(knn_classifier, selected_features, y, cv=10, scoring='accuracy')
    attributes.append("\n".join(feature_names[selectors]))
    avg_score = scores.mean()
    final_scores.append(avg_score)
    print(i, selectors, feature_names[selectors], avg_score)

fig = plt.figure()
fig.set_figwidth(14)
fig.set_figheight(6)
fig.subplots_adjust(bottom=0.3)

plt.bar(attributes, final_scores)
plt.xticks(rotation=90)
plt.xlabel("Atributy")
plt.ylabel("Přesnost modelu")

# ulozeni grafu do souboru
plt.savefig("111.png")

# vykresleni grafu na obrazovku
plt.show()

```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//iris_features_selection_graphical.py)

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

---

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

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//linear_regression_gen_data.py)

---

### Použití modelu lineární regrese

* California housings

```python
import matplotlib.pyplot as plt

from sklearn import linear_model
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# nacteni datove sady
housings = fetch_california_housing()

# precteni dat z datove sady
# urcenych pro trenink, validaci atd.
data = housings["data"]

FIRST_DIM = 2
SECOND_DIM = 3

# rozdělení na trénovací a testovací data
x_train, x_test, y_train, y_test = train_test_split(data[:, FIRST_DIM], data[:, SECOND_DIM], test_size=0.6)

print("Array sizes:")
print(f"x_train: {len(x_train)}")
print(f"y_train: {len(y_train)}")
print(f"x_test:  {len(x_test)}")
print(f"y_test:  {len(y_test)}")

# konstrukce modelu
lr = linear_model.LinearRegression()

# trénink modelu
lr.fit(x_train.reshape(-1, 1), y_train)

# predikce modelu
y_pred = lr.predict(x_test.reshape(-1, 1))

# výpis vypočtených koeficientů modelu
print("Coefficients: \n", lr.coef_)
print("Intercept: \n", lr.intercept_)

# chyba predikce
print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))

# 1 = nejlepší predikce modelu
print("Coefficient of determination: %.2f" % r2_score(y_test, y_pred))

# vykreslení výsledku
plt.scatter(x_test, y_test, color="black", s=1)
plt.plot(x_test, y_pred, color="blue", linewidth=3)

# osy
plt.xlabel(housings.feature_names[FIRST_DIM])
plt.ylabel(housings.feature_names[SECOND_DIM])
plt.xticks(())
plt.yticks(())

# ulozeni diagramu do souboru
plt.savefig("82.png")

# zobrazeni diagramu
plt.show()
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//housings_linear_regression.py)

---

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

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//housings_prediction_1.py)

---

### Rozdělení přes train_test_split

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

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//housings_prediction_2.py)

---

### Konfigurace způsobu rozdělení

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

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//housings_prediction_3.py)

---

### Chyby modelu

```python
import numpy as np
import matplotlib.pyplot as plt

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

# jmena promennych/atributu
names = housings["feature_names"]

print("Ignored attribute\tMSE\tr2 score")

MEASUREMENTS = 200

for column_to_delete in range(len(names)):
    # X je matice, y je vektor
    X = np.delete(data, column_to_delete, axis=1) # smazat jeden vybrany sloupec
    y = targets

    column = names[column_to_delete]

    mses = []
    r2_scores = []

    for i in range(MEASUREMENTS):
        # rozdeleni dat na treninkovou a testovaci mnozinu
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.6)

        # konstrukce modelu
        lr = linear_model.LinearRegression()

        # trénink modelu
        lr.fit(X_train, y_train)

        # predikce modelu
        y_pred = lr.predict(X_test)

        # výpis vypočtených koeficientů modelu
        #print("Coefficients: \n", lr.coef_)
        #print("Intercept: \n", lr.intercept_)

        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        mses.append(mse)
        r2_scores.append(r2)

        print(f"{column:16}\t{mse:0.3f}\t{r2:0.3f}")

    plt.plot(range(MEASUREMENTS), mses, range(MEASUREMENTS), r2_scores)

    # titulek grafu
    plt.title(f"Mode prediction without column {column}")
    plt.legend(["MSE", "R2 score"])

    # osy
    plt.xticks()
    plt.yticks()

    # ulozeni diagramu do souboru
    plt.savefig(f"94_{column}.png")

    # zobrazeni diagramu
    plt.show()

```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//housings_prediction_errors_2.py)

---

### Výběr (filtrace) atributů

```python
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_california_housing

# nacteni datove sady
housings = fetch_california_housing()

# precteni dat z datove sady
# urcenych pro trenink, validaci atd.
data = housings["data"]

# vykresleni sady histogramu do mrizky
fig, axes = plt.subplots(nrows=4, ncols=2)
fig.set_figheight(15)
fig.set_figwidth(15)

# vykresleni jednotlivych histogramu do mrizky
for i in range(8):
    column = data[:, i]
    feature = housings.feature_names[i]
    ax = axes[i//2][i%2]
    # modifikace zpusobu vypoctu a zobrazeni histogrami
    ax.hist(column, bins=100, histtype="step")
    ax.set(xlabel=feature)


# zbavit se prazdneho mista okolo bunek mrizky
plt.tight_layout()

# ulozeni diagramu do souboru
plt.savefig("95.png")

# zobrazeni diagramu
plt.show()
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//housings_histograms.py)

---

## Křížová validace modelů

```python
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn import linear_model
from sklearn.model_selection import cross_val_score

# nacteni datove sady
housings = fetch_california_housing()

# X je matice (feature matrix)
X = housings.data

# y je vektor (response vector)
y = housings.target

feature_names = np.array(housings.feature_names)

print("n", "selectors", "features")

for i in range(1, 2**len(feature_names)):
    indexes = []
    n = i
    for j in range(len(feature_names)):
        if n % 2 == 1:
            indexes.append(j)
        n //= 2
    selectors = np.array(indexes, dtype=int)
    # konstrukce modelu
    lr = linear_model.LinearRegression()
    selected_features = X[:, selectors]
    scores = -cross_val_score(lr, selected_features, y, cv=10, scoring='neg_mean_squared_error')
    print(i, selectors, feature_names[selectors], scores.mean())

```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//housings_features_selection.py)

---

## Shluková analýza

```python
# budeme provádět vykreslování de facto standardní knihovnou Matplotlib
import matplotlib.pyplot as plt

import numpy as np
from sklearn.cluster import KMeans

# testovací data
n_samples = 10000

# počet oblastí, kam se budou data sdružovat
n_components = 6

samples = np.random.rand(n_samples, 2)

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
plt.savefig("k_means_5.png")

# vykreslení na obrazovku
plt.show()
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//clustering_random_points.py)

---

## Shluková analýza

```python
# Vykreslení bodů v 3D prostoru

import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# celkový počet vypočtených bodů
n_samples = 10000

# počet oblastí, kam se budou data sdružovat
n_components = 8

samples, _ = make_blobs(
    n_samples=n_samples, n_features=3, centers=n_components,
    cluster_std=1.80, random_state=0
)

# barvy použité pro obarvení bodů
colors = ["#4444cc", "#44bb44", "#cc4444", "#cccc44", "#44cccc", "#cc44cc", "#cccccc", "#000000"]

# příprava 3D grafu
fig = plt.figure(figsize=(6.4, 6.4))
ax = fig.add_subplot(projection="3d")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# clustering
kmeans = KMeans(n_clusters=n_components, random_state=0, n_init="auto").fit(samples)

# vykreslit centra nalezených oblastí
ax.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], kmeans.cluster_centers_[:, 2], c="red", s=50)

# vykreslení bodů s jejich přiřazením ke clusteru
for i, color in enumerate(colors):
    selector = kmeans.labels_ == i
    ax.scatter(samples[selector,0], samples[selector,1], samples[selector,2], marker=".", s=1)

# uložení grafu do souboru
plt.savefig("kmeans_spread_blobs_3D.png")

# uložení grafu do souboru
ax.view_init(90, -90, 0)
plt.savefig("kmeans_spread_blobs_view_1.png")

ax.view_init(0, -90, 0)
plt.savefig("kmeans_spread_blobs_view_2.png")

ax.view_init(0, 0, 0)
plt.savefig("kmeans_spread_blobs_view_3.png")
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//clustering_kmeans_spread_3d_blobs.py)

---

## Shluková analýza

```python
# budeme provádět vykreslování de facto standardní knihovnou Matplotlib
import matplotlib.pyplot as plt

from sklearn.cluster import SpectralClustering
from sklearn.datasets import make_blobs

# testovací data
n_samples = 10000

# počet oblastí, kam se budou data sdružovat
n_components = 6

samples, labels = make_blobs(
    n_samples=n_samples, centers=n_components, cluster_std=1.50, random_state=0
)

samples = samples[:, ::-1]

plt.figure(1)
colors = ["#4444cc", "#44bb44", "#cc4444", "#cccc44", "#44cccc", "#cc44cc"]

# clustering
spectral = SpectralClustering(n_clusters=n_components, eigen_solver="arpack", affinity="nearest_neighbors", random_state=0).fit(samples)

# vykreslení bodů s jejich přiřazením ke clusteru
for i, color in enumerate(colors):
    selector = spectral.labels_ == i
    plt.scatter(samples[selector, 0], samples[selector, 1], c=color, marker=".", s=1)

plt.title("Spectral clustering")

# uložení grafu do souboru
plt.savefig("blobs_spectral.png")

# vykreslení na obrazovku
plt.show()
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//clustering_blobs_spectral_clustering.py)

---

## Neuronové sítě

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# model zalozeny na neuronove siti
from sklearn.neural_network import MLPClassifier


# nacteni datove sady
iris = load_iris()

# konstrukce klasifikatoru
# (s hyperparametrem)
classifier = MLPClassifier(max_iter=5000)

# X je matice (feature matrix)
X = iris.data

# y je vektor (response vector)
y = iris.target

# rozdělení na trénovací a testovací data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# trening modelu
classifier.fit(X_train, y_train)

# očekávané výsledky
expexted_labels = y_test

# výsledky modelu (predikované výsledky)
predicted_labels = classifier.predict(X_test)

# jak je náš model úspěšný?
total = 0
same = 0

# porovnání predikce s očekáváním
for (expected, predicted) in zip(expexted_labels, predicted_labels):
    if expected==predicted:
        same+=1
    total+=1

print(f"total:    {total}")
print(f"same:     {same}")
print(f"accuracy: {100.0*same/total:4.1f}%")

print(f"Features: {classifier.n_features_in_}")
print(f"Layers:   {classifier.n_layers_}")
print(f"Outputs:  {classifier.n_outputs_}")
print("Weights:")

for layer, weights in enumerate(classifier.coefs_):
    print("\t", layer, weights.shape)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//mlp_classifier_01.py)

---

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score

# model zalozeny na neuronove siti
from sklearn.neural_network import MLPClassifier


# nacteni datove sady
iris = load_iris()

# konstrukce klasifikatoru
# (s hyperparametrem)
classifier = MLPClassifier(max_iter=5000)

# X je matice (feature matrix)
X = iris.data

# y je vektor (response vector)
y = iris.target

# rozdělení na trénovací a testovací data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# trening modelu
classifier.fit(X_train, y_train)


# výsledky modelu (predikované výsledky)
y_pred = classifier.predict(X_test)

# vypoctena presnost modelu
print(accuracy_score(y_test, y_pred))

print(f"Features: {classifier.n_features_in_}")
print(f"Layers:   {classifier.n_layers_}")
print(f"Outputs:  {classifier.n_outputs_}")
print("Weights:")

for layer, weights in enumerate(classifier.coefs_):
    print("\t", layer, weights.shape)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//mlp_classifier_02.py)

---

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score

# model zalozeny na neuronove siti
from sklearn.neural_network import MLPClassifier


# nacteni datove sady
iris = load_iris()

# konstrukce klasifikatoru
# (s hyperparametrem)
classifier = MLPClassifier(max_iter=5000, hidden_layer_sizes = (10, 10, 10))

# X je matice (feature matrix)
X = iris.data

# y je vektor (response vector)
y = iris.target

# rozdělení na trénovací a testovací data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# trening modelu
classifier.fit(X_train, y_train)


# výsledky modelu (predikované výsledky)
y_pred = classifier.predict(X_test)

# vypoctena presnost modelu
print(accuracy_score(y_test, y_pred))

print(f"Features: {classifier.n_features_in_}")
print(f"Layers:   {classifier.n_layers_}")
print(f"Outputs:  {classifier.n_outputs_}")
print("Weights:")

for layer, weights in enumerate(classifier.coefs_):
    print("\t", layer, weights.shape)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//mlp_classifier_03.py)

---

```python

import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score

# model zalozeny na neuronove siti
from sklearn.neural_network import MLPClassifier


# nacteni datove sady
iris = load_iris()

# X je matice (feature matrix)
X = iris.data

# y je vektor (response vector)
y = iris.target

avg_scores = []

r = range(1, 20)

# hledani optimalniho poctu neuronu ve vrstvach
for neurons in r:
    # konstrukce klasifikatoru
    # (s hyperparametrem)
    classifier = MLPClassifier(max_iter=5000, hidden_layer_sizes = (neurons, neurons, neurons))

    # vypocet skore
    scores = cross_val_score(classifier, X, y, cv=10, scoring='accuracy')

    avg_score = scores.mean()

    # vypsani prumerneho skore do tabulky
    print(neurons, avg_score)

    avg_scores.append(avg_score)

plt.plot(r, avg_scores)
plt.xlabel("Změna počtu neuronů ve třech vrstvách")
plt.ylabel("Přesnost modelu")

# ulozeni grafu do souboru
plt.savefig("139.png")

# vykresleni grafu na obrazovku
plt.show()

```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//mlp_classifier_04.py)

---

```python

import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score

# model zalozeny na neuronove siti
from sklearn.neural_network import MLPClassifier


# nacteni datove sady
iris = load_iris()

# X je matice (feature matrix)
X = iris.data

# y je vektor (response vector)
y = iris.target

avg_scores = []

r = range(1, 20)

# hledani optimalniho poctu neuronu ve vrstvach
for neurons in r:
    # konstrukce klasifikatoru
    # (s hyperparametrem)
    classifier = MLPClassifier(max_iter=5000, hidden_layer_sizes = (neurons, neurons, neurons, neurons, neurons))

    # vypocet skore
    scores = cross_val_score(classifier, X, y, cv=10, scoring='accuracy')

    avg_score = scores.mean()

    # vypsani prumerneho skore do tabulky
    print(neurons, avg_score)

    avg_scores.append(avg_score)

plt.plot(r, avg_scores)
plt.xlabel("Změna počtu neuronů v pěti vrstvách")
plt.ylabel("Přesnost modelu")

# ulozeni grafu do souboru
plt.savefig("140.png")

# vykresleni grafu na obrazovku
plt.show()

```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//mlp_classifier_05.py)

---

```python

import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score

# model zalozeny na neuronove siti
from sklearn.neural_network import MLPClassifier


# nacteni datove sady
iris = load_iris()

# X je matice (feature matrix)
X = iris.data

# y je vektor (response vector)
y = iris.target

avg_scores = []

NEURONS = 5
r = range(1, 40)

# hledani optimalniho poctu neuronu ve vrstvach
for layers in r:
    # konstrukce klasifikatoru
    # (s hyperparametrem)
    layer_sizes = (NEURONS, ) * layers
    classifier = MLPClassifier(max_iter=5000, hidden_layer_sizes = layer_sizes)

    # vypocet skore
    scores = cross_val_score(classifier, X, y, cv=10, scoring='accuracy')

    avg_score = scores.mean()

    # vypsani prumerneho skore do tabulky
    print(layers, avg_score)

    avg_scores.append(avg_score)

plt.plot(r, avg_scores)
plt.xlabel("Změna počtu vrstev")
plt.ylabel("Přesnost modelu")

# ulozeni grafu do souboru
plt.savefig("141.png")

# vykresleni grafu na obrazovku
plt.show()

```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//mlp_classifier_06.py)

---

```python
# model zalozeny na neuronove siti
from sklearn.neural_network import MLPRegressor

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
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

# konstrukce modelu
nn = MLPRegressor(max_iter=5000)

# trénink modelu
nn.fit(X_train, y_train)

# predikce modelu
y_pred = nn.predict(X_test)

# chyba predikce
print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))

# 1 = nejlepší predikce modelu
print("Coefficient of determination: %.2f" % r2_score(y_test, y_pred))

print(f"Features: {nn.n_features_in_}")
print(f"Layers:   {nn.n_layers_}")
print(f"Outputs:  {nn.n_outputs_}")
print("Weights:")

for layer, weights in enumerate(nn.coefs_):
    print("\t", layer, weights.shape)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//mlp_regression_1.py)

---

```python
# model zalozeny na neuronove siti
from sklearn.neural_network import MLPRegressor

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
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

neurons = 1000

# konstrukce modelu
nn = MLPRegressor(max_iter=5000, hidden_layer_sizes = (neurons, neurons, ))

# trénink modelu
nn.fit(X_train, y_train)

# predikce modelu
y_pred = nn.predict(X_test)

# chyba predikce
print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))

# 1 = nejlepší predikce modelu
print("Coefficient of determination: %.2f" % r2_score(y_test, y_pred))

print(f"Features: {nn.n_features_in_}")
print(f"Layers:   {nn.n_layers_}")
print(f"Outputs:  {nn.n_outputs_}")
print("Weights:")

for layer, weights in enumerate(nn.coefs_):
    print("\t", layer, weights.shape)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//mlp_regression_2.py)

---

```python

import matplotlib.pyplot as plt

# model zalozeny na neuronove siti
from sklearn.neural_network import MLPRegressor

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import cross_val_score

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

r = range(1, 12)
avg_scores = []

# hledani optimalniho poctu neuronu ve vrstvach
for i in r:
    # konstrukce modelu
    neurons = 2**i
    nn = MLPRegressor(max_iter=5000, hidden_layer_sizes = (neurons, ))

    scores = cross_val_score(nn, X, y, cv=10, scoring='r2')

    # vypsani prumerneho skore do tabulky
    avg_score = scores.mean()
    print(neurons, avg_score)

    avg_scores.append(avg_score)

plt.plot(r, avg_scores)
plt.xlabel("Změna počtu neuronů v jedné vrstvě")
plt.ylabel("R2")

# ulozeni grafu do souboru
plt.savefig("144.png")

# vykresleni grafu na obrazovku
#plt.show()

```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//mlp_regression_3.py)

---

```python

import matplotlib.pyplot as plt

# model zalozeny na neuronove siti
from sklearn.neural_network import MLPRegressor

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import cross_val_score

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

r = range(1, 12)
avg_scores = []

# hledani optimalniho poctu neuronu ve vrstvach
for i in r:
    # konstrukce modelu
    neurons = 2**i
    nn = MLPRegressor(max_iter=5000, hidden_layer_sizes = (neurons, neurons, neurons))

    scores = cross_val_score(nn, X, y, cv=10, scoring='r2')

    # vypsani prumerneho skore do tabulky
    avg_score = scores.mean()
    print(neurons, avg_score)

    avg_scores.append(avg_score)

plt.plot(r, avg_scores)
plt.xlabel("Změna počtu neuronů ve třech vrstvách")
plt.ylabel("R2")

# ulozeni grafu do souboru
plt.savefig("145.png")

# vykresleni grafu na obrazovku
#plt.show()

```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//mlp_regression_4.py)

---

```python

import matplotlib.pyplot as plt

# model zalozeny na neuronove siti
from sklearn.neural_network import MLPRegressor

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import cross_val_score

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

r = range(1, 12)
avg_scores = []

# hledani optimalniho poctu neuronu ve vrstvach
for i in r:
    # konstrukce modelu
    neurons = 2**i
    nn = MLPRegressor(max_iter=5000, hidden_layer_sizes = (neurons, neurons, neurons, neurons, neurons))

    scores = cross_val_score(nn, X, y, cv=10, scoring='r2')

    # vypsani prumerneho skore do tabulky
    avg_score = scores.mean()
    print(neurons, avg_score)

    avg_scores.append(avg_score)

plt.plot(r, avg_scores)
plt.xlabel("Změna počtu neuronů v pěti vrstvách")
plt.ylabel("R2")

# ulozeni grafu do souboru
plt.savefig("146.png")

# vykresleni grafu na obrazovku
#plt.show()

```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//mlp_regression_5.py)

