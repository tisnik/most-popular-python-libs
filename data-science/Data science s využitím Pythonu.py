#!/usr/bin/env python
# coding: utf-8

# # Data science s využitím Pythonu
# 
# ---
# 
# * Pavel Tišnovský
# * kurzy.python@centrum.cz
# 
# ---
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
# * Knihovny používané v této oblasti: NumPy, Pandas, Polars, Seaborn, scikit-learn
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
# * Moderní způsoby využití Pythonu
#     - AI
#     - Machine Learning (Deep Learning)
#     - PyTorch
#     - Big data
# * Tzv. „glue“ jazyk
# * Vestavitelný interpret Pythonu
# 
# ---
# 
# ## Nástroje pro datovou analýzu
# 
# * Data mining
# * Data procesing a modelování
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
# ### NumPy
# 
# ![numpy_arrays.png](images/numpy_logo.png)
# 
# ---
# 
# ### NumPy
# 
# * výslovnosti
#     - [nəmpᴧɪ]
#     - [nəmpi]
# * historie
#     - matrix package
#     - Numeric
#     - NumPy
# * Kooperace s dalšími knihovnami a frameworky
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
# 
# ### Nativní (skalární) datové typy
# 
# ```
# ```
# 
# ---
# 
# ### N-dimenzionální pole
# 
# ![numpy_arrays.png](images/numpy_arrays.png)
# 
# ---
# 
# ### N-dimenzionální pole
# 
# * Představuje obecné n-dimenzionální pole
# * Interní způsob uložení dat zcela odlišný od Pythonovských seznamů či n-tic
#     - „pohled“ na kontinuální blok hodnot
# * Homogenní datová struktura
#     - menší flexibilita
#     - menší paměťové nároky
#     - vyšší výpočetní rychlost díky použití nativního kódu
#     - obecně lepší využití cache a rychlejší přístup k prvkům
# * Základní strukturovaný datový typ knihovny NumPy
# 
# ---
# 
# ### N-dimenzionální pole
# 
# * Volitelný typ prvků
# * Volitelný počet dimenzí
#     - vektory
#     - matice
#     - pole s větším počtem dimenzí
# * Volitelné uspořádání prvků
#     - podle zvyklostí jazyka Fortran
#     - podle zvyklostí jazyka C
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
# ### Pandas
# 
# ---
# 
# ### Polars
# 
# ---
# 
# ### Matplotlib
# 
# ---
# 
# ## Vizualizace dat: Matplotlib
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
# ### Užitečné odkazy
# 
# * 15 Python Libraries for Data Science You Should Know
#     - https://www.dataquest.io/blog/15-python-libraries-for-data-science/
# * Top Python Libraries for Data Science in 2022
#     - https://www.datacamp.com/blog/top-python-libraries-for-data-science
# 
# ---
# 

# In[ ]:




