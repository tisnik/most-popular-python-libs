# Jazyk Python - základy programování


---

* Pavel Tišnovský
    - `kurzy.python@centrum.cz`
* Slajdy a demonstrační příklady:
    - https://github.com/tisnik/most-popular-python-libs
    - složka "courses"

![Python](images/python.png)

---

## Obsah kurzu (1/5)

* Úvod
    - proč a k čemu používat Python
    - srovnání s ostatními programovacími jazyky
* Základy jazyka
    - čísla a řetězce
    - řetězce Unicode
    - seznamy (pole)
    - n-tice
    - práce se slovníky

---

## Obsah kurzu (2/5)

* Řízení toku programu
    - základní konstrukce
    - funkce
    - příkazy
    - větvení
    - programové smyčky
    - složitější formy větvení
    - pattern matching

---

## Obsah kurzu (3/5)

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

---

## Obsah kurzu (4/5)

* Vstup a výstup
    – práce se soubory
    - souborové objekty
    - formátování výstupu
* Chyby a výjimky
    – přehled
    - vyvolání výjimky
    - obsluha výjimek
    - syntaktické chyby
    - složitější použití

---

## Obsah kurzu (5/5)

* Třídy
    – použitá terminologie
    - definování
    - objekty
    - dědičnost
    - speciální metody
* Iterátory, generátory
* Nejpoužívanější knihovny
* Užitečné nástroje pro Python
* Časté problémy

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

---

### Základní informace o jazyku Python

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

---

### Interpretry vs překladače

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

---

### Proč a k čemu používat programovací jazyk Python

* Zpracování dat
    - Pandas
* Moderní způsoby využití Pythonu
    - AI
    - Machine Learning (Deep Learning)
    - scikit-learn
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
* Jupyter Notebook
* Thonny
    - často používáno při výuce

---

### IDLE

* Pravděpodobně máte už nainstalováno
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
* Volitelné typové informace (type hints)
* Automatická správa paměti (garbage collector)
    - obsahuje většina moderních jazyků
* Objektově orientovaný jazyk
    - Java, C++, C#

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

---

### Implementace Pythonu

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

---

### Python 2.x vs Python 3.x

