# Jazyk Python - základy programování

* Pavel Tišnovský
    - `kurzy.python@centrum.cz`
* Slajdy a demonstrační příklady:
    - `https://github.com/tisnik/python-programming-courses`

---

## Obsah kurzu (1/3)

* Úvod
    - proč a k čemu používat Python
    - srovnání s ostatními programovacími jazyky
* Základy jazyka
    - čísla a řetězce
    - řetězce Unicode
    - seznamy (pole)
    - n-tice
    - práce se slovníky
* Řízení toku programu
    - základní konstrukce
    - funkce
    - příkazy
    - větvení
    - programové smyčky

---

## Obsah kurzu (2/3)

* Procedury a funkce
    – použití
    - definice funkcí
    - platnost proměnných
* Funkcionální prvky jazyka Python
    - lambda výrazy
* Moduly
    – přehled
    - vyhledávání
    - pravidla
    - funkce, balíčky
* Vstup a výstup
    – práce se soubory
    - souborové objekty
    - formátování výstupu

---

## Obsah kurzu (3/3)

* Chyby a výjimky
    – přehled
    - vyvolání výjimky
    - obsluha výjimek
    - syntaktické chyby
    - složitější použití
* Třídy
    – použitá terminologie
    - definování
    - objekty
    - dědičnost
    - speciální metody
* Iterátory, generátory
* Nejpoužívanější knihovny
* Užitečné nástroje pro Python

---

## Úvod

* Základní informace o programovacím jazyku Python
* Proč a k čemu používat jazyk Python
* Srovnání s ostatními programovacími jazyky
* Implementace Pythonu
* Python 2.x vs Python 3.x

---

### Základní informace o jazyku Python

* Interpret
    - s generováním bajtkódu
* Objektově orientovaný jazyk
* Dynamicky typovaný
* Používá odsazení pro deklaraci bloků
* Dostupný pro mnoho platforem
    - MS Windows
    - Linux
    - Apple
    - jednodeskové mikropočítače
* Používaný pro CLI aplikace, na serverech, pro GUI atd.
* "Batteries included"
    - rozsáhlá základní knihovna
    - nápověda
    - dostupné nástroje (tools)

---

### Interpretry vs překladače

* Interpret
    - Python, Perl, JavaScript, Ruby, TCL, shelly
    - typicky dynamicky typované jazyky (rychlejší vývoj)
    - snadněji použitelné (jednodušší syntaxe a sémantika)
    - kompaktnější kód
    - obecně pomalejší běh programů
    - lepší podpora tzv. introspekce
* Překladač
    - Java, C, C++, C#, Fortran
    - nutnost překladu (a slinkování)
    - pomalejší cyklus vývoje: editace-překlad-slinkování-spuštění
    - výsledné aplikace rychlejší (1:10 apod.)

---

### Proč a k čemu používat programovací jazyk Python

* Nástroje a utility ovládané z příkazového řádku
* Aplikace s grafickým uživatelským rozhraním
* Client-server
    - serverová část (Flask, Django, ...)
* Numerické výpočty, symbolické výpočty
    - Numpy
    - SciPy
    - Matplotlib
* Zpracování dat
    - Pandas
* Moderní způsoby využití Pythonu
    - AI
    - Machine Learning (Deep Learning)
    - Big data
* Tzv. "glue" jazyk

---

### Vývojová prostředí pro Python

* IDLE
    - výchozí, relativně primitivní
* VSCode
    - s rozšířením pro Python
* PyCharm
    - profesionální IDE

---

### IDLE
    - https://docs.python.org/3/library/idle.html
    - vytvořeno přímo v Pythonu
    - používá `tkinter`
    - využitelné na Windows, Linuxu i macOS
    - editor zdrojových kódů
    - debugger
    - Python shell (REPL)

---

### Srovnání s ostatními programovacími jazyky

* Skriptovací jazyk
    - Perl
    - Ruby
* Dynamicky typovaný jazyk
    - Ruby, Perl
* Automatická správa paměti (garbage collector)
    - obsahuje většina moderních jazyků
* Objektově orientovaný jazyk
    - Java
    - C++
    - C#

---

### Implementace Pythonu

* Nejpoužívanější implementace
    - CPython
    - Jython
    - Iron Python
    - Pypy

* Další implementace
    - Psyco
    - Stackles Python
    - MicroPython

* Speciální implementace
    - Cython
    - RPython
    - Numba

---

### Python pro Windows

* Oficiální instalace Pythonu
    - https://www.python.org/downloads/windows/
* ActiveState Python
    - https://www.activestate.com/products/python/

---

### Python 2.x vs Python 3.x

* Tyto dvě větve nejsou plně kompatibilní
* Skript `2to3` pro automatický převod
    - nutno ručně zkontrolovat
