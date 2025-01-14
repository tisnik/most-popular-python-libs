# Typové informace v&nbsp;Pythonu

---

* Pavel Tišnovský
* kurzy.python@centrum.cz

---

![Python](images/python.png)

---

## Postupné rozšiřování možností Pythonu

* Sémantika
* (Syntaxe)

---

## Nová syntaxe+sémantika v Pythonu 3.x

```
Python 3.5    typové informace
Python 3.6    f-řetězce, async-IO
Python 3.7    klíčová slova async a await
Python 3.8    mroží operátor, poziční parametry
Python 3.9    generické typy
Python 3.10   pattern matching
Python 3.11   skupiny výjimek
Python 3.12   klíčové slovo type + sémantika
```

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

### Základní základy

@ variable-1.py
@ variable-2.py

---

@ variable-3.py
@ variable-4.py

---

* Typ `Any` je přidán automaticky

@ adder-1.py

---

* Proč `Any`?

@ adder-2.py

---

### Typové anotace

* specifikují se za dvojtečkou

@ adder-3.py

---

### Typové anotace

* využití

@ adder-4.py

---

### `bool` nebo `int`?

* Viz specifikaci Pythonu!

```
assert True+True==2
```

---

### `bool` nebo `int`?

@ adder-5.py

---

### `bool` nebo `int`?

@ adder-6.py

---

### Výpis typových anotací

* `any`

```python
def add(a, b):
    return a+b


print(add.__annotations__)
```

* explicitní typy

```python
def add(a:int, b:int) -> int:
    return a+b


print(add.__annotations__)
```

---

### Typ `Union`

@ adder-7.py

---

### Typ `Union`

@ adder-8.py

---

### Dekorátor `@overload`

@ adder-9.py

---

### Dekorátor `@overload`

@ adder-A.py

---

### Typ `Optional`

@ optional-1.py
@ optional-2.py

---

### Typované n-tice

* nekorektní varianta

@ tuple-type-1.py

@ tuple-type-1B.py

---

### Typované n-tice

* korektní varianta

@ tuple-type-2.py

@ tuple-type-2B.py

---

### Rozdílné typy prvků v n-tici

@ tuple-type-3.py

@ tuple-type-3B.py

---

### Typované seznamy

@ list-type-1.py
@ list-type-1B.py

---

### Typované seznamy

@ list-type-2.py
@ list-type-2B.py

---

* bool/int

@ list-type-3.py
@ list-type-3B.py

---

### Seznamy a typ `Union`

@ list-type-4.py
@ list-type-4B.py

---

### Typované slovníky

* Slovníky v Pythonu

@ dict-type-1.py

---

@ dict-type-2.py

---

### Typované slovníky

@ dict-type-3.py

---

@ dict-type-4.py

---

### Slovníky a typ `Union`

@ dict-type-5.py

---

@ dict-type-5B.py

---

### Slovníky a typ `Union`

@ dict-type-6.py

---

@ dict-type-6B.py

---

### Slovníky a typ `Optional`

@ dict-type-7.py

---

### Slovníky a typ `Optional`

@ dict-type-7B.py

---

### Funkce bez návratové hodnoty

@ function-no-return.py

---

### Typy a funkce vyššího řádu

* typ `callable`

@ callable-1.py

---

@ callable-2.py

---

### Typy a funkce vyššího řádu

* problém variance

@ callable-3.py

---

### Datový typ `range`

@ range-type-1.py
@ range-type-2.py

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

### Míchání hrušek s jablky v1

@ variance-1.py

---

### Míchání hrušek s jablky v2

@ variance-2.py

---

### Řešení problému variance v Pythonu

@ variance-3.py

---

### Použití `sequence` a nikoli seznamu

@ variance-4.py

---

### Tisk typové anotace

@ variance-5.py

---

### Návratové typy jsou kovariantní

@ variance-6.py

---

### Odkazy

1. [PEP 484 -- Type Hints](https://www.python.org/dev/peps/pep-0484/)
1. [What’s New In Python 3.5](https://docs.python.org/3.5/whatsnew/3.5.html)
1. [26.1. typing — Support for type hints](https://docs.python.org/3.5/library/typing.html#module-typing)
1. [Type Hints - Guido van Rossum - PyCon 2015 (youtube)](https://www.youtube.com/watch?v=2wDvzy6Hgxg)
1. [Python 3.5 is on its way](https://lwn.net/Articles/650904/)
1. [Type hints](https://lwn.net/Articles/640359/)

---

@ exit.py

