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

```python
# int/long
print(42)
print(100000000000000000000000000000000000000000000000000000)

# float
print(3.1415)
print(1.2e10)
print(3e-3)
print(-3e-3)

# complex
print(2 + 3j)
print(1.5 + 2.8j)
print(1e10 + 3e-5j)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/numbers2.py)

---

### Pravdivostní hodnoty

* měnitelnost
    - neměnitelné
* datový typ
    - `bool`
* hodnoty
    - `True`
    - `False`
* použito především u větvení popř. u programových smyček
* podporované operátory
    - `and`
    - `or`
    - `not`

---

### Pravdivostní hodnoty

* jsou výsledkem aplikace dalších operátorů
    - `==`
    - `!=`
    - `<`
    - `<=`
    - `>`
    - `>=`
    - `is`
    - `is not`
    - `in`
    - `not in`

---

### Řetězce (raw, Unicode)

* měnitelnost
    - neměnitelné
* sekvence znaků
* původně sekvence bajtů
    - rozdíl - Unicode
* tzv. "raw" řetězce

---

### Řetězce (raw, Unicode)

```python
# běžný řetězec
print("Hello")

# bytové pole
print(b"abcdef")

# podpora pro Unicode
print(u"příliš žluťoučký kůň")

# řídicí znaky
print("abc\ndef")

# 'raw' řetězce
print(r"abc\ndef")

# víceřádkový řetězec
print("""A
B
C
D
E
F""")
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/strings.py)

---

### Funkce pro práci s řetězci

* `len` - vrací počet znaků řetězce

---

### Seznamy (pole)

* základní složený datový typ Pythonu
* měnitelnost
    - měnitelné
* homogenní datový typ
    - ne
* základní vlastnosti
    - do seznamu je možné přidávat nové prvky
    - prvky je možné i odstraňovat
    - k prvkům se přistupuje pomocí celočíselného indexu
    - záporný index - výběr prvků od konce seznamu
    - lze získat i podseznam (tzv. výsek seznamu)

---

### Funkce pro práci se seznamy

* `len` - vrací délku seznamu

---

### Metody pro práci se seznamy

* `clear`
* `append`
* `insert`
* `count`
* `reverse`
* `sort`

---

### Seznamy (pole) - ukázka

```python
seznam = [1, 2, 3, 4]

print(seznam[0])
print(seznam[1])
print(seznam[-1])
print(seznam[-2])

seznam.append(5)
seznam.append(6)

seznam.insert(0, -10)
seznam.insert(0, -100)

print(seznam)

del seznam[0]
print(seznam)

del seznam[-1]
print(seznam)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/list.py)

---

### Operace spojení seznamů

```python
seznam1 = [1, 2, 3]
seznam2 = [4, 5, 6]

seznam3 = seznam1 + seznam2

print(seznam3)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/list_append.py)

---

### Operace opakování seznamu

```python
seznam1 = [1, 2, 3]

seznam2 = seznam1 * 3
print(seznam2)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/list_repeat.py)

---

### Seřazení seznamu

* Dvě varianty
    - seřazení (změna) původního seznamu
    - vytvoření nového seřazeného seznamu

```python
seznam = [5, 4, 1, 3, 4, 100, -1]
print(seznam)

seznam.sort()
print(seznam)

seznam = [5, 4, 1, 3, 4, 100, -1]
print(seznam)

seznam2 = sorted(seznam)
print(seznam)
print(seznam2)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/list_sort.py)

---

### Vytvoření podseznamu


```python
seznam = [1, 2, 3, 4, 5, 6]

print(seznam[2:4])

print(seznam[0:6:2])

print(seznam[4:1])
print(seznam[4:1:-1])

print(seznam[4:])
print(seznam[:4])
print(seznam[:])
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/list_sublist.py)

---

### Slovníky

* základní složený datový typ Pythonu
* měnitelnost
    - měnitelné
* základní vlastnosti
    - dvojice klíč-hodnota
    - není zachováno pořadí dvojic!
    - klíč slouží pro výběr hodnoty
    - do slovníků lze přidávat nové prvky
    - ze slovníku lze prvek vymazat pomocí `del`

---

### Slovníky - ukázka

```python
d = {"id": 1,
     "name": "Eda",
     "surname": "Wasserfall"}

print(d)

print(d["name"])

d["hra"] = "Svestka"

print(d)

del d["id"]

print(d)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/dict.py)

---

### Množiny

* měnitelnost
    - měnitelné
* homogenní datový typ
    - ne
