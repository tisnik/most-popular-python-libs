# Evoluce Pythonu

---

![Python](images/python.png)

---

## Obsah kurzu

* Nové vlastnosti jazyka
* Novinky v ekosystému Pythonu
* Vylepšení výkonnosti Pythonu
* Python a vývoj webových aplikací
* Alternativní projekty a jazyky
* Testování aplikací v Pythonu

---

## Obsah kurzu
### Nové vlastnosti jazyka

* Formátovací řetězce
* Pouze poziční parametry funkcí
* Pattern matching
* "Mroží" operátor
* Podpora pro asynchronní programování
* Skupiny výjimek
* Deklarace datových typů
* Statická typová kontrola

---

## Obsah kurzu
### Novinky v ekosystému Pythonu

* Správa projektů
* Lintery

---

## Obsah kurzu
### Vylepšení výkonnosti Pythonu

* Výkonnější CPython
* Problém související s GILem
* JIT překlad

---

## Obsah kurzu
### Python a vývoj webových aplikací

* Brython
* Transcrypt
* PyScript
* Bokeh

---

## Obsah kurzu
### Alternativní projekty a jazyky

* Coconut
* Mojo

---

## Obsah kurzu
### Testování aplikací v Pythonu

* Jednotkové testy
* Zjištění pokrytí kódu testy
* Testy chování (BDD)
* Nástroj Hypothesis
* Fuzzy testy

---

# Nové vlastnosti jazyka

![Python](images/python.png)

---

## Nové vlastnosti jazyka

* Formátovací řetězce
* Pouze poziční parametry funkcí
* Pattern matching
* "Mroží" operátor
* Podpora pro asynchronní programování
* Skupiny výjimek
* Deklarace datových typů
* Statická typová kontrola

---

## Postupné rozšiřování možností Pythonu

```
Python 3.6    f-řetězce, async-IO
Python 3.7    klíčová slova async a await
Python 3.8    mroží operátor, poziční parametry
Python 3.9    generické typy
Python 3.10   pattern matching
Python 3.11   skupiny výjimek
Python 3.12   klíčové slovo type + sémantika
```

---

## Formátovací řetězce

* Přidáno do Pythonu 3.6
* Lze využít společně s původním formátováním
* Prefix `f""`
    - proto se nazývají f-strings

---

### Ukázka použití f-řetězců

* "Interpolace" proměnných

@ f-string-1.py

---

### Výrazy v f-řetězci

* V řetězci lze použít i výrazy

@ f-string-2.py

---

### Podmínka ve výrazu

* Ne vždy plně čitelné, ale pro jednoduché šablony ano

@ f-string-3.py

---

### Volání funkce v f-řetězci

@ f-string-4.py

---

### Volání metody v f-řetězci

@ f-string-5.py

---

### Jednodušší ladění

@ f-string-6.py

Výsledek:

```
name='Guido' surname='Rossum'
```

---

## Poziční parametry funkcí

* Přidáno do Pythonu 3.8
* Umožňují rozlišit funkce s parametry zapisovanými jen pozičně
* Ostatní parametry buď pozičně nebo je lze pojmenovat

---

### Poziční parametry funkcí

* Běžně deklarovaná funkce

@ positional-params-1.py

---

### Poziční parametry funkcí

* Parametry lze pojmenovat a předat v jiném pořadí

@ positional-params-2.py

---

### Poziční parametry funkcí

* Všechny parametry jsou čistě poziční

@ positional-params-3.py

---

### Poziční parametry funkcí

* První parametr je čistě poziční

@ positional-params-4.py

---

### Poziční parametry funkcí

* Kombinace s pojmenovanými parametry

@ positional-params-5.py

---

## Pattern matching

* Přidáno do Pythonu 3.10
* Lepší varianta konstrukce `switch-case`

---

### Inspirováno dalšími programovacími jazyky

