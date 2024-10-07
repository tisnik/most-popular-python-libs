# Typové informace v Pythonu

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

```python
# - specifikace typu globální proměnné
# - přiřazení nové hodnoty do proměnné


x: int = 42

x = 10
```

```python
# - specifikace typu globální proměnné
# - přiřazení nové hodnoty nekompatibilního typu do proměnné


x: int = 42

x = "foo"
```

```python
# - specifikace typu lokální proměnné
# - přiřazení nové hodnoty kompatibilního typu do proměnné


def funkce() -> int:
    x: int = 42
    return x * 2
```

```python
# - specifikace typu lokální proměnné
# - přiřazení nové hodnoty nekompatibilního typu do proměnné


def funkce(param: float) -> int:
    x: int = 1 / param
    return x
```


---

* Typ `Any` je přidán automaticky

```python
# - funkce bez uvedení typových anotací


def add(a, b):
    """Funkce bez typových anotací."""
    return a + b
```


---

* Proč `Any`?

```python
# Typové anotace a nástroj Mypy:
# - funkce bez uvedení typových anotací
# - zavolání této funkce pro různé typy argumentů


def add(a, b):
    """Funkce bez typových anotací."""
    return a + b


# zavolání funkce add s argumenty různých typů
print(add(1, 2))
print(add(1.1, 2.2))
print(add(1 + 1j, 2 + 2j))
print(add("foo", "bar"))
print(add([1, 2, 3], [4, 5, 6]))
print(add((1, 2, 3), (4, 5, 6)))
```


---

### Typové anotace

* specifikují se za dvojtečkou

```python
# - funkce s plným uvedením typových anotací


def add(a: int, b: int) -> int:
    """Funkce s typovými anotacemi."""
    return a + b
```


* využití

```python
# Typové anotace a nástroj Mypy:
# - funkce s uvedením typových informací
# - zavolání této funkce pro různé typy argumentů


def add(a: int, b: int) -> int:
    """Funkce s typovými anotacemi."""
    return a + b


# zavolání funkce add s argumenty různých typů
print(add(1, 2))
print(add(1.1, 2.2))
print(add(1 + 1j, 2 + 2j))
print(add("foo", "bar"))
print(add([1, 2, 3], [4, 5, 6]))
print(add((1, 2, 3), (4, 5, 6)))
```


---

### `bool` nebo `int`?

* Viz specifikaci Pythonu!

```
assert True+True==2
```

---

### `bool` nebo `int`?

```python
# - funkce s uvedením typových informací
# - zavolání této funkce pro argumenty typu bool a int
# - (ekvivalence mezi True a 1 i False a 0)


def add(a: int, b: int) -> int:
    """Funkce s typovými anotacemi."""
    return a + b


# zavolání funkce add s argumenty různých typů
print(add(1, 2))
print(add(1, True))
print(add(1, False))
```


```python
# - funkce s uvedením typových informací
# - zavolání této funkce pro argumenty typu bool a int


def add(a: bool, b: bool) -> bool:
    """Funkce s typovými anotacemi."""
    return a and b


# zavolání funkce add s argumenty různých typů
print(add(1, 2))
print(add(1, True))
print(add(1, False))
print(add(True, False))
```


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

```python
# - funkce s uvedením typových informací
# - použití zobecněného typu Union
# - zavolání této funkce pro různé typy argumenů

from typing import Union


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Funkce s typovými anotacemi."""
    return a + b


# zavolání funkce add s argumenty různých typů
print(add(1, 2))
print(add(1.1, 2))
print(add(1.1, 2.2))
```


```python
# - funkce s uvedením typových informací
# - použití zobecněného typu Union
# - úprava pro Python 3.10 a vyšší
# - zavolání této funkce pro různé typy argumentů


def add(a: int | float, b: int | float) -> int | float:
    """Funkce s typovými anotacemi."""
    return a + b


# zavolání funkce add s argumenty různých typů
print(add(1, 2))
print(add(1.1, 2))
print(add(1.1, 2.2))
```


---

### Dekorátor `@overload`

```python
# - funkce s uvedením typových informací pro dvě varianty parametrů
# - použití dekorátoru @overload
# - zavolání této funkce pro různé typy argumentů


from typing import Union, overload


@overload
def add(a: int, b: int) -> int:
    ...


@overload
def add(a: str, b: str) -> str:
    ...


def add(a: Union[int, str], b: Union[int, str]) -> Union[int, str]:
    """Funkce s typovými anotacemi."""
    return a + b


# zavolání funkce add s argumenty různých typů
print(add(1, 2))
print(add("foo", "bar"))
print(add(1, "bar"))
print(add("foo", 2))
```