* základní vlastnosti
    - každý prvek je unikátní
    - prvky by neměly být měnitelné (jinak nelze zaručit unikátnost)
    - do množiny je možné prvky přidávat
    - prvky lze i odstraňovat

---

### Funkce pro práci s množinami

* `len` - vrací počet prvků množiny

---


### Množiny

```python
s = {1, 2, 3, 4}
print(s)

s2 = {"hello", "world", "!", 0}
print(s2)

s3 = set()
print(s3)

s3.add(1)
s3.add(2)
print(s3)

s3.update([3, 4, 5])
print(s3)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/sets.py)

---

### Operace `discard` a `remove`

```python
s1 = {1,2,3,4}
print(s1)

s1.discard(2)
print(s1)

s1.discard(1000)
print(s1)

s1.remove(3)
print(s1)

s1.remove(1000)
print(s1)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/sets_discard_remove.py)

---

### Množinové operace

* `x in s`
    -test na existenci prvku v množině
* `x not in s`
    - opačný test
* `s <= t`
    - test na relaci "je podmnožinou"
* `s >= t`
    - test na relaci "je nadmnožinou"
* `s | t`
    - sjednocení množin
* `s & t`
    - průnik množin
* `s - t`
    - rozdíl množin
* `s ^ t`
    - symetrická diference

---

### Množinové operace - příklad použití

```python
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

print(s1)
print(s2)

print(s1 | s2)
print(s1 & s2)
print(s1 - s2)
print(s2 - s1)
print(s1 ^ s2)

print(1 in s1)
print(10 in s1)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/sets_operations.py)

---

### Zápis množinových operací metodami

* Shodný význam s příslušnými operátory
    - (dodržení štábní kultury)

```python
s.issubset(t)
s.issuperset(t)
s.union(t)
s.intersection(t)
s.difference(t)
s.symmetric_difference(t)
```

---

### Množinové operace - příklad použití

* (převzato přímo z dokumentace Pythonu)

```python
engineers = {'John', 'Jane', 'Jack', 'Janice'}
programmers = {'Jack', 'Sam', 'Susan', 'Janice'}
managers = {'Jane', 'Jack', 'Susan', 'Zack'}

employees = engineers | programmers | managers
engineering_management = engineers & managers
fulltime_management = managers - engineers - programmers

print(engineers)
print(programmers)
print(managers)
print(employees)
print(engineering_management)
print(fulltime_management)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/sets_example.py)

---

### N-tice

* další základní složený datový typ Pythonu
* měnitelnost
    - neměnitelné
* homogenní datový typ
    - ne
* částečně se podobají seznamům
    - ovšem kvůli neměnitelnosti mají jiné použití
    - paměťová efektivita

---

```python
# tříprvková n-tice
t1 = (1, 2, 3)

# jednoprvková n-tice
t2 = (4, )

# pozor - není tuple!
t3 = (5)

# nehomogenní n-tice
t4 = (4, 3.14, "string", [])

# prázdná n-tice
t5 = ()

print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/tuple.py)

---

### Spojení n-tic operátorem `+`

```python
x = (1, 2, 3)
y = (3, 4, 5)

print(x + y)
print(y + x)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/tuple_join.py)


### Test na existenci prvku v n-tici

```python
x = (1, 2, 3)
y = (3, 4, 5)
z = x + y

print(1 in z)
print(10 in z)
print("foobar" in z)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/tuple_exists.py)

---

### Výrazy, operátory

* aritmetické operátory
    - `+`
    - `-`
    - `*`
    - `/`
    - `//`
    - `%`
    - `**`

---

### Výrazy, operátory

* porovnávání
    - `==`
    - `!=`
    - `<>` (jen v Pythonu 2.x, nyní již není podporován)
    - `>`
    - `<`
    - `>=`
    - `<=`

---

### Výrazy, operátory

* logické operátory
    - `and`
    - `or`
    - `not`

---

### Výrazy, operátory

* bitové operátory
    - `&`
    - `|`
    - `^`
    - `~`
    - `<<`
    - `>>`

---

### Výrazy, operátory

* přiřazení
    - `=`
    - `+=`
    - `-=`
    - `*=`
    - `/=`
    - `%=`
    - `**=`
    - `//=`

---

### Výrazy, operátory

* další operátory
    - `in`
    - `not in`
    - `is`
    - `is not`

---

### Rozhodovací konstrukce ve výrazu

```python
x = 1 if y > 10 else 0
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/expr_if_else.py)

### Výrazy, operátory: ukázky použití

* Celočíselné operace

```python
x = 10
y = 3

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)
print(x ** y)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/expr_integers.py)

