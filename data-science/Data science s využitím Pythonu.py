#!/usr/bin/env python
# coding: utf-8

# # Data science s využitím Pythonu
# 
# ---
# 
# * Pavel Tišnovský
# * kurzy.python@centrum.cz
# 
# ![Python](images/python.png)
# 
# ---
# 
# ## Obsah
# 
# * Nástroje pro datovou analýzu
# * Transformace dat na informace
# * Jupyter Notebook
# * Knihovny používané v této oblasti: NumPy, Pandas, Polars, Seaborn, scikit-learn, Dask
# * Vizualizace dat: Matplotlib
# * Zpracování obrazů a přirozeného jazyka v Pythonu
# * Strojové učení
# 
# ---
# 
# ## Python
# 
# * Dnes jeden z nejpopulárnějších programovacích jazyků
#     - viz například TIOBE programming community index
#     - <https://www.tiobe.com/tiobe-index/>
#     - popř. statistika dostupná na OpenHubu
#     - <https://www.openhub.net/languages/compare>
# * Dostupnost na většině platforem
#     - na některých MCU jako MicroPython
# 
# ---
# 
# ## Typické použití Pythonu
# 
# * Nástroje a utility ovládané z příkazového řádku
# * Aplikace s grafickým uživatelským rozhraním
# * Client-server
#     - serverová část (Flask, Django, CherryPy, ...)
#     - klient (Brython, spíše technologické demo)
# * Numerické výpočty, symbolické výpočty
#     - NumPy
#     - SciPy
#     - Matplotlib
# 
# ---
# 
# ## Typické použití Pythonu
# 
# * Moderní způsoby využití Pythonu
#     - AI
#     - Machine Learning (Deep Learning)
#     - PyTorch
#     - Big data
#     - aplikace v prohlížeči
# * Tzv. „glue“ jazyk
# * Vestavitelný interpret Pythonu
# 
# ---
# 
# ## Nástroje pro datovou analýzu
# 
# * Data mining
# * Data procesing a modelování
#     - klasifikace
#     - predikce
#     - výběr modelu
#     - redukce počtu dimenzí
#     - pre-processing
#     - modelování
# * Vizualizace
# 
# ---
# 
# ## Jupyter Notebook
# 
# * Typický centrální prvek, v němž se odehrává vývoj
# * Lze sdílet
# * Podporuje různá jádra (kernels)
# * Podpora vizualizace přímo na ploše notebooku
# 
# ---
# 
# ## Data mining
# 
# * Scrapy
# * BeautifulSoup
# 
# ---
# 
# ## Data processing a modelování
# 
# * NumPy
# * SciPy
# * Xarray
# * Pandas
# * Polars
# * SciKit-learn
# 
# ---
# 
# ## Vizualizace dat
# 
# * Matplotlib
# * Seaborn
# * Bokeh
# * Plotly
# * pydot
# * plotnine
# 
# ---
# 
# ## Strojové učení
# 
# * PyCaret
# * H2O
# * TPOT
# * Auto-sklearn
# * Keras
# * SciKit-Learn
# * PyTorch
# * TensorFlow
# 
# ---
# 
# ## Zpracování přirozeného jazyka
# 
# * NLTK
# * spaCy
# 
# ---
# 
# ## HPC
# 
# * Dask
# 
# ---
# 
# ## NumPy
# 
# ![numpy_arrays.png](images/numpy_logo.png)
# 
# ---
# 
# ### Knihovna NumPy
# 
# - Výslovnosti
#     - [nəmpᴧɪ]
#     - [nəmpi]
# - Historie
#     - matrix package
#     - Numeric
#     - NumPy
# - Podpora pro n-dimenzionální pole
#     - + nové funkce
#     - + nové (přetížené) operátory
# - Kooperace s dalšími knihovnami a frameworky
#     - SciPy
#     - Matplotlib
#     - OpenCV
# 
# ---
# 
# ### NumPy
# 
# * n-dimenzionální pole jako základní datový typ
#     - ideově vychází z APL
#     - nové funkce
#     - nové (přetížené) operátory
# * mnoho typů konstruktorů
# * broadcsting
# * (re)shaping
#     - změna tvaru pole (počet dimenzí, tvar)
# 
# ---
# ### Skalární datové typy
# - <https://docs.scipy.org/doc/numpy/user/basics.types.html>
# ```
# ╔════════════╤═══════════════════════════╤═══════════════════════════════╗
# ║ Formát     │ Popis                     │ Rozsah                        ║
# ╟────────────┼───────────────────────────┼───────────────────────────────╢
# ║ bool       │ uloženo po bajtech        │  True/False                   ║
# ╟────────────┼───────────────────────────┼───────────────────────────────╢
# ║ int8       │ celočíselný se znaménkem  │ -128..127                     ║
# ║ int16      │ celočíselný se znaménkem  │ -32768..32767                 ║
# ║ int32      │ celočíselný se znaménkem  │ -2147483648..2147483647       ║
# ║ int64      │ celočíselný se znaménkem  │ -9223372036854775808..        ║
# ║            │                           │  9223372036854775807          ║
# ╟────────────┼───────────────────────────┼───────────────────────────────╢
# ║ uint8      │ celočíselný bez znaménka  │  0..255                       ║
# ║ uint16     │ celočíselný bez znaménka  │  0..65535                     ║
# ║ uint32     │ celočíselný bez znaménka  │  0..4294967295                ║
# ║ uint64     │ celočíselný bez znaménka  │  0..18446744073709551615      ║
# ╟────────────┼───────────────────────────┼───────────────────────────────╢
# ║ float16    │ plovoucí řádová čárka     │  poloviční přesnost (half)    ║
# ║ float32    │ plovoucí řádová čárka     │  jednoduchá přesnost (single) ║
# ║ float64    │ plovoucí řádová čárka     │  dvojitá přesnost (double)    ║
# ╟────────────┼───────────────────────────┼───────────────────────────────╢
# ║ complex64  │ komplexní číslo (dvojice) │  2×float32                    ║
# ║ complex128 │ komplexní číslo (dvojice) │  2×float64                    ║
# ╚════════════╧═══════════════════════════╧═══════════════════════════════╝
# ```
# 
# ### Kódy skalárních datových typů
# - jednoznakové kódy je možné použít namísto jména typu
# ```
# ╔════════════╤══════╗
# ║  Formát    │ Kód  ║
# ╟────────────┼──────╢
# ║ formát     │ kód  ║
# ║ bool       │ '?'  ║
# ║ int8       │ 'b'  ║
# ║ int16      │ 'h'  ║
# ║ int32      │ 'i'  ║
# ║ int64      │ 'l'  ║
# ║ uint8      │ 'B'  ║
# ║ uint16     │ 'H'  ║
# ║ uint32     │ 'I'  ║
# ║ uint64     │ 'L'  ║
# ║ float16    │ 'e'  ║
# ║ float32    │ 'f'  ║
# ║ float64    │ 'd'  ║
# ║ complex64  │ 'F'  ║
# ║ complex128 │ 'D'  ║
# ╚════════════╧══════╝
# ```
# 
# ### Datový typ single
# ```
# Celkový počet bitů (bytů):   32 (4)
# Bitů pro znaménko:            1
# Bitů pro exponent:            8
# Bitů pro mantisu:            23
# ```
# 
# ### Datový typ double
# ```
# Celkový počet bitů (bytů):   64 (8)
# Bitů pro znaménko:            1
# Bitů pro exponent:           11
# Bitů pro mantisu:            52
# ```
# 
# ### Datový typ float16
# ```
# Celkový počet bitů (bytů):   16 (2)
# Bitů pro znaménko:            1
# Bitů pro exponent:            5
# Bitů pro mantisu:            10
# BIAS (offset exponentu):     15
# Přesnost:                    5-6 číslic
# Maximální hodnota:           65504
# Minimální hodnota:          -65504
# Nejmenší kladná nenulová hodnota:      5,960×10⁻⁸
# Nejmenší kladná normalizovaná hodnota: 6,104×10⁻⁵
# ```
# 
# ### N-dimenzionální pole
# ![numpy_arrays.png](images/numpy_arrays.png)
# 
# ### Datová struktura ndarray
# - Představuje obecné n-dimenzionální pole
# - Interní způsob uložení dat zcela odlišný od Pythonovských seznamů či n-tic
#     - „pohled“ na kontinuální blok hodnot
# - Homogenní datová struktura
#     - menší flexibilita
#     - menší paměťové nároky
#     - vyšší výpočetní rychlost díky použití nativního kódu
#     - obecně lepší využití cache a rychlejší přístup k prvkům
# - Základní strukturovaný datový typ knihovny NumPy
# - Volitelný počet dimenzí
#     - vektory
#     - matice
#     - pole s větším počtem dimenzí
# - Volitelný typ prvků
# - Volitelné uspořádání prvků
#     - podle zvyklostí jazyka Fortran
#     - podle zvyklostí jazyka C
# 
# ### Tvar (shape) n-dimenzionálního pole
# - Popisuje organizaci a uspořádání prvků v poli
#     - n-tice obsahující rozměry pole v jednotlivých dimenzích
# - Příklady tvarů
#     - `(10,)` - vektor s deseti prvky
#     - `(2, 3)` - dvourozměrná matice se dvěma řádky a třemi sloupci
#     - `(2, 3, 4)` - trojrozměrné pole
# - Tvar je možné zjistit
#     - atribut „shape“
#     - funkce `numpy.shape()`
# - Tvar je možné změnit
#     - funkce `numpy.reshape()`
# 
# ### Konstrukce n-dimenzionálních polí
# - Několik typů konstruktorů
#     - `numpy.array()`
#     - `numpy.zeros()`
#     - `numpy.ones()`
#     - `numpy.full()`
#     - `numpy.eye()`
#     - `numpy.arange()`
#     - `numpy.linspace()`
#     - `numpy.geomspace()`
#     - `numpy.logspace()`
# - Konverzní funkce
#     - `numpy.matrix()`
# 
# ### Konstruktor numpy.array
# - parametry
# `array(object, dtype=None, copy=True, order=None, subok=False, ndmin=0)`
# 
# ### Order
# ```
# ╔═════════╤════════════════════════════════════╗
# ║ Hodnota │ Význam                             ║
# ╟─────────┼────────────────────────────────────╢
# ║ 'C'     │ prvky jsou interně uspořádány jako ║
# ║         │ v programovacím jazyku C           ║
# ║         │                                    ║
# ║ 'F'     │ prvky jsou interně uspořádány jako ║
# ║         │ v programovacím jazyku Fortran     ║
# ║         │                                    ║
# ║ 'A'     │ ponecháme na implementaci, který   ║
# ║         │ způsob uspořádání interně zvolit   ║
# ╚═════════╧════════════════════════════════════╝
# ```
# 
# ### Order - rozdíl v uspořádání
# - 2D matice tak, jak ji vidí uživatel (logická struktura)
# ```
# | 1 2 3 |
# | 4 5 6 |
# | 7 8 9 |
# ```
# 
# - Uložení v operační paměti
# ```
# 1 2 3 4 5 6 7 8 9 - 'C'
# 1 4 7 2 5 8 3 6 9 - 'F'
# ```
# 
# 
# ---
# 
# ## Xarray
# 
# ![xarray](images/xarray1.png)
# 
# ---
# 
# ### Xarray
# 
# * n-dimensionální pole s metadaty
#     - jméno
#     - dimenze (osy)
#     - koordináty na osách
#     - uživatelské atributy
# 
# ---
# 
# ### Přednosti použití Xarray
# 
# * intuitivní práce s poli
# * založeno na metadatech, ne na kódu
# * stručnost
# * dnes de facto standardní řešení
# * méně chyb při zpracování dat
#     - operace nad nekorektními osami
# * broadcasting založený na jménu osy
# * velmi jednoduchá operace typu `groupby`
# 
# ---
# 
# ### Množina polí
# 
# ![xarray](images/xarray2.png)
# 
# ---
# 
# ## Pandas
# 
# ![pandas](images/pandas.png)
# 
# ---
# 
# ## Pandas
# 
# * Načtení dat z různých datových zdrojů do datových rámců
#     - CSV
#     - TSV
#     - databáze
#     - tabulkové procesory
# * Programová konstrukce datových rámců
# * Prohlížení obsahu datových rámců
# 
# ---
# 
# ## Pandas
# 
# * Iterace nad daty, řazení a další podobné operace
# * Spojování, seskupování a změna tvaru dat
# * Práce s takzvanými sériemi
#     - většinou získanými z datových rámců
# * Vykreslování grafů z údajů získaných z datových rámců
# 
# ---
# 
# ### Práce s datovými rámci
# 
# * Knihovna Pandas podporuje využití různých datových zdrojů, především pak:
#   - Souborů CSV (Comma-Separated Values)
#   - Souborů TSV (Tab-Separated Values)
#   - Textových souborů s volitelným oddělovačem a formátem sloupců
#   - Tabulek z tabulkových procesorů (xls, xlsx, xlsm, xlsb, odf, ods, odt)
#   - Souborů JSON se strukturovanými daty
#   - Načítání z relačních databází s využitím SQL
#   - Načítání z Parquet souborů
# 
# ---
# 
# ### Zpracování souborů s nestandardním formátem
# 
# * https://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt
# * Evidentně se jedná o tabulková a velmi dobře strukturovaná data, která by bylo vhodné umět automaticky zpracovat
# 
# ---
# 
# ### Zpracování souborů s nestandardním formátem
# 
# ```
# 13.11.2023 #219
# země|měna|množství|kód|kurz
# Austrálie|dolar|1|AUD|14,683
# Brazílie|real|1|BRL|4,672
# Bulharsko|lev|1|BGN|12,573
# Čína|žen-min-pi|1|CNY|3,162
# Dánsko|koruna|1|DKK|3,296
# EMU|euro|1|EUR|24,590
# Filipíny|peso|100|PHP|41,117
# Hongkong|dolar|1|HKD|2,952
# Indie|rupie|100|INR|27,682
# Indonesie|rupie|1000|IDR|1,468
# Island|koruna|100|ISK|16,040
# Izrael|nový šekel|1|ILS|5,964
# Japonsko|jen|100|JPY|15,186
# Jižní Afrika|rand|1|ZAR|1,228
# Kanada|dolar|1|CAD|16,664
# Korejská republika|won|100|KRW|1,740
# Maďarsko|forint|100|HUF|6,514
# Malajsie|ringgit|1|MYR|4,896
# Mexiko|peso|1|MXN|1,303
# MMF|ZPČ|1|XDR|30,319
# Norsko|koruna|1|NOK|2,069
# Nový Zéland|dolar|1|NZD|13,550
# Polsko|zlotý|1|PLN|5,552
# Rumunsko|leu|1|RON|4,947
# Singapur|dolar|1|SGD|16,936
# Švédsko|koruna|1|SEK|2,118
# Švýcarsko|frank|1|CHF|25,471
# Thajsko|baht|100|THB|64,040
# Turecko|lira|1|TRY|0,806
# USA|dolar|1|USD|23,050
# Velká Británie|libra|1|GBP|28,230
# ```
# 
# ---
# 
# ## Polars
# 
# ![polars](images/polars.png)
# 
# ---
# 
# ### Polars
# 
# * Alternativa ke knihovně Pandas
# * Podporuje multithreading
# * SIMD operace (ne vždy)
# * Optimalizace dotazů
# * Líné vyhodnocování
# 
# ---
# 
# ### Polars
# 
# * Datové rámce rozsáhlejší než dostupná RAM
# * Naprogramováno v Rustu
# * Vazby s dalšími knihovnami
#     - pyarrow, NumPy, Pandas etc.
# * Rozhraní pro Python a NodeJS
# 
# ---
# 
# ### Datové řady a datové rámce
# 
# * Podobné těm v Pandas
#     - funkce a metody se stejnými jmény
#     - ovšem ne zcela kompatibilní
# 
# ---
# 
# ### Načtení z SQL
# 
# ```python
# import polars
# 
# connection_string = "postgresql://postgres:postgres@localhost:5432/testdb"
# 
# query = """
#     SELECT org_id, cluster_id, rule_fqdn
#       FROM rule_hit
#      ORDER by org_id, cluster_id
# """
# 
# df = polars.read_sql(query, connection_string)
# 
# print(df)
# print()
# ```
# 
# ---
# 
# ### Klíč k úspěchu: být líný!
# 
# * FP programování
# * Architektura založená na Kafce atd.
# * Dask atd.
# * Líné datové rámce v Polars
# 
# ---
# 
# ### Líné datové rámce
# 
# ```python
# import polars
# 
# df = polars.read_csv("hall_of_fame.csv").lazy()
# 
# df2 = df.groupby("Winner", maintain_order=True).agg([polars.col("Year").len()]). \
#       sort("Year"). \
#       reverse(). \
#       head(5)
# 
# print(df2.describe_plan())
# print(df2.describe_optimized_plan())
# ```
# 
# ---
# 
# ## Matplotlib
# 
# ![Matplotlib](images/matplotlib.png)
# 
# ---
# 
# ## Matplotlib
# 
# * zaměřena explicitně na tvorbu grafů
# * právě vzájemnou kombinací obou knihoven NumPy+matplotlib lze relativně
# * snadno dosáhnout velmi pěkných výsledků plně porovnatelných s výsledky
#   vytvořenými komerčními balíky.
# 
# ---
# 
# ### Možnosti knihovny Matplotlib
# 
# * grafy funkcí typu y = f(x)
# * parametrické zadání 2D průběhu x, y = f(t)
# * grafy funkcí typu z = f(x,y)
# * parametrické zadání 3D průběhu x, y, z = f(t)
# 
# ---
# 
# ### Zobrazení grafů
# 
# * na obrazovce
# * do plochy Jupyter Notebooku
# * do rastrových obrázků
# * do vektorových kreseb
# * do PDF
# 
# ---
# 
# ## Plotnine
# 
# ---
# 
# ## Zpracování obrazů a přirozeného jazyka v Pythonu
# 
# ---
# 
# ## Strojové učení
# 
# ---
# 
# ## Užitečné odkazy
# 
# * 15 Python Libraries for Data Science You Should Know
#     - https://www.dataquest.io/blog/15-python-libraries-for-data-science/
# * Top Python Libraries for Data Science in 2022
#     - https://www.datacamp.com/blog/top-python-libraries-for-data-science
# 
# ---
# 
# 