* Nejdůležitější rozdíly
    - `print`: příkaz vs funkce
    - celočíselné dělení (operátory / a //)
    - Unicode řetězce: nyní tři typy (str, byte, bytearray)
    - striktnější pravidla při porovnávání hodnot různých typů
    - `xrange()`: nyní se `range()` chová jako `xrange()`
    - argument při vyhazování výjimek musí být v závorkách
    - `except TypVýjimky, e:` versus `except TypVýjimky as e:`
    - generátory nemají metodu `next()`, namísto ní se používá funkce `next()`
    - `range()` vrací iterátor, ne seznam
    - některé funkce typu `apply()` byly přesunuty do zvláštního modulu

---

### Python 2.x vs Python 3.x: range/xrange

```python
n = 10000

def test_range(n):
    for i in range(n):
        pass

def test_xrange(n):
    for i in xrange(n):
        pass

test_range(n)
test_xrange(n)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/range.py)

---

## Základy programovacího jazyka Python

* Python jako skriptovací jazyk
* Vstupně/výstupní funkce
* Ukázkový příklad
* Rezervovaná klíčová slova
* Datové typy
* Čísla
* Pravdivostní hodnoty
* Řetězce (raw, Unicode)
* Seznamy (pole)
* Slovníky
* Množiny
* N-tice

---

### Python jako skriptovací jazyk

```python
# Body Mass Index calculator

print("Mass (kg): ")
mass = int(input())

print("Height (cm): ")
height = int(input())

# předod výšky na metry
height = height / 100.0

# výpočet (bez jakýchkoli kontrol)
bmi = mass / (height * height)

# výpis výsledku
print("BMI = ", bmi)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/bmi.py)

---

### Python jako skriptovací jazyk

* Spuštění
    - nepřímo z příkazové řádky
    - přes interpret

```
python bmi.py
```

```
python2 bmi.py
```

```
python3 bmi.py
```

---

### Základní vstupně/výstupní funkce

* Koncept tzv. proudů
    - input stream
    - output stream
    - error stream
* `print()`
    - tisk jakékoli hodnoty
    - viz další slajd
* `input()`
    - se zpracováním vstupu
    - v Pythonu 2 se odvozoval typ hodnoty
    - v Pythonu 3 se vždy vrací řetězec
* `raw_input()`
    - existuje v Pythonu 2
    - vždy vrací řetězec (vs `input()`)
* `input("zprava")`
    - zobrazí navíc zprávu (výzvu) uživateli

---

### Funkce print

* Existuje ve formě příkazu v Pythonu 2.x:

```python
print "Hello"
```

* V Pythonu 3 se však jedná o funkci:

```python
print("Hello")
```

* Použijeme ji v navazujících slajdech

---

### Funkce print
* Výhody `print` jako funkce
    - lze použít v lambda výrazech
    - není nutná speciální syntaxe
    - řešení tisku prázdných řádků
    - (uvidíme dále)

---

### Základní struktura kódu v Pythonu

```python
#!/usr/bin/env python
# encoding=utf-8

"""Dokumentační řetězec"""

# importy
# třídy
# funkce

if __name__ == "__main__":
    # vstupní bod programu
```

---

### Ukázkový příklad - úprava kalkulátoru BMI

```python
#!/usr/bin/env python
# encoding=utf-8

"""Body Mass Index calculator."""

import sys


def compute_bmi(mass, height):
    """Vlastní výpočet BMI za základě hmotnosti a výšky."""
    height = height / 100.0
    bmi = mass / (height * height)
    return bmi


print("Mass (kg): ")
mass = int(input())

# kontrola na špatný vstup
if mass < 0:
    print("Invalid input")
    sys.exit(1)

print("Height (cm): ")
height = int(input())

# kontrola na špatný vstup
if height < 0:
    print("Invalid input")
    sys.exit(1)

# výpočet výsledku a výpis na obrazovku
print("BMI = ", compute_bmi(mass, height))
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/bmi_2.py)

---

### Ukázkový příklad (pokračování)

* Příklad spuštění:
    - Linux, BSD, další Unixy

```
chmod u+x bmi.py
./bmi.py
```

* Stále lze spustit i přes interpret

```
python bmi.py
```

```
python2 bmi.py
```

```
python3 bmi.py
```

---

## Základy Pythonu

---

### Rezervovaná klíčová slova Pythonu

```
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
```

* Nelze je použít jako běžné identifikátory
    - jména proměnných
    - jména funkcí
    - názvy tříd a metod

---

### Soft keywords

```
match
case
type
_
```

* V některém kontextu se chovají jako klíčová slova
* Ovšem obecně ne
* Byly přidány do Pythonu později

---

### Proměnné

* Udržují informaci o stavu aplikace

* Dynamicky typované
    - typ proměnné = typ hodnoty do proměnné uložené
    - může se v rámci jednoho programu měnit
    - viditelnost proměnných (viz další slajdy)

* Různá oblast platnosti/viditelnosti

---

### Příklad použití proměnných

```python
x = 42
y = "Python"
z = 3e27