```python
# - funkce s uvedením typových informací pro dvě varianty argumentů
# - použití dekorátoru @overload
# - zavolání této funkce pro různé typy argumentů


from typing import Union, overload


@overload
def add(a: int, b: int) -> int:
    ...


@overload
def add(a: str, b: str) -> str:
    ...


def add(a: Union[int, str], b: Union[int, str]) -> Union[int, str]:
    """Funkce s typovými anotacemi."""
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, str) and isinstance(b, str):
        return a + b
    else:
        raise TypeError("Mixing int and str is not supported!")


# zavolání funkce add s argumenty různých typů
print(add(1, 2))
print(add("foo", "bar"))
print(add(1, "bar"))
print(add("foo", 2))
```


---

### Typ `Optional`

```python
# - typ Optional
from typing import Optional

x: Optional[int]

x = None
x = 42
```

```python
# - typ Optional

x: int | None

x = None
x = 42
```


---

### Typované n-tice

* nekorektní varianta

```python
# - definice n-tice s jediným prvkem
# - kompatibilita s Mypy
# - (nekorektní typová informace)

from typing import Tuple

p: Tuple[int] = (1, 2, 3)
```


```python
# - definice n-tice s jediným prvkem
# - vyžaduje novější verzi Pythonu
# - (nekorektní typová informace)

p: tuple[int] = (1, 2, 3)
```


* korektní varianta

```python
# - definice n-tice s třemi prvky shodného typu
# - kompatibilita s Mypy

from typing import Tuple

p: Tuple[int, int, int] = (1, 2, 3)
```


```python
# - definice n-tice s třemi prvky shodného typu
# - vyžaduje novější verzi Pythonu

p: tuple[int, int, int] = (1, 2, 3)
```


---

### Rozdílné typy prvků v n-tici

```python
# - definice n-tice se čtyřmi prvky různých typů
# - kompatibilita s Mypy

from typing import Tuple

p: Tuple[int, float, bool, str] = (1, 3.14, True, "Hello")
```


```python
# - definice n-tice se čtyřmi prvky různých typů
# - vyžaduje novější verzi Pythonu

p: tuple[int, float, bool, str] = (1, 3.14, True, "Hello")
```


---

### Typované seznamy

```python
# Typové anotace a nástroj Mypy:
# - definice seznamu s prvky typu int
# - kompatibilita s Mypy

from typing import List

lst: List[int] = []
```

```python
# Typové anotace a nástroj Mypy:
# - definice seznamu s prvky typu int
# - vyžaduje novější verzi Pythonu

lst: list[int] = []
```


```python
# Typové anotace a nástroj Mypy:
# - definice seznamu s prvky typu int
# - inicializace prvků
# - kompatibilita s Mypy

from typing import List

lst: List[int] = [1, 2, 3]
```

```python
# Typové anotace a nástroj Mypy:
# - definice seznamu s prvky typu int
# - inicializace prvků
# - vyžaduje novější verzi Pythonu

lst: list[int] = [1, 2, 3]
```


---

* bool/int

```python
# - definice seznamu s prvky typu int
# - inicializace prvků
# - použití hodnot True a False

from typing import List

lst: List[int] = [1, True, False]
```

```python
# - definice seznamu s prvky typu int
# - inicializace prvků
# - použití hodnot True a False
# - vyžaduje novější verzi Pythonu

lst: list[int] = [1, True, False]
```


---

### Seznamy a typ `Union`

```python
# - definice seznamu s prvky typu int a str
# - inicializace prvků

from typing import List, Union

lst: List[Union[int, str]] = [1, "foo", 42, "bar"]
```

```python
# - definice seznamu s prvky typu int a str
# - inicializace prvků
# - úprava pro Python 3.10 a vyšší

lst: list[int | str] = [1, "foo", 42, "bar"]
```


---

### Typované slovníky

* Slovníky v Pythonu

```python
# - definice slovníku
# - všechny prvky mají shodné typy klíčů i hodnot

d = {}

d["foo"] = 1
d["bar"] = 3
d["baz"] = 10

print(d)
```


```python
# - definice slovníku
# - prvky mají rozdílné typy klíčů i hodnot

d = {}

d["foo"] = 1
d["bar"] = 3.14
d[10] = 10
d[42] = "answer"

print(d)
```


```python
# - definice slovníku
# - specifikace typu klíčů i typu hodnot

from typing import Any, Dict

d: Dict[Any, Any] = {}

d["foo"] = 1
d["bar"] = 3.14
d[10] = 10
d[42] = "answer"

print(d)
```