# # Praktická část

# ## NumPy

# ### Instalace
# * Nejprve je nutné naimportovat všechny potřebné funkce a konstanty z balíčku `numpy`
# 
# #### Používají se následující varianty importu
# 
# * `import numpy`
# 
# * `import numpy as np`
# 
# * `from numpy import *`
# 
# * `from numpy import array, linspace`
# 
# 

# In[2]:


import numpy as np


# ### Konstruktory polí
#  Postupně si popíšeme následující typy konstruktorů polí typu `ndarray`
# 
#  1. `numpy.array()`
#  1. `numpy.zeros()`
#  1. `numpy.ones()`
#  1. `numpy.full()`
#  1. `numpy.eye()`
#  1. `numpy.arange()`
#  1. `numpy.linspace()`
#  1. `numpy.geomspace()`
#  1. `numpy.logspace()`
# 

# #### Příklady použití funkce `numpy.array()`

# In[5]:


# Vytvoření pole ze seznamu
np.array([1, 2, 3, 4])


# In[7]:


# Vytvoření pole z generátoru `range`
np.array(range(10))


# In[9]:


# Vytvoření pole z generátoru `range`
np.array(range(10))


# In[10]:


# Explicitní specifikace uspořádání prvků pole
# (nemá velký význam pro 1D pole=vektory)
np.array(range(10), order="C")