print(x)
print(y)
print(z)

x = None
print(x)

x = 10
print(x)

x = "něco jiného"
print(x)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/variables.py)

---

### Datové typy

* čísla (tři typy)
    - int / long
    - float
    - complex
* pravdivostní hodnoty (Boolean, bool)
* řetězce (string)
* seznamy (list)
* slovníky (dictionary, dict)
* množiny (set)
* n-tice (tuple)
* sekvence bajtů (bytes)
    - v praxi většinou není příliš důležitý
* pole bajtů (bytearray)
    - v praxi většinou není příliš důležitý
* frozenset
* NoneType
* objekt

---

### Měnitelnost/neměnitelnost

* mutability/immutability
* význam ve funkcionálních i imperativních jazycích
* Měnitelné typy
    - seznamy
    - slovníky
    - množiny
    - pole bajtů (bytearray)
    - objekt
* Neměnitelné typy
    - čísla
    - pravdivostní hodnoty
    - řetězce
    - n-tice
    - frozenset
    - sekvence bajtů
    - NoneType

---

### Homogennost

* všechny prvky uložené v tzv. kontejneru mají shodný typ
* význam v některých programovacích jazycích, které například vyžadují homogenní pole
* v Pythonu jsou kontejnery obecně *nehomogenní*
    - seznamy
    - n-tice
    - slovníky
    - množiny

---

### Čísla

* měnitelnost
    - neměnitelné
* ve skutečnosti existují tři typy číselných hodnot
    - `int` / `long` (Python 2.x / Python 3.x)
    - `float`
    - `complex`

```python
print(42)
print(3.1415)
print(2+3j)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/numbers1.py)

* pozor na:
    - operátory se odlišují podle použitého typu
    - zápis komplexního čísla s "j" a nikoli s "i"
    - nekompatibilita u operátoru `/` (viz další slajdy s popisem operátorů)
## Časté problémy

---

```python
# Třídní atributy jsou de facto uloženy ve slovníku
# Ve skutečnosti B a C nemají vlastní hodnoty atributů
# pouze reference do A


class A(object):
    attribute = "foo"


class B(A):
    pass


class C(A):
    pass


print(A.attribute, B.attribute, C.attribute)

A.attribute = "baz"

print(A.attribute, B.attribute, C.attribute)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/pitfalls/classes.py)

```python
# výchozí hodnota funkce je vyhodnocena pouze jedenkrát
# a to ve chvíli definici funkce


def foo(bar=[]):
    bar.append("baz")
    return bar


print(foo())

print(foo())

print(foo())
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/pitfalls/default_argument_1.py)

```python
# výchozí hodnota funkce je vyhodnocena pouze jedenkrát
# a to ve chvíli definici funkce


def foo(bar=None):
    if bar is None:
        bar = []
    bar.append("baz")
    return bar


print(foo())

print(foo())

print(foo())
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/pitfalls/default_argument_2.py)

```python
x = 1


def foo():
    x += 1
    print(x)


foo()
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/pitfalls/scoping1.py)

```python
x = 1


def foo():
    global x
    x += 1
    print(x)


foo()
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/pitfalls/scoping2.py)

```python
seznam = []


def foo(x):
    seznam.append(x)


print(seznam)
foo(1)
print(seznam)
foo(2)
print(seznam)


def bar(x):
    seznam += [x]


print(seznam)
bar(3)
print(seznam)
bar(4)
print(seznam)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/pitfalls/scoping3.py)

```python
seznam = []


def foo(x):
    seznam.append(x)


print(seznam)
foo(1)
print(seznam)
foo(2)
print(seznam)


def bar(x):
    global seznam
    seznam += [x]


print(seznam)
bar(3)
print(seznam)
bar(4)
print(seznam)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/pitfalls/scoping4.py)

```python
y = 10


def adder(x):
    return y + x


print(adder(1))

y = 20

print(adder(1))
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/pitfalls/closures.py)

```python
# Python 2 vs Python 3

x = 0.2

x += 0.1

print(x)

print(repr(x))

print(str(x))
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/pitfalls/floats.py)

Bližší informace o formátu float/double:
[https://www.h-schmidt.net/FloatConverter/IEEE754.html](https://www.h-schmidt.net/FloatConverter/IEEE754.html)

```python
x = 0.1

while x != 10:
    x += 0.1
    print(x)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/pitfalls/endless_loop.py)

```python
numbers = [n for n in range(10)]

print(numbers)

for i in range(len(numbers)):
    print(i)
    if numbers[i] % 2 == 0:
        del numbers[i]

print(numbers)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/pitfalls/mutating_list.py)
