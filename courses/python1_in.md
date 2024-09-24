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

@ range.py

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

@ bmi.py

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

@ bmi_2.py

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

@ variables.py

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

@ numbers1.py

* pozor na:
    - operátory se odlišují podle použitého typu
    - zápis komplexního čísla s "j" a nikoli s "i"
    - nekompatibilita u operátoru `/` (viz další slajdy s popisem operátorů)

@ numbers2.py

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

@ strings.py

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

@ list.py

---

### Operace spojení seznamů

@ list_append.py

---

### Operace opakování seznamu

@ list_repeat.py

---

### Seřazení seznamu

* Dvě varianty
    - seřazení (změna) původního seznamu
    - vytvoření nového seřazeného seznamu

@ list_sort.py

---

### Vytvoření podseznamu


@ list_sublist.py

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

@ dict.py

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

@ sets.py

---

### Operace `discard` a `remove`

@ sets_discard_remove.py

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

@ sets_operations.py

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

@ sets_example.py

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

@ tuple.py

---

### Spojení n-tic operátorem `+`

@ tuple_join.py


### Test na existenci prvku v n-tici

@ tuple_exists.py

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

@ expr_if_else.py

### Výrazy, operátory: ukázky použití

* Celočíselné operace

@ expr_integers.py

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

@ expr_floats.py

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

@ while1.py

---

### Programová smyčka `for`

@ for1.py

---

### Typická podoba `for`

* Náhrada smyčky s počitadlem známá z jiných programovacích jazyků

@ for_range.py
---

* Použití kroku

@ for_range_step.py

* Počítání směrem dolů

@ for_range_step_down.py
---

### Konstrukce `break`

@ break.py

---

### Konstrukce `continue`

@ continue.py

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

@ function.py

---

### Rekurzivní funkce

@ recursive.py

* Varianta se smyčkou:

@ factorial.py

---

### Složitější rekurzivní funkce

* Příkaz `return` může být v kódu umístěn kdekoli

@ ackermann.py

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

@ global.py

### Význam global/nonlocal

@ global_nonlocal_1.py

@ global_nonlocal_2.py

@ global_nonlocal_3.py

@ global_nonlocal_4.py

---

## Funkcionální prvky jazyka

* Lambda výrazy
* Generátorová notace seznamu
* Funkce vyššího řádu

---

### Lambda výrazy

@ lambda.py

---

### Generátorová notace seznamu

* List comprehension

@ list_comprehension.py

---

### Funkce vyššího řádu

* Akceptují jako svůj parametr jinou funkci
* A/nebo vrací novou funkci jako svůj výsledek

* Funkce `map`

@ map.py

---

### Funkce vyššího řádu

* Funkce `filter`

@ filter.py

---

### Funkce vyššího řádu

* Funkce `reduce`
    - musí být importována z balíčku `functools`

@ reduce.py




---

## Časté problémy

@ pitfalls/classes.py

@ pitfalls/default_argument_1.py

@ pitfalls/default_argument_2.py

@ pitfalls/scoping1.py

@ pitfalls/scoping2.py

@ pitfalls/scoping3.py

@ pitfalls/scoping4.py

@ pitfalls/closures.py

@ pitfalls/floats.py

Bližší informace o formátu float/double:
[https://www.h-schmidt.net/FloatConverter/IEEE754.html](https://www.h-schmidt.net/FloatConverter/IEEE754.html)

@ pitfalls/endless_loop.py

@ pitfalls/mutating_list.py