# In[11]:


# Explicitní specifikace uspořádání prvků pole
# (nemá velký význam pro 1D pole=vektory)
np.array(range(10), order="F")


# In[12]:


# Vytvoření dvourozměrné matice
# konstrukce pole
np.array([[1, 2, 3], [4, 5, 6]])


# #### Specifikace typů buněk
# ```
# ╔════════════╤══════╗
# ║  Formát    │ Kód  ║
# ╟────────────┼──────╢
# ║ formát     │ kód  ║
# ║ bool       │ '?'  ║
# ║ int8       │ 'b'  ║
# ║ int16      │ 'h'  ║
# ║ int32      │ 'i'  ║
# ║ int64      │ 'l'  ║
# ║ uint8      │ 'B'  ║
# ║ uint16     │ 'H'  ║
# ║ uint32     │ 'I'  ║
# ║ uint64     │ 'L'  ║
# ║ float16    │ 'e'  ║
# ║ float32    │ 'f'  ║
# ║ float64    │ 'd'  ║
# ║ complex64  │ 'F'  ║
# ║ complex128 │ 'D'  ║
# ╚════════════╧══════╝
# ```

# In[6]:


l = [10000, 20000, 30000, 40000, 50000, 60000, 70000]
x = np.array(l, dtype='d')
x


