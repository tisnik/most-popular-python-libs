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

@ numpy_01_array.py

---

@ numpy_02_array_range.py

---

@ numpy_03_array_dtype.py

---

@ numpy_04_array_order_c.py

---

@ numpy_05_array_order_f.py

---

@ numpy_06_2D_array.py

---

@ numpy_07_zeros_1D_array.py

---

@ numpy_08_zeros_1D_array.py

---

@ numpy_09_zeros_2D_array.py

---

@ numpy_10_zeros_3D_array.py

---

@ numpy_11_zeros_specify_type.py

---

@ numpy_12_zeros_complex_numbers.py

---

@ numpy_13_ones_1D_array.py

---

@ numpy_14_ones_2D_array.py

---

@ numpy_15_ones_specify_type.py

---

@ numpy_16_ones_3D_array.py

---

@ numpy_17_ones_complex_numbers.py

---

@ numpy_18_eye_1D_array.py

---

@ numpy_19_eye_2D_array.py

---

@ numpy_20_eye_2D_array.py

---

@ numpy_21_eye_2D_array_dtype.py

---

@ numpy_22_eye_2D_array_k_positive.py

---

@ numpy_23_eye_2D_array_k_negative.py

---

@ numpy_24_eye_2D_array_k_10.py

---

@ numpy_25_full_1D_array.py

---

@ numpy_26_full_2D_array.py

---

@ numpy_27_full_3D_array.py

---

@ numpy_28_full_dtype.py

---

@ numpy_29_full_inf.py

---

@ numpy_30_full_inf_complex.py

---

@ numpy_31_arange_10.py

---

@ numpy_32_arange_10_20.py

---

@ numpy_33_arange_positive_step.py

---

@ numpy_34_arange_negative_step.py

---

@ numpy_35_arange_floats.py

---

@ numpy_36_arange_complex.py

---

@ numpy_37_arange_complex.py

---

@ numpy_38_linspace_default_number_of_items.py

---

@ numpy_39_linspace_specific_number_of_items.py

---

@ numpy_40_linspace_specific_number_of_items.py

---

@ numpy_41_linspace_decrementing.py

---

@ numpy_42_linspace_complex_real_part.py

---

@ numpy_43_linspace_complex_imaginary_part.py

---

@ numpy_44_linspace_complex_both_parts.py

---

@ numpy_45_geomspace_default_number_of_items.py

---

@ numpy_46_geomspace_specific_number_of_items.py

---

@ numpy_47_geomspace_specific_number_of_items.py

---

@ numpy_48_geomspace_dtype.py

---

@ numpy_49_logspace_default_number_of_items.py

---

@ numpy_50_logspace_specific_number_of_items.py

---

@ numpy_51_logspace_specific_number_of_items.py

---

@ numpy_52_logspace_dtype.py

---

@ numpy_53_retype_int64_array.py

---

@ numpy_54_retype_int64_array_wrong_input.py

---

@ numpy_55_retype_float16_array.py

---

@ numpy_56_retype_array_to_array.py

---

@ numpy_57_astype1.py

---

@ numpy_58_matrix_string.py

---

@ numpy_59_matrix_string_2D_array.py

---

@ numpy_60_matrix_string_2D_array_error.py

---

@ numpy_61_info_about_1D_array.py

---

@ numpy_62_info_about_2D_array.py

---

@ numpy_63_info_about_3D_array.py

---

@ numpy_64_print_big_array.py

---

@ numpy_65_reshape1.py

---

@ numpy_66_reshape2.py

---

@ numpy_67_reshape3.py

---

@ numpy_68_reshape4.py

---

@ numpy_69_selectors_1D_array.py

---

@ numpy_70_selectors_2D_array.py

---

@ numpy_71_select_by_other_array.py

---

@ numpy_72_select_by_other_array_negative_indexes.py

---

@ numpy_73_select_rows.py

---