```python
# - definice slovníku
# - specifikace typu klíčů i typu hodnot

from typing import Dict

d: Dict[str, float] = {}

d["foo"] = 1
d["bar"] = 3.14
d[10] = 10
d[42] = "answer"

print(d)
```


---

### Slovníky a typ `Union`

```python
# - definice slovníku
# - specifikace typu klíčů i typu hodnot
# - u hodnot je použit typ Union

from typing import Dict, Union

d: Dict[str, Union[int, float, str]] = {}

d["foo"] = 1
d["bar"] = 3.14
d[10] = 10
d[42] = "answer"

print(d)
```


```python
# - definice slovníku
# - specifikace typu klíčů i typu hodnot
# - u hodnot je použit typ Union
# - úprava pro Python 3.10

d: dict[str, int | float | str] = {}

d["foo"] = 1
d["bar"] = 3.14
d[10] = 10
d[42] = "answer"

print(d)
```


```python
# - definice slovníku
# - specifikace typu klíčů i typu hodnot
# - u klíčů i hodnot je použit typ Union

from typing import Dict, Union

d: Dict[Union[int, str], Union[int, float, str]] = {}

d["foo"] = 1
d["bar"] = 3.14
d[10] = 10
d[42] = "answer"

print(d)
```


```python
# - definice slovníku
# - specifikace typu klíčů i typu hodnot
# - u klíčů i hodnot je použit typ Union
# - úprava pro Python 3.10

d: dict[int | str, int | float | str] = {}

d["foo"] = 1
d["bar"] = 3.14
d[10] = 10
d[42] = "answer"

print(d)
```


---

### Slovníky a typ `Optional`

```python
# Typové anotace a nástroj Mypy:
# - definice slovníku
# - specifikace typu klíčů i typu hodnot
# - hodnoty mohou nabývat None

from typing import Dict, Optional

d: Dict[str, Optional[float]] = {}

d["foo"] = 1
d["bar"] = 3.14
d["baz"] = None

print(d)
```


```python
# Typové anotace a nástroj Mypy:
# - definice slovníku
# - specifikace typu klíčů i typu hodnot
# - hodnoty mohou nabývat None
# - úprava pro Python 3.10

d: dict[str, float | None] = {}

d["foo"] = 1
d["bar"] = 3.14
d["baz"] = None

print(d)
```


---

### Funkce bez návratové hodnoty

```python
# Typové anotace a nástroj Mypy:
# - funkce bez návratové hodnoty s uvedením typových informací
# - zavolání této funkce pro argumenty typu str a int


def message(msg: str) -> None:
    """Funkce s typovými anotacemi."""
    print(f"Zpráva: {msg}")


# zavolání funkce
message("Ahoj")
```


---

### Typy a funkce vyššího řádu

* typ `callable`

```python
# - funkci printIsPositive lze předat jinou funkci
# - parametr "condition" nemá zapsán datový typ


def printIsPositive(x: float, condition) -> None:
    if condition(x):
        print("Positive")
    else:
        print("Negative")


def positiveFloat(x: float) -> bool:
    return x > 0.0


def positiveInt(x: int) -> bool:
    return x > 0


printIsPositive(4, positiveFloat)
printIsPositive(-0.5, positiveFloat)
```

```python
# - funkci printIsPositive lze předat jinou funkci
# - parametr "condition" má zapsán plný datový typ

from typing import Callable


def printIsPositive(x: float, condition: Callable[[float], bool]) -> None:
    if condition(x):
        print("Positive")
    else:
        print("Negative")


def positiveFloat(x: float) -> bool:
    return x > 0.0


printIsPositive(4, positiveFloat)
printIsPositive(-0.5, positiveFloat)
```


* problém variance

```python
# - funkci printIsPositive lze předat jinou funkci
# - parametr "condition" má zapsán datový typ
# - testování typu variance

from typing import Callable


def printIsPositive(x: float, condition: Callable[[float], bool]) -> None:
    if condition(x):
        print("Positive")
    else:
        print("Negative")


def positiveFloat(x: float) -> bool:
    return x > 0.0


def positiveInt(x: int) -> bool:
    return x > 0


printIsPositive(4, positiveFloat)
printIsPositive(-0.5, positiveFloat)
printIsPositive(1, positiveInt)
printIsPositive(1, positiveInt)
```


---

### Datový typ `range`

```python
# Typové anotace a nástroj Mypy:
# - použití datového typu range
# - typ definován pro návratovou hodnotu funkce


def funkce(from_val: int, to_val: int) -> range:
    return range(from_val, to_val)
```

```python
# Typové anotace a nástroj Mypy:
# - použití datového typu range
# - typ definován pro parametr funkce


def suma(x: range) -> int:
    return sum(x)


print(suma(range(100)))
```


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