# In[17]:


ls = [1, 3.14, 0]
y = np.array(ls)
y


# #### Konstruktor `numpy.zeros`
# - Vektor nebo matice s nulovými prvky
# - Poměrně častý požadavek v praxi
#     - opět lze zvolit interní uspořádání prvků
# - Volání konstruktoru numpy.zeros
# ```
# zeros(shape, dtype=float, order='C')
# ```

# In[14]:


# Jednorozměrný vektor s jediným prvkem
# konstrukce pole
np.zeros(1)


# In[16]:


# Jednorozměrný vektor s deseti prvky
np.zeros((10))


# In[17]:


# Matice o velikosti 3x4 prvky
np.zeros((3,4))


# In[18]:


# 3D pole
np.zeros((3,4,5))


# In[19]:


# Použití komplexních čísel
np.zeros((2, 2), dtype=complex)


# #### Konstruktor `numpy.ones`
# - Vektor či matice s prvky nastavenými na jedničku
# - (nejedná se o jednotkovou matici!)
#     - viz konstruktor `numpy.eye`
# - Volání konstruktoru numpy.ones
# ```
# ones(shape, dtype=None, order='C')
# ```

# In[20]:


# Jednorozměrný vektor s deseti prvky
np.ones(10)


# In[21]:


# Matice se třemi řádky a čtyřmi sloupci
np.ones((3, 4))


# In[22]:


# Matice se třemi řádky a čtyřmi sloupci s explicitní specifikací typu prvků
np.ones((3, 4), dtype=int)


# In[23]:


# Trojrozměrné pole s prvky typu `int`
np.ones((3, 4, 5), dtype=int)


# In[24]:


# Komplexní jednotka
# zde může být použití typu komplexní číslo možná poněkud překvapující ovšem stále platí, že 1=1+0j
np.ones((3, 2), dtype=complex)


# #### Konstruktor `numpy.eye`
# - Vytvoří se jednotková matice
# - Uvádí se její velikost
# - Lze ovšem vytvořit i nečtvercovou matici

# In[25]:


# Matice 1x1 prvek
np.eye(1)


# In[26]:


# Matice 5x5 prvků
np.eye(5)


# In[27]:


# Matice 2x10 prvků
np.eye(2, 10)


# #### Funkce `numpy.arange`
#  - Array+range
#  - Podobné jako xrange/range
#      - ovšem návratovou hodnotou je `ndarray`

# In[28]:


# Zavolání s jediným parametrem
# při použití jednoho parametru má tento parametr význam hodnoty „stop“
# vytvoří se vektor s prvky od 0 do „stop“ (kromě)
np.arange(10)


# In[29]:


# Specifikace hodnot „start“ (včetně) a „stop“ (kromě)
np.arange(10, 20)


# In[30]:


# Třetí nepovinný parametr určuje krok použitý při generování prvků vektoru
np.arange(10, 20, 2)


# In[31]:


# Krok může být samozřejmě záporný
np.arange(20, 10, -2)


# In[32]:


# Použití komplexních čísel
# Nemusíme zůstat pouze u celých čísel, protože pracovat je možné i s hodnotami
# typu `float` a `complex`
np.arange(0, 5, 0.1)


# In[33]:


# Použití komplexních čísel
np.arange(0 + 0j, 10 + 10j, 2 + 0j)


# #### Funkce `numpy.linspace()`
# - Při znalosti první a poslední hodnoty ve vektoru
# - Zadává se
#     - počáteční hodnota
#     - koncová hodnota
#     - počet prvků vektoru (implicitně 50 prvků)

# In[34]:


# Implicitní počet prvků
# pokud se nespecifikuje počet prvků, bude se předpokládat, že výsledný
# vektor má mít padesát prvků
np.linspace(0, 1)


# In[35]:


# Explicitní určení počtu prvků
# zde explicitně specifikujeme, že výsledný vektor má mít deset prvků
# (tím, že se začíná od nuly, získáme krok 0.11111111...)
np.linspace(0, 1, 10)


# In[36]:


# Explicitní určení počtu prvků
# zde explicitně specifikujeme, že výsledný vektor má mít jedenáct prvků
np.linspace(0, 1, 11)


# In[37]:


# Sekvence hodnot samozřejmě může i klesat
np.linspace(1, 0, 11)


# In[38]:


# Použít je možné i komplexní čísla
np.linspace(0 + 0j, 1 + 0j, 10)


# In[39]:


# Použít je možné i komplexní čísla
np.linspace(0 + 0j, 0 + 1j, 10)


# In[40]:


# Další možnost použití komplexních čísel
np.linspace(0 + 0j, 1 + 1j, 10)


# #### Funkce numpy.geomspace()
# - Krok mezi prvky není lineární ale tvoří geometrickou posloupnost
# - Při znalosti první a poslední hodnoty ve vektoru
# - Zadává se
#     - počáteční hodnota
#     - koncová hodnota
#     - počet prvků vektoru (implicitně 50 prvků)

# In[41]:


# Implicitní počet prvků
# pokud se nespecifikuje počet prvků, bude se předpokládat, že výsledný vektor má mít padesát prvků
np.geomspace(1, 100)


# In[42]:


# Explicitní počet prvků
# zde explicitně specifikujeme, že výsledný vektor má mít deset prvků
np.geomspace(1, 1000, 10)


# In[43]:


# Explicitní počet prvků
# zde explicitně specifikujeme, že výsledný vektor má mít šest prvků
np.geomspace(1, 100000, 6)


# #### Funkce numpy.logspace()
# - Krok mezi prvky není lineární ale tvoří logaritmickou posloupnost
# - Při znalosti první hodnoty, poslední hodnoty a báze
# - Nepatrně odlišné od funkce `linspace` a `geomspace`
# - Zadává se
#     - počáteční hodnota
#     - koncová hodnota
#     - báze (implicitně 10)
#     - krok je vypočten na základě ln(samples) / ln(base)

# In[44]:


# Implicitní počet prvků
# pokud se nespecifikuje počet prvků, bude se předpokládat, že výsledný vektor má mít padesát prvků
np.logspace(1, 100)


# In[45]:


# Explicitní počet prvků
# zde explicitně specifikujeme, že výsledný vektor má mít deset prvků
np.logspace(1, 10, 10)


# #### Přetypování prvků v poli
# - Dva způsoby
#     - konverzní funkce
#         - `numpy.float32()`
#         - `numpy.int32()`
#         - `numpy.complex128()`
#         - ...
#     - použití metody `astype`

# In[46]:


# Přetypování na typ `int64`

# konstrukce běžného seznamu
lst = [1, 2, 3, 4]

# přetypování (konstrukce pole daného typu)
np.int64(lst)


# In[47]:


# Přetypování na typ `float16`

# konstrukce běžného seznamu
lst = [1, 2, 3, 4]