* Výsledky pro Python 2.x

```
13
7
30
3
3
1
1000

```

* Výsledky pro Python 3.x

```
13
7
30
3.3333333333333335
3
1
1000
```

---

### Výrazy, operátory: ukázky použití

* Operace s typem `float/double`

```python
x = 10.0
y = 3

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)
print(x ** y)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/expr_floats.py)

---

* Výsledky pro Python 2.x

```
13.0
7.0
30.0
3.33333333333
3.0
1.0
1000.0
```

* Výsledky pro Python 3.x

```
13.0
7.0
30.0
3.3333333333333335
3.0
1.0
1000.0
```

---

### Priority operátorů

* Tabulka se třinácti prioritami
    - není nutné si pamatovat, lze používat závorky

```
1       **
2       ~ + -
3       * / % //
4       + -
5       >> <<
6       &
7       ^ |
8       <= < > >=
9       <> == !=
10      = %= /= //= -= += *= **=
11      is   is not
12      in   not in
13      not or and
```

---

### Celočíselné dělení

* Nekompatibilita mezi Pythonem 2.x a Pythonem 3.x

```python
print '3 / 2 =', 3 / 2
print '3 // 2 =', 3 // 2
print '3 / 2.0 =', 3 / 2.0
print '3 // 2.0 =', 3 // 2.0
```

* Výsledky pro Python 2:

```
3 / 2 = 1
3 // 2 = 1
3 / 2.0 = 1.5
3 // 2.0 = 1.0
```

```python
print('3 / 2 =', 3 / 2)
print('3 // 2 =', 3 // 2)
print('3 / 2.0 =', 3 / 2.0)
print('3 // 2.0 =', 3 // 2.0)
```

* Výsledky pro Python 3:

```
3 / 2 = 1.5
3 // 2 = 1
3 / 2.0 = 1.5
3 // 2.0 = 1.0
```

---

## Řízení toku programu

* Základní pojmy
* Větvení (rozhodovací konstrukce)
* Složitější formy větvení
* Programové smyčky

---

### Základní pojmy

* Řídicí struktura
    - též strukturovaný příkaz
    - control flow statement
* Tři druhy struktur programu:
    - prostá posloupnost příkazů
    - větvení (podmíněný příkaz)
    - cyklus (programová smyčka)

---

### Větvení (rozhodovací konstrukce)

* Základní forma:

```python
if condition1:
    pass
```

* Viz příklad s výpočtem BMI

```python
print("Mass (kg): ")
mass = int(input())

if mass < 0:
    print("Invalid input")
    sys.exit(1)
```

---

### Složitější formy větvení

* Tzv. plné větvení

```python
if condition1:
    pass
else:
    pass
```

---

### Složitější formy větvení

* Nahrazuje konstrukci typu `switch-case`

```python
if condition1:
    pass
elif condition2:
    pass
elif condition3:
    pass
else:
    pass
```

---

### Programové smyčky

* Existují tyto druhy cyklů
    - nekonečný cyklus
    - cyklus `while-do` – cyklus s podmínkou na začátku
    - cyklus `do-while` – cyklus s podmínkou na konci
    - cyklus s podmínkou uprostřed
    - cyklus `for` - unifikované `while-do`
    - cyklus `for-each` - průchod sekvencemi

* V Pythonu
    - cyklus `while-do` – (zahrnuje i nekonečný cyklus)
    - cyklus `for-each` - průchod sekvencemi
    - příkazy `break` a `continue` pro další varianty

---

### Programová smyčka `while`

```python
x = 1

while x < 2000:
    print(x)
    x *= 2
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/while1.py)

---

### Programová smyčka `for`

```python
list = ["one", "two", "three", "four"]

for item in list:
    print(item)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/for1.py)

---

### Typická podoba `for`

* Náhrada smyčky s počitadlem známá z jiných programovacích jazyků

```python
for i in range(10):
    print(i)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/for_range.py)
---

* Použití kroku

```python
for i in range(4, 11, 2):
    print(i)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/for_range_step.py)

* Počítání směrem dolů

```python
for i in range(10, 0, -1):
    print(i)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/for_range_step_down.py)
---

### Konstrukce `break`

```python
x = 1

while True:
    print(x)
    if x > 1000:
        break
    x *= 2
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/break.py)

---

### Konstrukce `continue`

```python
x = 1

while True:
    if x > 1000:
        break
    x *= 2
    if x < 100:
        continue
    print(x)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/continue.py)

---

## Procedury a funkce