* Nejdůležitější rozdíly
    - `print`: příkaz vs funkce
    - celočíselné dělení (operátory / a //)
    - Unicode řetězce: nyní tři typy (str, byte, bytearray)
    - striktnější pravidla při porovnávání hodnot různých typů
    - `xrange()`: nyní se `range()` chová jako `xrange()`
    - argument při vyhazování výjimek musí být v závorkách

---

### Python 2.x vs Python 3.x

* Nejdůležitější rozdíly
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

---

## Základy programovacího jazyka Python

* Seznamy (pole)
* Slovníky
* Množiny
* N-tice

---

### Struktura zdrojového kódu

@ basic_structure.py

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
 
---

### Základní vstupně/výstupní funkce
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

### Struktura kódu v Pythonu

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

```python
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

### Funkce

* Změna stavu aplikace
* Jiné operace

@ function.py

---

### Parametry funkce a návratová hodnota

@ function_bmi.py

---

### Další způsoby předávání parametrů

@ args_kwargs.py

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

---

### Datové typy

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

---

### Měnitelné typy

* Měnitelné typy
    - seznamy
    - slovníky
    - množiny
    - pole bajtů (bytearray)
    - objekt

---

### Neměnitelné typy

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

---

### Čísla


* pozor na:
    - operátory se odlišují podle použitého typu
    - zápis komplexního čísla s "j" a nikoli s "i"
    - nekompatibilita u operátoru `/` (viz další slajdy s popisem operátorů)

---

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
* použito především u větvení a programových smyček

---

### Pravdivostní hodnoty

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

---

### Seznamy (pole)

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

---

### Množinové operace

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

---

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

---

### Výrazy, operátory: ukázky použití

* Celočíselné operace

@ expr_integers.py

---

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

---

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

---

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

---

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

### Pattern matching

---

### Konstrukce `if`

@ ackermann-if.py

---

### Konstrukce `if-else`

@ ackermann-if-else.py

---

### Konstrukce `match`

@ pattern-matching-ackermann.py

---

@ pattern-matching-fib.py

---

### Podmínka zapsaná v&nbsp;rozhodovacích větvích konstrukce `match`

* Nazývá se "guard"

---

@ pattern-matching-factorial1.py

---

@ pattern-matching-factorial2.py

---

@ pattern-matching-factorial3.py

---

@ pattern-matching-factorial4.py

---

### Programové smyčky

* Existují tyto druhy cyklů
    - nekonečný cyklus
    - cyklus `while-do` – cyklus s podmínkou na začátku
    - cyklus `do-while` – cyklus s podmínkou na konci
    - cyklus s podmínkou uprostřed
    - cyklus `for` - unifikované `while-do`
    - cyklus `for-each` - průchod sekvencemi

---

### Programové smyčky

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

---

### Varianta se smyčkou:

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

---

@ global.py

---

### Význam global/nonlocal

---

@ global_nonlocal_1.py

---

@ global_nonlocal_2.py

---

@ global_nonlocal_3.py

---

@ global_nonlocal_4.py

---

### Příklady funkcí

---

### Faktoriál

@ factorial1.py

---

### Faktoriál

@ factorial2.py

---

### Faktoriál

@ factorial3.py

---

### Fibonacci

@ fibonacci_for_loop.py

---

### Fibonacci

@ fibonacci_recursion.py

---

### Fibonacci

@ fibonacci_while_loop.py

---

### Fibonacci

@ fibonacci_while_loop_2.py

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

## Moduly

* Přehled
* Vyhledávání
* Pravidla a idiomy
* Funkce
* Balíčky

---

## Vstup a výstup

* Práce se soubory
* Souborové objekty
* Formátování výstupu

---

### Práce se soubory

* Základní funkce
    - `open`
    - `close`
    - `read`
    - `write`
    - `append`

---

### Souborové objekty

* Přečtení celého souboru

@ file_read_all.py

---

### Čtení po řádcích (1/2)

@ file_read_line.py

---

### Čtení po řádcích (2/2)

@ file_read_line_by_line.py

---

### Přečtení všech řádků do seznamu

@ file_read_all_lines.py

---

### Zápis do souboru

@ file_write.py

---

### Použití bloku `with`

@ file_read_with.py

@ file_read_line_by_line_with.py

---

### Formátování výstupu

* Metoda `string.format()`

* Příklad použiti

@ string_format_1.py

---

### Formátování tabulky na výstupu (1/3)

@ string_format_2.py

---

### Formátování tabulky na výstupu (2/3)

@ string_format_3.py

---

### Formátování tabulky na výstupu (3/3)

@ string_format_4.py

---

## Chyby a výjimky

* Přehled
* Vyvolání výjimky
* Obsluha výjimky
* Syntaktické chyby
* Blok `finally`

---

### Důvody vedoucí k zavedení výjimek

* Při běhu programu může dojít k různým chybovým (nebo jen neobvyklým)
    - ty je zapotřebí zpracovat
* Řešení v procedurálních jazycích
    - návratové kódy s číslem chyby (C standard library)
    - nastavení chybové proměnné (`errno`)
    - nověji se jedná o makro kvůli možnosti běhu vícevláknových aplikací

---

### Důvody vedoucí k zavedení výjimek

* Nevýhody využití návratových kódů
    - vlastní algoritmus je doplněn o množství nových podmínek
    - některé funkce musí vracet skutečné návratové hodnoty nepřímo - referencí
* Nevýhody využití proměnné errno
    - změna hodnoty proměnné při každém volání systémové funkce
    - taktéž vede k nutnosti použití množství nových podmínek v programu

---

### Důvody vedoucí k zavedení výjimek

* Výjimky
    - oddělení vlastního algoritmu od zpracování chybových stavů
    - standardizovaný postup

---

### Zachycení výjimky

@ try_catch_finally.py

---

### Vyvolání výjimky

@ raise_exception.py

---

### Vlastní výjimky

@ custom_exception.py

---

### Blok `finally`

* Provede se vždy
    - typicky uvolnění prostředků atd.

@ finally_block.py

---

## Třídy

* Použitá terminologie
* Definice třídy
* Atributy
* Metody
* Objekty
* Dědičnost
* Speciální metody

---

### Použitá terminologie

* Třída
    - data+funkce+(zapouzdření)
* Předek, potomek
* Objekt
    - instance třídy
* Metoda
* Atribut
    - objektu
    - třídní
* Konstruktor

---

### Definice třídy

@ class1.py

---

### Objekty

@ class2.py

---

### Atributy

* Datové položky
* Vytvářené explicitně pro každou instanci třídy
    - typicky v konstruktoru
* Přístup k atributům
    - interně přes `self`
    - externě pomocí "tečkové notace"
* Třídní/statický atribut
    - deklarován přímo ve třídě
    - sdílený všemi instancemi
    - přístup přes `JménoTřídy.jménoAtributu`
    - mohou být pojmenovány stejně jako atributy objektu

---

@ class3.py

---

### Konstruktor

* Zavolán při konstrukci objektu

@ class4.py

---

### Metody

* Funkce, které mají přístup k datovým položkám
    - přístup přes `self`
    - zavolání pomocí "tečkové notace"

@ class5.py

---

### Dědičnost

@ class6.py

---

### Speciální metody

* Seznam speciálních metod

```
__init__
__str__
__repr__
__hash__
__call__
__iter__
__getattr__
__getattribute__
__setattr__
__delattr__

__eq__  x, y    x == y
__ne__  x, y    x != y
__lt__  x, y    x < y
__gt__  x, y    x > y
__le__  x, y    x <= y
__ge__  x, y    x >= y
```

---

```
__add__         binární + operátor
__sub__         binární - operátor
__mul__         * operátor
__div__         / operátor
__floordiv__    // operátor (P2)
__truediv__     / operátor (P3)
__mod__         % operátor
__pow__         ** operátor or pow(x, y, z)
__neg__         unární - operátor
__pos__         unární + operátor
__abs__         absolutní hodnota
__nonzero__     konverze na Boolean
__invert__      ~ operátor
__lshift__      << operátor
__rshift__      >> operátor
__and__         & operátor
__or__  x, y    | operátor
__xor__         ^ operátor
```

---

```
__iadd__        += operátor
__isub__        -= operátor
__imul__        *= operátor
__idiv__        /= operátor (P2)
__ifloordiv__   //= operátor
__itruediv__    /= operátor (P3)
__imod__        %= operátor
__ipow__        **= operátor
__ilshift__     <<= operátor
__irshift__     >>= operátor
__iand__        &= operátor
__ior__         |= operátor
__ixor__        ^= operátor
```

---

* Konstrukce objektů, zavolání metod

@ class7.py

---

### Přetížení speciální metody \_\_str\_\_

@ class8.py

---

## Parametry zadávané na příkazovém řádku

@ args.py

---

## Další jednoduché třídy

---

### Dvojice hodnot

@ dvojice1.py

---

### Dvojice hodnot

@ dvojice2.py

---

### Komplexní čísla

@ complex1.py

---

### Komplexní čísla

@ complex2.py

---

### Komplexní čísla

@ complex3.py

---

### Komplexní čísla

@ complex4.py

---

### Komplexní čísla

@ complex5.py

---

## Moduly

* Standardní moduly
* Další užitečné moduly
* Způsob importu

---

## Standardní moduly (1/3)

* string
* re
* pprint
* math
* random
* decimal
* fractions

---

## Standardní moduly (2/3)

* collections
* itertools
* functools
* datetime
* time

---

## Standardní moduly (2/3)

* subprocess
* os
* io
* sys
* csv
* json
* pickle

---

## Další užitečné moduly

* requests
* cffi
* fastapi
* flask
* pil/pillow
* numpy
* scipy
* matplotlib
* scikit-learn

---

## Způsoby importu modulů

```
import datetime
import datetime as dt
from datetime import date
from datetime import *
```

---

## Instalace dalších balíčků

* pip
    - výchozí nástroj, většinou již nainstalován
* pdm
* poetry

---

## Použití debuggeru

```
python -m pdb test.py
pdb.set_trace()
```

## Post mortem debug

```
try:
    raise Exception()
except:
    import pdb
    pdb.post_mortem()
```

---

## MicroPython

* 2013, mikrořadič pyboard
* Dnes dostupný na více jednodeskových mikropočítačů
    - Micro Bit
    - Arduino
    - ESP32
    - ESP8255
    - PIC16...

---

## MicroPython

* Typické omezení
    - 256 kB ROM
    - 16 kB RAM
* Dva možné režimy činnosti
    - interpret přímo na CPU/MCU
    - překlad do hex/objektového kódu
* Repositář
    - https://github.com/micropython/micropython
    - překlad pro každý CPU/MCU zvlášť

---

## Rozdíly CPython vs MicroPython

* Chybí některé standardní knihovny
* Navíc přístup k hardware

```python
from machine import Pin
pin = Pin(0, Pin.IN)
print(pin.value())
```

```python
from machine import Pin
pin = Pin(14, Pin.OUT)
pin.value(1)
```

---

## MicroPython pro MicroBit

* MicroPython pro MicroBit
    - http://microbit.org/guide/python/
    - Online editor: http://python.microbit.org/v/1
    - převod zdrojového kódu do Intel hex formátu
    - upload v Intel hex formátu

---

## Užitečné nástroje pro Python (1/2)

* pydocstyle
    - testuje, zda jsou správně zapsány komentáře
* pycodestyle (pep8)
    - kontroluje styl zápisu programů
    - udržuje štábní kulturu
* pylint
    - ještě detailnější kontroly

---

## Užitečné nástroje pro Python (2/2)

* Ruff
    - dnes nejlepší nástroj pro kontrolu zdrojových kódů
* Mypy
    - test datových typů
* Pyright
    - dtto
* Black
    - formátovač zdrojových kódů

---

## Zvýšení výkonnosti aplikací psaných v Pythonu

* AOT překladače
* JIT překladače
* varianty "bez GIL"
* standardní CPython není ani AOT ani JIT

---

### AOT

* Ahead-Of-Time compilation
* Provedeno před spuštěním vlastní aplikace
* Bývá velmi agresivní
* Počáteční zdržení

---

### JIT

* Just-In-Time compilation
* Prováděno průběžně při běhu
* Ne tak důrazné optimalizace jako AOT
* Spekulativní optimalizace

---

### Python bez GIL

* Dokáže urychlit zejména vícevláknový programový kód

---

## Časté problémy

* V Pythonu najdeme určité problematické části jazyka
* Je vhodné o nich vědět a vyvarovat se některých konstrukcí

---

@ pitfalls/classes.py

---

@ pitfalls/default_argument_1.py

---

@ pitfalls/default_argument_2.py

---

@ pitfalls/scoping1.py

---

@ pitfalls/scoping2.py

---

@ pitfalls/scoping3.py

---

@ pitfalls/scoping4.py

---

@ pitfalls/closures.py

---

@ pitfalls/floats.py

Bližší informace o formátu float/double:
[https://www.h-schmidt.net/FloatConverter/IEEE754.html](https://www.h-schmidt.net/FloatConverter/IEEE754.html)

---

@ pitfalls/endless_loop.py

---

@ pitfalls/mutating_list.py

---

## Užitečné odkazy

* Python Quick Reference: http://rgruet.free.fr/#QuickRef
* Python docs: http://www.python.org/doc/
* PEP 8: http://www.python.org/dev/peps/pep-0008/
* pep8.py: http://pypi.python.org/pypi/pep8/
* pylint: http://www.logilab.org/project/pylint
* Epydoc: http://epydoc.sourceforge.net/
* Sphinx: http://sphinx-doc.org/
* Python in Python: http://pypy.org/
* The key differences between Python 2.7.x and Python 3.x with examples: http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html
* Language differences and workarounds: http://python3porting.com/differences.html
* Everything you did not want to know about Unicode in Python 3: http://lucumr.pocoo.org/2014/5/12/everything-about-unicode/
* Unicode (Wikipedia): https://en.wikipedia.org/wiki/Unicode
* Dive Into Python: http://www.diveintopython.net/
* Dive into Python 3: http://www.diveintopython3.net/