# přetypování (konstrukce pole daného typu)
np.float16(lst)


# In[50]:


# Přetypování na vektor celých čísel

# konstrukce pole
np.linspace(0, 1, 10)

# přetypování na vektor celých čísel (povšimněte si výsledků)
np.int32(np.linspace(0, 1, 10))


# #### Použití metody astype

# In[51]:


# konstrukce pole
a = np.arange(0, 10)

# konverze
b = a.astype(np.complex64)

# tisk typu a obsahu původního pole
print(type(a))
print(a.dtype)
print(a)

# tisk typu a obsahu zkonvertovaného pole
print(type(b))
print(b.dtype)
print(b)


# ### Zjištění počtu dimenzí a tvaru pole
# 
# - Atribut `ndim`
# - Atribut `shape`
# - Funkce `numpy.shape()`

# In[55]:


# Zjištění počtu dimenzí a tvaru 1D pole

# jednorozměrný vektor
a = np.array([1, 2, 3])

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


# In[56]:


# Zjištění počtu dimenzí a tvaru 2D pole

# dvourozměrné pole
a = np.eye(5)

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


# In[57]:


# Zjištění počtu dimenzí tvaru 3D pole

# trojrozměrné pole
a = np.ones((3, 4, 5), dtype=int)

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


# In[59]:


x = np.arange(10)


# In[60]:


x.ndim


# In[61]:


x.shape


# In[62]:


y = np.zeros((6, 10))


# In[63]:


y


# In[64]:


y.ndim


# In[65]:


y.shape


# In[66]:


x.size


# In[67]:


x.itemsize


# In[68]:


y.size


# In[69]:


y.itemsize


# ### Změna tvaru polí

# In[83]:


np.linspace(1, 100, 100).reshape(10, 10)


# In[85]:


np.linspace(1, 100, 100).reshape(20, 5)


# In[87]:


np.linspace(1, 24, 24).reshape(2, 3, 4)


# In[9]:


z = np.linspace(1, 24, 24).reshape(4, 3, 2)


# In[10]:


z.reshape(2, 12)


# In[12]:


z.reshape(3, 2, 4)


# In[13]:


a = np.arange(10000).reshape(100, 100)


# ### Přístup k prvkům polí

# In[95]:


a


# In[15]:


x


# In[16]:


x[0]


# In[17]:


x[4]


# In[18]:


x[100]


# In[100]:


x[-1]


# In[101]:


x[-2]


# In[104]:


a = np.reshape(np.arange(12), (3, 4))


# In[105]:


a


# In[106]:


a[1]


# In[107]:


a[-1]


# In[108]:


a[1][3]


# In[109]:


a[1,3]


# In[110]:


b = np.reshape(np.arange(24), (2, 3, 4))


# In[111]:


b


# In[112]:


b[1, 0, -1]


# In[113]:


b[1]


# ### Adresování prvků obsahem jiného pole

# In[115]:


a = np.arange(12)


# In[116]:


a


# In[119]:


b = np.array([-1, 2, -9, -8, 5])


# In[120]:


a[b]


# In[121]:


c = np.arange(25).reshape(5,5)


# In[122]:


c


# In[126]:


i = np.array([[0,0], [1,1], [4,2]])


# In[127]:


i


# In[128]:


c[i]


# In[129]:


a


# In[130]:


a[3:7]


# In[131]:


a[3:-3]


# In[132]:


a[3:]


# In[133]:


a[:5]


# In[134]:


a[:]


# In[135]:


a[0:0]


# In[136]:


a[2:-2:3]


# In[137]:


c = np.arange(25).reshape(5,5)


# In[138]:


c


# In[143]:


c[2:4, 0:2]


# In[144]:


c[0:-1]


# In[146]:


c[0::2]


# In[147]:


c[0::2, 0::2]


# In[148]:


c = np.arange(100).reshape(10,10)


# In[149]:


c


# In[150]:


c[0::2, 0::2]


# ### Broadcasting a operace nad celými poli

# In[165]:


x = np.array([1,2,3])


# In[166]:


y = np.array([5,6,7])


# In[167]:


x


# In[168]:


y


# In[171]:


x*y


# In[172]:


10+x


# In[173]:


2*x


# In[174]:


c = np.arange(100).reshape(10,10)


# In[175]:


c


# In[176]:


c-50


# In[177]:


c+c


# In[178]:


c


# In[181]:


c *= 10


# In[182]:


c


# In[193]:


a1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11,12]])


# In[194]:


a1


# In[198]:


a2 = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])


# In[199]:


a2


# ### Operátor maticového součinu

# In[200]:


a1@a2


# ### Modul lineární algebry

# In[206]:


import numpy.linalg as l


# In[203]:


m = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 1]])


# In[204]:


m


# In[207]:


l.det(m)


# In[208]:


l.inv(m)


# ### Broadcasting podmínky

# In[209]:


a


# In[210]:


a < 5


# In[211]:


c


# In[212]:


c < 5000


# In[213]:


a


# In[218]:


b = np.array([0, 1, 2, 10, 20, 30, 7, 0, 0, 11, 11, 11])


# In[219]:


b


# In[220]:


a == b


# In[221]:


a < b


# In[222]:


a


# In[223]:


a < 6


# In[224]:


a[a<6]


# In[226]:


a%2==0


# ### Broadcasting podmínky + výběr prvků booleovským polem

# In[227]:


a[a%2==0]


# In[228]:


c = np.reshape(np.arange(100, 125), (5, 5))


# In[229]:


c


# In[231]:


c[c % 3 == 0]


# ### Operace prováděné nad celými osami

# In[232]:


a1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


# In[238]:


a1.min(axis=1)


# In[240]:


a1.max(axis=1)


# In[235]:


a1.max()


# In[241]:


a1.sum(axis=0)


# In[242]:


a1.sum(axis=1)


# In[243]:


a1


# In[244]:


a1-5


# In[245]:


np.abs(a1-5)


# In[246]:


a = np.linspace(0, np.pi/2)


# In[247]:


a


# In[248]:


np.sin(a)


# In[249]:


a1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


# In[250]:


a1


# In[251]:


a = np.apply_along_axis(lambda v: v[1], 0, a1)


# In[252]:


a


# In[253]:


a = np.array([[2]])
a


# In[254]:


b = np.array([10])


# In[256]:


l.solve(a, b)


# In[257]:


a = np.array([[1, 1], [1, -1]])


# In[258]:


b = np.array([2, 0])


# In[259]:


l.solve(a, b)


# In[260]:


# x=1, y=1


# ## Xarray

# In[1]:


import numpy as np
import xarray as xr


# ### Vytvoření 2D pole

# In[2]:


array = xr.DataArray(np.identity(10))
array


# ### Pojmenování dimenzí

# In[3]:


array = xr.DataArray(np.identity(10),
                     dims=("x", "y"))
array


# ### Pojmenování dimenzí, značky na osách

# In[4]:


array = xr.DataArray(np.identity(10),
                     dims=("x", "y"),
                     coords={"x":[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]})
array


