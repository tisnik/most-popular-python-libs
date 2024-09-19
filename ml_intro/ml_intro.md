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
* Bayesovské site
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

![akt1.png](images/akt1.png)

---

### Aktivační funkce

![akt2.png](images/akt2.png)

---

### Feed-forward síť

* Vstupní vrstva
* Skryté vrstvy
* Výstupní vrstva

---

### Feed-forward síť

![ff.png](images/ff.png)

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
- Volitelný počet dimenzí
    - vektory
    - matice
    - pole s větším počtem dimenzí
- Volitelný typ prvků
- Volitelné uspořádání prvků
    - podle zvyklostí jazyka Fortran
    - podle zvyklostí jazyka C

### Tvar (shape) n-dimenzionálního pole
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

### Konstruktor numpy.array
- parametry
`array(object, dtype=None, copy=True, order=None, subok=False, ndmin=0)`

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

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//iris_description.py)

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

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//linear_regression_gen_data.py)

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

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/ml_intro/examples//housings_prediction_1.py)

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