* SNOBOL
* AWK
* ML (Caml, OCaml, F#)
* Rust
* Coconut (překládáno do Pythonu)

---

### Částečně flexibilní řešení

* Ne všechny vzory je možné použít
    - například `"literal" + x + "literal"`
    - možná se jejich podpora objeví v další verzi Pythonu?

---

### Ukázky pattern matchingu

---

### Klasické řešení problému bez pattern matchingu

@ pattern-matching-abort-retry-fail-1.py

---

### Použití mapy (slovníku)

@ pattern-matching-abort-retry-fail-2.py

---

### Řídicí struktura match-case

@ pattern-matching-abort-retry-fail-3.py

---

### Množiny pro větší množství vstupů

@ pattern-matching-abort-retry-fail-4.py

---

### Spojka `or` ve vzoru

@ pattern-matching-abort-retry-fail-5.py

---

### Zachycení hodnoty ve vzoru

@ pattern-matching-abort-retry-fail-6.py

---

### Zachycení hodnoty ve vzoru

@ pattern-matching-abort-retry-fail-7.py

---

### Generátor Fibonaccího posloupnosti

@ pattern-matching-fib.py

---

### Výpočet faktoriálu - základní varianta

@ pattern-matching-factorial1.py

---

### Podmínka ve větvi

@ pattern-matching-factorial2.py

---

### Test typu

@ pattern-matching-factorial3.py

---

### Větev "or"

@ pattern-matching-factorial4.py

---

### Vzorek s n-ticí

@ pattern-matching-complex1.py

---

### Vzorek s n-ticí a s podmínkou

@ pattern-matching-complex2.py

---

### Příkazy složené z většího množství slov

@ pattern-matching-multiword-commands-1.py

---

### Vzorek a seznamy

@ pattern-matching-multiword-commands-2.py

---

### Zachycení hodnoty

@ pattern-matching-multiword-commands-3.py

---

### Vnořená konstrukce `match-case`

@ pattern-matching-multiword-commands-4.py

---

### Vnořená konstrukce `match-case` + množiny ve vzorku

@ pattern-matching-multiword-commands-5.py

---

### Vzorky a OOP

@ pattern-matching-object1.py

---

### Vzorky a OOP

@ pattern-matching-object2.py

---

## Mroží operátor

* Přidáno do Pythonu 3.8
* PEP 572 - Assignment Expressions
* Možnost přiřazení v rámci `výrazu`
    - původní přiřazení lze jen v rámci `příkazu`
* Takzvané `pojmenované výrazy`

---

### Proměnná definovaná v podmínce

@ walrus-operator-1.py

---

### Dtto, ale opačný výsledek

@ walrus-operator-2.py

---

### Problém: opakované výpočty

@ walrus-operator-3.py

---

### Předpočet hodnot

@ walrus-operator-4.py

---

### Úprava založená na walrus operátoru

@ walrus-operator-5.py

---

## Podpora pro asynchronní programování

* Postupně přidáno v Pythonu 3.6 a 3.7
* Nová klíčová slova `async` a `await`

---

### Souběžnost a paralelismus

* Nejedná se o tytéž vlastnosti
* Souběžnost
    - více úloh běžících na menším množství CPU
    - i na jednom CPU
    - překrývání
* Paralelismus
    - n úloh na n CPU

---

### Souběžnost a paralelismus v Pythonu

* Více procesů
    - `multiprocessing`
* Více vláken
    - `threading`
* Korutiny
    - `asyncio`

---

### `async` a `await`

* Nejenom v Pythonu
    - populární i v dalších jazycích
* Typicky pro I/O operace
* Funkce označené `async`
* Čekání na dokončení pomocí `await`

---

### `async` a `await`

* Nekorektní použití `await`

@ async-await-1.py

---

### `async` a `await`

* Korektní použití `await`

@ async-await-2.py

---

### Dvě souběžné úlohy

@ async-await-3.py

---

### Tři souběžné úlohy, čtení výsledné hodnoty

@ async-await-4.py

---

### Komunikace přes fronty

@ async-queue-1.py

---

### Čtení výsledků přes frontu

* Synchronizace

@ async-queue-2.py

---

### Producent-konzument

* Běžící asynchronně

@ async-queue-3.py

---

### Prioritní fronta

@ priority-queue.py

---

### `aiohttp`

@ aiohttp1.py

---

### `aiohttp`

@ aiohttp2.py

---

## Skupiny výjimek

* Přidáno do Pythonu 3.11
* PEP 654 – Exception Groups and except

---

### Vyhození skupiny výjimek

@ exception-group-1.py

---

### Vyhození skupiny výjimek

@ exception-group-2.py

---

## Deklarace datových typů

* Přidáváno postupně
* PEP 484 - Type Hints a další

---

### Nejpopulárnější jazyky současnosti

```
Dynamicky typované   Staticky typované
--------------------------------------
Python               C
JavaScript           C++
Ruby                 Go
Perl                 Rust
Matlab               Java
PHP                  Scala
```

---

### Přednosti dynamicky typovaných jazyků

* Rychlý cyklus vývoje
    - edit-(compile)-run
* Velmi snadné pro začátečníky
* Ideální pro skriptování
    - CLI
    - skripty na webových stránkách

---

### Zápory dynamicky typovaných jazyků

* Zaručení korektnosti rozsáhlých projektů
* Většinou se vyžaduje větší množství jednotkových testů
    - code coverage není dobrou metrikou!
* Informace o typech se někdy zapisují do komentářů
* IDE nemusí vždy nabízet správné funkce/metody/opravy

---

## To nejlepší z obou světů?

* Volitelné typy

```
Jazyk          Technologie pro statické typy
--------------------------------------------
JavaScript     TypeScript, Flow
Python         Mypy, Pyright, Pyre
Ruby           Sorbet
```

---

### Volitelné typy a Python

* Python je dynamicky typovaný
    - a nejsou plány to změnit!
* Typy jsou čistě volitelné
    - přidáno do Pythonu 3.5
    - nazvané "type hints"
    - (aby to vývojáře nestrašilo)
* Statické typové kontroly
    - mypy, pyright, pyre

---

### Statická typová kontrola a Mypy

---

![Mypy logo](images/mypy.png)

---

@ mypy-add-1.py

* Typ `Any` je přidán automaticky

---

### Typové anotace

* specifikují se za dvojtečkou

@ mypy-add-2.py

---

### `bool` nebo `int`?

* Viz specifikace Pythonu!

@ mypy-add-3.py
@ mypy-add-4.py

---

### Výpis typových anotací

* `any`

@ mypy-add-5.py

* explicitní typy

@ mypy-add-6.py


---

### Výpis typových anotací

* složitější typy

@ mypy-add-7.py

---

### Typované n-tice

* nekorektní varianta

@ mypy-tuple-type-1.py

* korektní varianta

@ mypy-tuple-type-2.py

---

### Rozdílné typy prvků

* nekorektní varianta

@ mypy-tuple-type-3.py

* korektní varianta

@ mypy-tuple-type-4.py

---

### Typované seznamy

* nekorektní varianta

@ mypy-list-type-1.py

* import

@ mypy-list-type-2.py

---

### Test typu prvků

* v pořádku

@ mypy-list-type-3.py

* nekorektní

@ mypy-list-type-4.py

---

### Znovu problém bool-int

* v pořádku

@ mypy-list-type-5.py

* nekorektní

@ mypy-list-type-6.py

---

### Typované slovníky

* Slovníky v Pythonu

@ mypy-dict-type-1.py

* Libovolné klíče a hodnoty

@ mypy-dict-type-2.py

---

### Specifikace typu slovníku

* použití typu `any`

@ mypy-dict-type-3.py

---

### Specifikace typu slovníku

* explicitní specifikace

@ mypy-dict-type-4.py

---

### Typ `union`

* Pro hodnoty

@ mypy-dict-type-5.py

---

### Typ `union`

* Pro klíče

@ mypy-dict-type-6.py

---

### Typ `optional`

* Bez `optional`

@ mypy-dict-type-7.py

---

### Typ `optional`

* S `optional`

@ mypy-dict-type-8.py

---

### Typy a funkce vyššího řádu

* typ `callable`

@ mypy-callable.py

---

### Problém s variancí

* Týká se podtypů a nadřazených typů
    - v OOP běžné
* Čtyři možné typy variance
    - kovariance
    - kontravariance
    - invariance
    - bivariance

---

### Příklad variancí

* `Jablko` je podtypem typu `Ovoce` ve všech dalších případech

---

### Příklad variancí

* Covariance
    - `List[Apple]` je podtypem `List[Fruit]`
* Contravariance
    - `List[Fruit]` je podtypem `List[Apple]`
* Invariance
    - `List[Fruit]` nemá žádný vztah k `List[Apple]`
* Bivariance
    - `List[Apple]` je podtypem `List[Fruit]`
    - a současně (!!!):
    - `List[Fruit]` je podtypem `List[Apple]`

---

### Proč se o varianci vůbec starat?

* Úzce souvisí s typovým systémem
* A s tím, jaké kontroly lze provést staticky

---

```java
class Fruit {
}

class Orange extends Fruit {
    public String toString() {
        return "Orange";
    }
}

class Apple extends Fruit {
    public String toString() {
        return "Apple";
    }
}

public class Variance1 {
    public static void mix(Fruit[] punnet) {
        punnet[0] = new Orange();
        punnet[1] = new Apple();
    }

    public static void main(String[] args) {
        Fruit[] punnet = new Fruit[2];
        mix(punnet);

        for (Fruit Fruit:punnet) {
            System.out.println(Fruit);
        }
    }
}
```

---

### Statická kontrola typů ok, pád v runtime!

```java
class Fruit {
}

class Orange extends Fruit {
    public String toString() {
        return "Orange";
    }
}

class Apple extends Fruit {
    public String toString() {
        return "Apple";
    }
}

public class Variance2 {
    public static void mix(Fruit[] punnet) {
        punnet[0] = new Orange();
        punnet[1] = new Apple();
    }

    public static void main(String[] args) {
        Fruit[] punnet = new Orange[2];
        mix(punnet);

        for (Fruit Fruit:punnet) {
            System.out.println(Fruit);
        }
    }
}
```

---

### Variance v Pythonu

@ mypy-variance-1.py

---

### Použití `sequence` a nikoli seznamu

@ mypy-variance-2.py

---

### Tisk typové anotace

@ mypy-variance-3.py

---

# Novinky v ekosystému Pythonu

![Python](images/python.png)

---

## Novinky v ekosystému Pythonu

* Správa projektů
* Lintery

---

# Vylepšení výkonnosti Pythonu

![Python](images/python.png)

---

## Vylepšení výkonnosti Pythonu

* Výkonnější CPython
* Problém související s GILem
* JIT překlad

---

## Výkonnější CPython

---

## Problém související s GILem

---

## JIT překlad

* Just-in-time (JIT)
* Ahead-of-time (AOT)
* Několik projektů nabízejících JIT/AOT

---

# Python a vývoj webových aplikací

![Python](images/python.png)

---

## Python a vývoj webových aplikací

* Brython
* Transcrypt
* PyScript
* Bokeh

---

# Alternativní projekty a jazyky

![Python](images/python.png)

---

## Alterntivní projekty a jazyky

* Coconut
* Mojo

---

# Testování

![Python](images/python.png)

* Základní technologie testování
* Pyramida testů
* Zmrzlinový kornout jako antipattern
* Jednotkové testy
* Modul `pytest`
* Nástroj Hypothesis
* Fuzzy testy

---

### Testovací frameworky v Pythonu

```
1                   unittest
2                   doctest
3                   pytest
4                   nose
5                   testify
6                   Trial
7                   Twisted
8                   subunit
9                   testresources
10                  reahl.tofu
11                  unit testing
12                  testtools
13                  Sancho
14                  zope.testing
15                  pry
16                  pythoscope
17                  testlib
18                  pytest
19                  dutest
```

---

### Pyramida typů testů

* Business část
    - Beta testy
    - Alfa testy
    - Akceptační testy
* Technologická část
    - UI testy
    - API testy
    - Integrační testy
    - Testy komponent
    - Unit testy
* Další typy testů
    - Benchmarky

---