# ### Uživatelské atributy

# In[5]:


temperatures = -10 + 40*np.random.rand(10, 10)

xcoords = np.linspace(10, 100, 10)
ycoords = np.linspace(-100, -10, 10)

array = xr.DataArray(temperatures,
                     name="Temperature measurement",
                     dims=("x", "y"),
                     coords={"x":xcoords, "y":ycoords},
                     attrs={
                         "units": "centigrees",
                         "description": "Local temperature values measured in grid",
                         "measured_by": {"name": "ThermometerBot",
                              "vendor": "BIY",
                              "version": (1, 0, 0)}
                         })
array


# ### Trojrozměrné pole (2D řezy v čase)

# In[6]:


temperatures = -10 + 40*np.random.rand(2, 2, 3)

longitudes = [[-99.83, -99.32], [-99.79, -99.23]]
latitudes = [[42.25, 42.21], [42.63, 42.59]]
times = ["2023-10-01", "2023-10-02", "2023-10-03"]

array = xr.DataArray(temperatures,
                     name="Temperature measurement",
                     dims=("x", "y", "time"),
                     coords={
                        "lon": (["x", "y"], longitudes),
                        "lat": (["x", "y"], latitudes),
                        "time": times,
                     },
                     attrs={
                         "units": "centigrees",
                         "description": "Local temperature values measured in grid",
                         "measured_by": {"name": "ThermometerBot",
                              "vendor": "BIY",
                              "version": (1, 0, 0)}
                         })
array


# ### Reprezentace šachové partie (pro oddych)

# In[7]:


chessboard = np.array([" "]*64).reshape(8, 8)
chessboard[0, 0] = "♚"
chessboard[1, 5] = "♔"
chessboard[2, 5] = "♙"
chessboard[3, 4] = "♜"

files = ["a", "b", "c", "d", "e", "f", "g", "h"]
ranks = np.linspace(1, 8, 8, dtype=np.int8)

array = xr.DataArray(chessboard,
                     name="Saavedra position",
                     dims=("files", "ranks"),
                     coords={"files":files, "ranks":ranks})

array.attrs["units"] = "chess pieces"
array.attrs["description"] ="White to move and win",
array.attrs["metadata"] = {"played by": "Fernando Saavedra",
                           "winner": "white",
                           "see also": "https://www.youtube.com/watch?v=Mg2OOsQPURs",}

arrayarray.sel(files="c")


# In[8]:


array.sel(files="c")array.sel(ranks=6)


# In[9]:


array.sel(ranks=6)


# ### Operace `groupby` a časové řady

# In[14]:


measured_at = np.arange(
        np.datetime64("2023-01-01"),
        np.datetime64("2024-01-01"),
        np.timedelta64(1, "D")).astype('datetime64[ns]')

temperatures = 10 + 20 * np.random.rand(365)

array = xr.DataArray(temperatures,
                     name="Temperature measurement",
                     dims=("time",),
                     coords={"time":measured_at},
                     attrs={
                         "units": "centigrees",
                         "description": "Local temperature values measured in time serie #1",
                         "measured_by": {"name": "ThermometerBot",
                              "vendor": "BIY",
                              "version": (1, 0, 0)}
                         })

array.groupby("time.season")


# In[15]:


array.groupby("time.dayofweek")


# In[17]:


array.groupby("time.month")


# ### Výběr nejbližší známé hodnoty (algoritmus "nearest")

# In[12]:


temperatures = np.arange(0, 300).reshape((10, 10, 3))

xcoords = np.linspace(10, 100, 10)
ycoords = np.linspace(-100, -10, 10)

times = ["2023-10-01", "2023-10-02", "2023-10-03"]

array = xr.DataArray(temperatures,
                     name="Temperature measurement",
                     dims=("x", "y", "time"),
                     coords={"x":xcoords, "y":ycoords, "time":times},
                     attrs={
                         "units": "centigrees",
                         "description": "Local temperature values measured in grid",
                         "measured_by": {"name": "ThermometerBot",
                              "vendor": "BIY",
                              "version": (1, 0, 0)}
                         })

array.sel(time="2023-10-02").sel(x=51, y=-51, method="nearest")


# ## Matplotlib

# In[30]:


import matplotlib.pyplot as plt


# In[27]:


x = np.linspace(0, 2*np.pi, 100)


# In[21]:


x


# In[28]:


y = np.sin(x)


# In[23]:


y


# In[31]:


plt.plot(x,y)
plt.xlabel("t")
plt.ylabel("sin(t)")
plt.title("Sinusovka")


# In[32]:


plt.show()


# In[290]:


x = np.linspace(0, 2*np.pi, 100)
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


# In[33]:


x = np.linspace(0.01, 4*np.pi, 100)
# hodnoty na y-ové ose: první funkce

y1 = np.sin(x)
# hodnoty na y-ové ose: druhá funkce

y2 = np.cos(x)
# hodnoty na y-ové ose: třetí funkce

y3 = np.sin(x)/x
# vykreslit průběh všech tří funkcí se změnou stylu vykreslování

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


# In[34]:


x = np.linspace(0, 2*np.pi, 100)

# hodnoty na y-ové ose: první funkce
y1 = np.sin(x)

# hodnoty na y-ové ose: druhá funkce
y2 = np.sin(3*x)/(x+1)

# vykreslit průběh obou funkcí se změnou stylu vykreslování
plt.fill(x, y1, "red", x, y2, "yellow", alpha=0.5)
plt.plot(x, y2, "blue")

# popis os
plt.xlabel("x")
plt.ylabel("sin(x) a sinc(3x)")

# zobrazení grafu
plt.show()


# In[35]:


x = np.linspace(0.001, 2*np.pi, 100)

y1 = np.sin(5*x)

y2 = np.sin(5*x)/(x+1/2)

y3 = 1/(x+1/2)
y4 = -y3

plt.fill(x, y1, "yellow", alpha=0.3, label="sin x")
plt.fill(x, y2, "r.", alpha=1.0, label="sinc 5x")
plt.plot(x, y3, "g--", label="obalka sinc")
plt.plot(x, y4, "g--", label="obalka sinc")

plt.legend(loc="upper right")

plt.xlabel("x")
plt.ylabel("sin(x) a sinc(3x)")

plt.show()


# In[36]:


x = np.linspace(0, 2*np.pi, 100)
# hodnoty na y-ové ose: první funkce

y1 = np.sin(x)
# hodnoty na y-ové ose: druhá funkce

y2 = np.cos(x)
# vykreslit průběh obou funkcí se změnou stylu vykreslování

plt.plot(x, y1, "b-", label="sin")
plt.plot(x, y2, "r-", label="cos")
# přidání legendy

plt.legend(loc="lower left")
# nastavení rozsahů na obou osách

plt.axis([-1, 7, -1.5, 1.5])


# vložit první popisek do grafu
plt.annotate("maximální hodnota sin(x)",
             xy=(np.pi/2, 1.0),
             xytext=(0, 1.3),
             arrowprops=dict(arrowstyle="->"))