@ numpy_74_select_from_2D_array.py

---

@ numpy_75_slicing.py

---

@ numpy_76_slicing.py

---

@ numpy_77_empty_slice.py

---

@ numpy_78_slicing_negative_indexes.py

---

@ numpy_79_slicing_2d_arrays.py

---

@ numpy_80_slicing_specify_steps.py

---

@ numpy_81_slicing_matrix_steps.py

---

@ numpy_82_add_item_by_scalar.py

---

@ numpy_83_mul_item_by_scalar.py

---

@ numpy_84_div_item_by_scalar.py

---

@ numpy_85_add_item_by_item.py

---

@ numpy_86_operator_pluseq.py

---

@ numpy_87_not_matrix_multiplication.py

---

@ numpy_88_matrix_multiplication.py

---

@ numpy_89_check_matrix_multiplication.py

---

## Matplotlib

![Matplotlib](images/matplotlib.png)

---

@ matplotlib_example01.py

---

@ matplotlib_example01.py

---

@ matplotlib_example02.py

---

@ matplotlib_example03.py

---

@ matplotlib_example04.py

---

@ matplotlib_example05.py

---

@ matplotlib_example06.py

---

@ matplotlib_example07.py

---

@ matplotlib_example08.py

---

@ matplotlib_example09.py

---

@ matplotlib_example10.py

---

@ matplotlib_example11.py

---

@ matplotlib_example12.py

---

@ matplotlib_example13.py

---

@ matplotlib_example14.py

---

@ matplotlib_example15.py

---

@ matplotlib_example16.py

---

@ matplotlib_example17.py

---

@ matplotlib_example18.py

---

@ matplotlib_example19.py

---

@ matplotlib_example20.py

---

@ matplotlib_example21.py

---

@ matplotlib_example22.py

---

@ matplotlib_example23.py

---

@ matplotlib_example24.py

---

@ matplotlib_example25.py

---

@ matplotlib_example26.py

---

@ matplotlib_example27.py

---

@ matplotlib_example28.py

---

@ matplotlib_example29.py

---

@ matplotlib_example30.py

---

@ matplotlib_example31.py

---

@ matplotlib_example32.py

---

@ matplotlib_example33.py

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

@ iris_dataset.py

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

@ iris_description.py

---

### Datová sada Iris

@ iris_data.py

---

### Datová sada California Housings

@ california_housings.py

---

### Umělá data pro clustering

* Blobs atd.
    - nabízí přímo scikit-learn

---

## Modely pro klasifikaci

@ iris_basic_classifier.py

---

@ iris_different_model.py

---

@ iris_features_selection_graphical.py

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

@ linear_regression_gen_data.py

---

### Použití modelu lineární regrese

* California housings

@ housings_linear_regression.py

---

### Trénink modelu se všemi daty

* Což obecně není vhodné

@ housings_prediction_1.py

---

### Rozdělení přes train_test_split

@ housings_prediction_2.py

---

### Konfigurace způsobu rozdělení

@ housings_prediction_3.py

---

### Chyby modelu

@ housings_prediction_errors_2.py

---

### Výběr (filtrace) atributů

@ housings_histograms.py

---

## Křížová validace modelů

@ housings_features_selection.py

---

## Shluková analýza

@ clustering_random_points.py

---

## Shluková analýza

@ clustering_kmeans_spread_3d_blobs.py

---

## Shluková analýza

@ clustering_blobs_spectral_clustering.py

---

## Neuronové sítě

@ mlp_classifier_01.py

---

@ mlp_classifier_02.py

---

@ mlp_classifier_03.py

---

@ mlp_classifier_04.py

---

@ mlp_classifier_05.py

---

@ mlp_classifier_06.py

---

@ mlp_regression_1.py

---

@ mlp_regression_2.py

---

@ mlp_regression_3.py

---

@ mlp_regression_4.py

---

@ mlp_regression_5.py