* Základní pojmy
* Příklady použití
* Rekurzivní funkce
* Definice funkcí
* Oblast platnosti proměnných
* Použití globálních proměnných

---

### Základní pojmy

* Čisté funkce
    - referenční transparentnost
* Funkce s vedlejším efektem
    - imperativní funkce
* Funkce vyššího řádu
* Anonymní funkce
* Rekurze

---

### Příklady použití

* Dělení programu na menší izolované celky
    - koncept "rozděl a panuj"
    - snadnější ladění
    - snadnější testování
    - zmenšení cyklomatické komplexity

---

### Běžná funkce

```python
def compute_bmi(mass, height):
    height = height / 100.0
    bmi = mass / (height * height)
    return bmi
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/function.py)

---

### Rekurzivní funkce

```python
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)


print(factorial(10))

for n in range(1, 11):
    print(n, factorial(n))
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/recursive.py)

* Varianta se smyčkou:

```python
def factorial(n):
    """Výpočet faktoriálu ve smyčce."""
    f = 1
    for x in range(1, n + 1):
        f *= x
    return f
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/factorial.py)

---

### Složitější rekurzivní funkce

* Příkaz `return` může být v kódu umístěn kdekoli

```python
calls = 0

def ackermann(m, n):
    global calls
    calls += 1
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

print(ackermann(3,4))
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/ackermann.py)

---

### Definice funkcí

* Běžné poziční parametry

```python
def fn1(arg1, arg2, arg3):
    pass
```

* Parametry s výchozí hodnotou

```python
def fn2(arg1, arg2, arg3=True):
    pass
```

---

### Definice funkcí

* Proměnný počet parametrů
    - uloží se do n-tice

```python
def fn3(arg1, arg2, *args):
    pass
```

* Parametry se jménem specifikovaným při volání funkce
    - uloží se do slovníku

```python
def fn4(arg1, arg2, **kwargs):
    pass
```

---

### Oblast platnosti proměnných

* Globální proměnné
* Uvnitř funkcí
    - čtení vs. přiřazení (zápis)
    - klíčové slovo `global`
    - klíčové slovo `nonlocal`

```python
x = 1

def fn1():
    pass


def fn2():
    x = 2


def fn3():
    global x
    x = 3


print(x)
fn1()
print(x)
fn2()
print(x)
fn3()
print(x)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/global.py)

### Význam global/nonlocal

```python
x = 0

def fn1():
    x = 1
    def fn2():
        x = 2
        print(x)
    fn2()
    print(x)


print(x)
fn1()
print(x)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/global_nonlocal_1.py)

```python
x = 0

def fn1():
    x = 1
    def fn2():
        nonlocal x
        x = 2
        print(x)
    fn2()
    print(x)


print(x)
fn1()
print(x)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/global_nonlocal_2.py)

```python
x = 0

def fn1():
    x = 1
    def fn2():
        global x
        x = 2
        print(x)
    fn2()
    print(x)


print(x)
fn1()
print(x)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/global_nonlocal_3.py)

```python
x = 0

def fn1():
    global x
    x = 1
    def fn2():
        global x
        x = 2
        print(x)
    fn2()
    print(x)


print(x)
fn1()
print(x)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/global_nonlocal_4.py)

---

## Funkcionální prvky jazyka

* Lambda výrazy
* Generátorová notace seznamu
* Funkce vyššího řádu

---

### Lambda výrazy

```python
f = lambda x, y : x + y
print(f(1,2))
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/lambda.py)

---

### Generátorová notace seznamu

* List comprehension

```python
seznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

seznam2 = [item*2 for item in seznam]

seznam3 = [item for item in seznam if item % 3 == 0]

print(seznam)
print(seznam2)
print(seznam3)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/list_comprehension.py)

---

### Funkce vyššího řádu

* Akceptují jako svůj parametr jinou funkci
* A/nebo vrací novou funkci jako svůj výsledek

* Funkce `map`

```python
x = range(10)

print(x)

y=map(lambda value: value*2, x)
print(list(y))
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/map.py)

---

### Funkce vyššího řádu

* Funkce `filter`

```python
x = range(20)

print(x)

y = filter(lambda value: value % 3 == 0, x)
print(list(y))
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/filter.py)

---

### Funkce vyššího řádu

* Funkce `reduce`
    - musí být importována z balíčku `functools`

```python
from functools import reduce

x = range(1, 11)

print(x)

y = reduce(lambda a, b: a*b, x)
print(y)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/python1/examples/reduce.py)




---

## Časté problémy

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