# vložit druhý popisek do grafu
plt.annotate("minimální hodnota cos(x)",
             xy=(np.pi, -1.0),
             xytext=(2, -1.3),
             arrowprops=dict(arrowstyle="->"))

# povolení zobrazení mřížky
plt.grid(True)

# popis os
plt.xlabel("x")
plt.ylabel("sin(x) a cos(x)")
# zobrazení grafu

plt.show()


# In[37]:


# úhel v polárním grafu
theta = np.linspace(0.01, 2*np.pi, 150)

# vzdálenost od středu
radius = theta#np.log(theta)

ax = plt.subplot(111, projection="polar")

# vykreslit průběh funkce v polárním grafu
ax.plot(theta, radius)

# zobrazení grafu
plt.show()


# In[38]:


# úhel v polárním grafu
theta = np.linspace(0.01, 2*np.pi, 150)

# první funkce: vzdálenost od středu
radius1 = theta

# druhá funkce: vzdálenost od středu
radius2 = 2*np.abs(theta-np.pi)

# třetí funkce: vzdálenost od středu
radius3 = 2*np.log(theta)

ax = plt.subplot(111, projection="polar")

# vykreslit průběh první funkce v polárním grafu
ax.plot(theta, radius1, "r.", label="f1")

# vykreslit průběh druhé funkce v polárním grafu
ax.plot(theta, radius2, "g", label="f2")

# vykreslit průběh třetí funkce v polárním grafu
ax.plot(theta, radius3, "b--", label="f3")

# přidání legendy
plt.legend(loc="lower left")

# zobrazení grafu
plt.show()


# In[39]:


# úhel v polárním grafu

theta = np.linspace(0.01, 4*np.pi, 150)
# první funkce: vzdálenost od středu

radius1 = theta
# druhá funkce: vzdálenost od středu

radius2 = 3*np.abs(theta-2*np.pi)

ax = plt.subplot(111, projection="polar")
# vykreslit průběh první funkce v polárním grafu

ax.plot(theta, radius2, "b", label="f1")
# vykreslit průběh druhé funkce v polárním grafu

ax.fill(theta, radius1, "yellow", alpha=0.3, label="f1")

ax.plot(theta, radius1, "red")

# přidání legendy

plt.legend(loc="lower left")
# zobrazení grafu

plt.show()


# In[40]:


# hodnoty na x-ové ose

x = np.linspace(0.2, 2*np.pi, 100)
# hodnoty na y-ové ose

y = np.sin(5*x)/x
y2 = 1/x
y3 = -y2
# vykreslit průběh funkce

plt.plot(x, y2, color='red',  label='obalka sinc')
plt.plot(x, y3, color='red',  label='obalka sinc')
plt.plot(x, y,  color='blue', label='sinc(x)', drawstyle='steps')
# povolení zobrazení mřížky

plt.grid(True)
# popis os

plt.xlabel("x")
plt.ylabel("sinc(x)")
# přidání legendy

plt.legend(loc="lower right")
# zobrazení grafu

plt.show()


# In[41]:


# historické ceny ropy

cena_ropy = [
    46.68, 44.68, 46.90, 47.15, 44.59, 44.00, 44.63, 45.92, 44.15, 45.94,
    46.05, 46.75, 46.25, 45.41, 49.20, 45.22, 42.56, 38.60, 39.31, 38.24,
    40.45, 41.32, 40.80, 42.62, 41.87, 42.50, 42.23, 43.30, 43.08, 44.96,
    43.87, 44.66, 45.15, 47.12, 48.52, 48.79, 47.98, 47.39, 48.14, 48.45]
# počet prvků

fig = plt.figure(figsize=(15, 12))

N = len(cena_ropy)
# indexy prvků

indexes = np.arange(N)
# šířka sloupců

width = 1.00
# sloupcový graf

plt.bar(indexes, cena_ropy, width, color='yellow', edgecolor='black',
        label='Cena ropy')
# povolení zobrazení mřížky

plt.grid(True)
# přidání legendy

plt.legend(loc="lower right")
# zobrazení grafu

plt.show()


# In[42]:


# první pole hodnot
vals1 = [10, 15, 20, 12, 14, 8]

# druhé pole hodnot
vals2 = [19, 18,  6, 11,  6, 14]

# počet prvků
N = len(vals1)

# indexy prvků
indexes = np.arange(N)

# šířka sloupců
width = 0.30

# sloupcový graf se dvěma skupinami sloupců
plt.bar(indexes, vals1, width, color='gray', edgecolor='black', label='CPU#1')

# posunuté sloupce
plt.bar(indexes+width, vals2, width, color='red', edgecolor='black',
        label='CPU#2')

plt.plot(indexes, vals1)

# povolení zobrazení mřížky
plt.grid(True)

# přidání legendy
plt.legend(loc="upper right")

# zobrazení grafu
plt.show()


# In[43]:


# náhodné hodnoty

y = np.random.normal(0, 0.1, 10000)

plt.hist(y, bins=100, range=None, density=True)

# zobrazení grafu
plt.show()


# In[44]:


# musíme naimportovat ještě jeden balíček
from matplotlib import font_manager as fm  # noqa: E402

# make a square figure and axes
fig = plt.figure(1, figsize=(6, 6), dpi=100)
ax = fig.add_axes([0.16, 0.16, 0.68, 0.68])

plt.title("Scripting languages")
ax.title.set_fontsize(30)

# popisky jednotlivých výřezů
labels = ['Perl', 'Python', 'Ruby']

# šířky jednotlivých výřezů
fracs = [90, 150, 20]

# vytvoření koláčového grafu
ax.pie(fracs, labels=labels, autopct='%1.1f%%', shadow=False)

# zobrazení grafu
plt.show()


# In[45]:


# make a square figure and axes
fig = plt.figure(1, figsize=(6, 6), dpi=100)
ax = fig.add_axes([0.16, 0.16, 0.68, 0.68])

plt.title("Scripting languages")
ax.title.set_fontsize(30)

# popisky jednotlivých výřezů

labels = ['Perl', 'Python', 'Ruby']

# šířky jednotlivých výřezů
fracs = [90, 150, 70]

# vytáhnutí výřezů
explode = (0.0, 0.0, 0.15)

# barvy
colors = ('yellow', '#60ff60', 'red')

# vytvoření koláčového grafu
patches, texts, autotexts = ax.pie(fracs, explode=explode, colors=colors,
                                   labels=labels, autopct='%1.1f%%',
                                   shadow=True)
# změna stylu písma
proptease = fm.FontProperties()
proptease.set_size('xx-large')
plt.setp(autotexts, fontproperties=proptease)
plt.setp(texts, fontproperties=proptease)

# zobrazení grafu
plt.show()


# In[51]:


# první pole hodnot a pole odchylek
vals1 = [10, 15, 20, 12, 14, 8]
delta1 = [1, 2, 3, 4, 5, 0]

# druhé pole hodnot a pole odchylek
vals2 = [19, 18,  6, 11,  6, 14]
delta2 = [4, 2, 3, 2, 2, 4]

# počet prvků
N = len(vals1)

# indexy prvků
indexes = np.arange(N)

# šířka sloupců
width = 0.30

# sloupcový graf se dvěma skupinami sloupců
plt.bar(indexes, vals1, width, color='gray', edgecolor='black', label='CPU#1',
        yerr=delta1, error_kw=dict(elinewidth=2, ecolor='red'))

# posunuté sloupce
plt.bar(indexes+width, vals2, width, color='red', edgecolor='black',
        label='CPU#2',
        yerr=delta2, error_kw=dict(elinewidth=2, ecolor='#606000'))

# povolení zobrazení mřížky
plt.grid(True)

# přidání legendy
plt.legend(loc="lower right")

# zobrazení grafu

plt.show()


# In[52]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# příprava vektorů pro konstrukci mřížky
x = np.linspace(-4, 4, 50)
y = np.linspace(0, 8, 50)

# konstrukce mřížky
x, y = np.meshgrid(x, y)

# implicitní funkce paraboly
f = 0.5
p = 2*f
z = x**2 - p*p*y + 5*np.sin(y)

# inicializace grafu
fig = plt.figure()

# nastavení 3D projekce
### starý Matplotlib: ax = fig.gca(projection='3d')
ax = fig.add_subplot(projection = '3d')

# zobrazení 3D grafu formou plochy
surface = ax.plot_surface(x, y, z, rstride=2, cstride=2, cmap=cm.coolwarm,
                          linewidth=0, antialiased=False)

# titulek grafu
fig.suptitle('Parabola', fontsize=15)

# rozměry grafu ve směru osy x
ax.set_xlabel('X')
ax.set_xlim(-4, 4)

# rozměry grafu ve směru osy y
ax.set_ylabel('Y')
ax.set_ylim(0, 8)

# rozměry grafu ve směru osy z
ax.set_zlabel('Z')
ax.set_zlim(0, 10)

# uložení grafu do rastrového obrázku
plt.savefig("parabola1.png")

# zobrazení grafu
plt.show()


# ### Meshgrid

# In[53]:


x = np.arange(0.0, 5, 1)


# In[54]:


x


# In[55]:


y = np.arange(10.0, 15, 1)


# In[56]:


y


# In[57]:


X, Y = np.meshgrid(x, y)


# In[58]:


X


# In[59]:


Y


# In[ ]:





# In[50]:


# import dvou dalších potřebných knihoven

import matplotlib.cm as cm  # noqa: E402
import matplotlib.mlab as mlab  # noqa: E402

fig = plt.figure(1, figsize=(8, 6), dpi=100)

delta = 0.1

# průběh nezávislé proměnné x
x = np.arange(-10.0, 10.0, delta)

# průběh nezávislé proměnné y
y = np.arange(-10.0, 10.0, delta)

# vytvoření dvou polí se souřadnicemi [x,y]
X, Y = np.meshgrid(x, y)

# vzdálenost od bodu [0,0]
R1 = np.sqrt(X*X+Y*Y)

# vzdálenost od bodu [3,3]
R2 = np.sqrt((X-3)*(X-3)+(Y-3)*(Y-3))

# výpočet funkce, kterou použijeme při vykreslování grafu
Z = np.sin(R1)-np.cos(R2)

# povolení zobrazení mřížky
plt.grid(True)

# vytvoření grafu s konturami funkce z=f(x,y)
CS = plt.contour(X, Y, Z)

# popisky “vrstevnic”
plt.clabel(CS, inline=1, fontsize=10)

CB = plt.colorbar(CS, shrink=0.7, extend='both')

plt.contour(X, Y, Z)
# zobrazení grafu

plt.show()


# ## Scipy

# ## Pandas

# ### Načtení dat do datového rámce

# In[3]:


import pandas

# přečtení zdrojových dat
df = pandas.read_csv("tiobe.tsv", sep="\t")

# datový rámec zobrazíme
print(df)
print()

# podrobnější informace o datovém rámci
print(df.dtypes)
print()

# více podrobnějších informací o datovém rámci
print(df.info())
print()


# ### Transformace v průběhu načítání dat

# In[4]:


import pandas

# přečtení zdrojových dat
df = pandas.read_csv("tiobe.tsv", sep="\t")

# specifikace indexu - má se získat ze sloupce Language
df.set_index("Language", inplace=True)

# formát hodnot ve sloupci
df["Ratings"] = df["Ratings"].transform("Rating is {:4.1f}%".format)

# datový rámec zobrazíme
print(df)
print()

# podrobnější informace o datovém rámci
print(df.dtypes)
print()

# více podrobnějších informací o datovém rámci
print(df.info())
print()


# ### Agregace výsledků

# In[12]:


import pandas
import numpy as np

# přečtení zdrojových dat
df = pandas.read_csv("tiobe.tsv", sep="\t")

# specifikace indexu - má se získat ze sloupce Language
df.set_index("Language", inplace=True)

# agregace výsledků
results = df["Ratings"].agg([pandas.Series.min, pandas.Series.max, pandas.Series.sum, pandas.Series.mean])

# tisk vypočtených výsledků
print("Results")
print(results)


# ### Kombinace

# In[13]:


import pandas

# přečtení zdrojových dat
df = pandas.read_csv("tiobe.tsv", sep="\t")

# specifikace indexu - má se získat ze sloupce Language
df.set_index("Language", inplace=True)

# omezení hodnot
df["Ratings"] = df["Ratings"].combine(10, min)

# omezení hodnot
df["Ratings"] = df["Ratings"].combine(2, max)

# datový rámec zobrazíme
print(df)
print()

# podrobnější informace o datovém rámci
print(df.dtypes)
print()

# více podrobnějších informací o datovém rámci
print(df.info())
print()


# ## Scikit-learn

# ## Plotnine

# ### Načtení testovacích dat

# In[4]:


from plotnine.data import economics


# In[5]:


economics


# ### Základní analýza nad daty

# In[6]:


economics.describe()


# ### Jednoduchý graf

# In[7]:


from plotnine import ggplot, aes, geom_line, labs


# In[8]:


ggplot(economics) + aes(x="date", y="uempmed") + geom_line() + labs(x="date", y="median duration of unemployment")


# ### Aproximace

# In[9]:


from plotnine import geom_point, geom_smooth, xlab, ylab


# In[10]:


(ggplot(economics)
        + aes(x="date", y="uempmed")
        + geom_point()
        + geom_smooth(color="red")
        + xlab("date (year)")
        + ylab("unemploynment"))


# ### Možnosti aproximace

# In[11]:


(ggplot(economics)
        + aes(x="date", y="uempmed")
        + geom_point(size=0.2)
        + geom_smooth(color="#ff0000", span=1)
        + geom_smooth(color="#cc0044", span=0.5)
        + geom_smooth(color="#880088", span=0.3)
        + geom_smooth(color="#4400cc", span=0.2)
        + geom_smooth(color="#0000ff", span=0.1)
        + xlab("date (year)")
        + ylab("unemploynment"))


# In[ ]:




