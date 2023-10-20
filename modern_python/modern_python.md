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

```python
a=1
b=2
c=a+b

print(f"{a}+{b}={c}")
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//f-string-1.py)

---

### Výrazy v f-řetězci

* V řetězci lze použít i výrazy

```python
a=1
b=2

print(f"{a}+{b}={a+b}")
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//f-string-2.py)

---

### Podmínka ve výrazu

* Ne vždy plně čitelné, ale pro jednoduché šablony ano

```python
a=1
b=-1

print(f"Kladné: {'ano' if a>0 else 'ne'}")
print(f"Kladné: {'ano' if b>0 else 'ne'}")
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//f-string-3.py)

---

### Volání funkce v f-řetězci

```python
x = "Hello world!"

print(f"Délka '{x}' je {len(x)} znaků")
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//f-string-4.py)

---

### Volání metody v f-řetězci

```python
x = "hello world!"

print(f"Zpráva pro vás: '{x.capitalize()}'")
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//f-string-5.py)

---

### Jednodušší ladění

```python
name = "Guido"
surname = "Rossum"

print(f"{name=} {surname=}")
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//f-string-6.py)

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

```python
def foo(x, y, z):
    return x+y-z


print(foo(1, 2, 10))
print(foo(x=1, y=2, z=10))
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//positional-params-1.py)

---

### Poziční parametry funkcí

* Parametry lze pojmenovat a předat v jiném pořadí

```python
def foo(x, y, z):
    return x+y-z


print(foo(1, 2, 10))
print(foo(z=1, y=2, x=10))
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//positional-params-2.py)

---

### Poziční parametry funkcí

* Všechny parametry jsou čistě poziční

```python
def foo(x, y, z, /):
    return x+y-z


print(foo(1, 2, 10))
print(foo(z=1, y=2, x=10))
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//positional-params-3.py)

---

### Poziční parametry funkcí

* První parametr je čistě poziční

```python
def foo(x, /, y, z):
    return x+y-z


print(foo(1, 2, 10))
print(foo(1, z=1, y=2))
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//positional-params-4.py)

---

### Poziční parametry funkcí

* Kombinace s pojmenovanými parametry

```python
def foo(x=0, /, y=0, z=0):
    return x+y-z


print(foo())
print(foo(10))
print(foo(1, 2, 10))
print(foo(1, z=1, y=2))
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//positional-params-5.py)

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

```python
print("Not ready reading drive A")


def abort_retry_fail():
    response = input("Abort, Retry, Fail? ")

    if response == "a":
        return "Abort"
    elif response == "r":
        return "Retry"
    elif response == "f":
        return "Fail"
    else:
        return "Wrong response"


print(abort_retry_fail())
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//pattern-matching-abort-retry-fail-1.py)

---

### Použití mapy (slovníku)

```python
print("Not ready reading drive A")


def abort_retry_fail():
    response = input("Abort, Retry, Fail? ")

    commands = {
            "a": "Abort",
            "r": "Retry",
            "f": "Fail"
            }

    return commands.get(response, "Wrong response")


print(abort_retry_fail())
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//pattern-matching-abort-retry-fail-2.py)

---

### Řídicí struktura match-case

```python
print("Not ready reading drive A")


def abort_retry_fail():
    response = input("Abort, Retry, Fail? ")

    match response:
        case "a":
            return "Abort"
        case "r":
            return "Retry"
        case "f":
            return "Fail"
        case _:
            return "Wrong response"


print(abort_retry_fail())
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//pattern-matching-abort-retry-fail-3.py)

---

### Množiny pro větší množství vstupů

```python
print("Not ready reading drive A")


def abort_retry_fail():
    response = input("Abort, Retry, Fail? ")

    if response in {"a", "A"}:
        return "Abort"
    elif response in {"r", "R"}:
        return "Retry"
    elif response in {"f", "F"}:
        return "Fail"
    else:
        return "Wrong response"


print(abort_retry_fail())
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//pattern-matching-abort-retry-fail-4.py)

---

### Spojka `or` ve vzoru

```python
print("Not ready reading drive A")


def abort_retry_fail():
    response = input("Abort, Retry, Fail? ")

    match response:
        case "a" | "A":
            return "Abort"
        case "r" | "R":
            return "Retry"
        case "f" | "F":
            return "Fail"
        case _:
            return "Wrong response"


print(abort_retry_fail())
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//pattern-matching-abort-retry-fail-5.py)

---

### Zachycení hodnoty ve vzoru

```python
print("Not ready reading drive A")


def abort_retry_fail():
    response = input("Abort, Retry, Fail? ")

    match response:
        case "a" | "A":
            return "Abort"
        case "r" | "R":
            return "Retry"
        case "f" | "F":
            return "Fail"
        case _ as x:
            return f"Wrong response {x}"


print(abort_retry_fail())
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//pattern-matching-abort-retry-fail-6.py)

---

### Zachycení hodnoty ve vzoru

```python
print("Not ready reading drive A")


def abort_retry_fail():

    match input("Abort, Retry, Fail? "):
        case "a" | "A":
            return "Abort"
        case "r" | "R":
            return "Retry"
        case "f" | "F":
            return "Fail"
        case _ as x:
            return f"Wrong response {x}"


print(abort_retry_fail())
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//pattern-matching-abort-retry-fail-7.py)

---

### Generátor Fibonaccího posloupnosti

```python
def fib(value):
    match value:
        case 0:
            return 0
        case 1:
            return 1
        case n if n>1:
            return fib(n-1) + fib(n-2)
        case _ as wrong:
            raise ValueError("Wrong input", wrong)


for n in range(0, 11):
    print(n, fib(n))

fib(-1)
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//pattern-matching-fib.py)

---

### Výpočet faktoriálu - základní varianta

```python
def factorial(n):
    match n:
        case 0:
            return 1
        case 1:
            return 1
        case x:
            return x * factorial(x-1)


for i in range(0, 10):
    print(i, factorial(i))
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//pattern-matching-factorial1.py)

---

### Podmínka ve větvi

```python
def factorial(n):
    match n:
        case 0:
            return 1
        case 1:
            return 1
        case x if x>1:
            return x * factorial(x-1)
        case _:
            raise TypeError("expecting integer >= 0")


for i in range(-1, 10):
    try:
        print(i, factorial(i))
    except Exception as e:
        print(e)
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//pattern-matching-factorial2.py)

---

### Test typu

```python
def factorial(n):
    match n:
        case 0:
            return 1
        case 1:
            return 1
        case x if isinstance(x, int) and x>1:
            return x * factorial(x-1)
        case _:
            raise TypeError("expecting integer >= 0")


for i in range(-1, 10):
    try:
        print(i, factorial(i))
    except Exception as e:
        print(e)

try:
    print(factorial(3.14))
except Exception as e:
    print(e)

try:
    print(factorial("hello"))
except Exception as e:
    print(e)
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//pattern-matching-factorial3.py)

---

### Větev "or"

```python
def factorial(n):
    match n:
        case 0 | 1:
            return 1
        case x if isinstance(x, int) and x>1:
            return x * factorial(x-1)
        case _:
            raise TypeError("expecting integer >= 0")


for i in range(-1, 10):
    try:
        print(i, factorial(i))
    except Exception as e:
        print(e)

try:
    print(factorial(3.14))
except Exception as e:
    print(e)

try:
    print(factorial("hello"))
except Exception as e:
    print(e)
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//pattern-matching-factorial4.py)

---

### Vzorek s n-ticí

```python
def test_number(value):
    match value:
        case (0, 0):
            print("Zero")
        case (real, 0):
            print(f"Real number {real}")
        case (0, imag):
            print(f"Imaginary number {imag}")
        case (real, imag):
            print(f"Complex number {real}+i{imag}")
        case _:
            raise ValueError("Not a complex number")


test_number((0,0))
test_number((1,0))
test_number((0,1))
test_number((1,1))
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//pattern-matching-complex1.py)

---

### Vzorek s n-ticí a s podmínkou

```python
def test_number(value):
    match value:
        case (0, 0):
            print("Zero")
        case (real, 0) if real>0:
            print(f"Positive real number {real}")
        case (real, 0):
            print(f"Negative real number {real}")
        case (0, imag) if imag<0:
            print(f"Negative imaginary number {imag}")
        case (0, imag):
            print(f"Negative imaginary number {imag}")
        case (real, imag):
            print(f"Complex number {real}+i{imag}")
        case _:
            raise ValueError("Not a complex number")


test_number((0,0))
test_number((1,0))
test_number((-1,0))
test_number((0,1))
test_number((0,-1))
test_number((1,1))
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//pattern-matching-complex2.py)

---

### Příkazy složené z většího množství slov

```python
def perform_command():
    response = input("> ")

    match response:
        case "quit":
            return "Quit"
        case "list employees":
            return "List employees"
        case "list departments":
            return "List departments"
        case "list rooms":
            return "List rooms"
        case _:
            return "Wrong command"


print(perform_command())
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//pattern-matching-multiword-commands-1.py)

---

### Vzorek a seznamy

```python
def perform_command():
    response = input("> ")

    match response.split():
        case ["quit"]:
            return "Quit"
        case ["list", "employees"]:
            return "List employees"
        case ["list", "departments"]:
            return "List departments"
        case ["list", "rooms"]:
            return "List rooms"
        case _:
            return "Wrong command"


print(perform_command())
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//pattern-matching-multiword-commands-2.py)

---

### Zachycení hodnoty

```python
def perform_command():
    response = input("> ")

    match response.split():
        case ["quit"]:
            return "Quit"
        case ["list", "employees"]:
            return "List employees"
        case ["list", "departments"]:
            return "List departments"
        case ["list", "rooms"]:
            return "List rooms"
        case ["info", subject]:
            return f"Info about subject '{subject}'"
        case _:
            return "Wrong command"


print(perform_command())
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//pattern-matching-multiword-commands-3.py)

---

### Vnořená konstrukce `match-case`

```python
def perform_command():
    response = input("> ")

    match response.split():
        case ["quit"]:
            return "Quit"
        case ["list", obj]:
            match obj:
                case "employees":
                    return "List employees"
                case "departments":
                    return "List departments"
                case "rooms":
                    return "List rooms"
                case _:
                    return "Invalid object type: employees, departments, or rooms expected"
        case ["info", subject]:
            return f"Info about subject '{subject}'"
        case _:
            return "Wrong command"


print(perform_command())
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//pattern-matching-multiword-commands-4.py)

---

### Vnořená konstrukce `match-case` + množiny ve vzorku

```python
def perform_command():
    response = input("> ")

    match response.split():
        case ["quit"]:
            return "Quit"
        case ["list", ("employees" | "departments" | "rooms") as obj]:
            match obj:
                case "employees":
                    return "List employees"
                case "departments":
                    return "List departments"
                case "rooms":
                    return "List rooms"
        case ["info", subject]:
            return f"Info about subject '{subject}'"
        case _:
            return "Wrong command"


print(perform_command())
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//pattern-matching-multiword-commands-5.py)

---

### Vzorky a OOP

```python
class Complex():

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"Complex number {self.real}+i{self.imag} represented as object"


def test_number(value):
    match value:
        case (0, 0):
            print("Zero")
        case (real, 0) if real>0:
            print(f"Positive real number {real}")
        case (real, 0):
            print(f"Negative real number {real}")
        case (0, imag) if imag<0:
            print(f"Negative imaginary number {imag}")
        case (0, imag):
            print(f"Negative imaginary number {imag}")
        case (real, imag):
            print(f"Complex number {real}+i{imag}")
        case Complex():
            print(value)
        case _:
            raise ValueError("Not a complex number")


test_number((0,0))
test_number((1,0))
test_number((-1,0))
test_number((0,1))
test_number((0,-1))
test_number((1,1))

test_number(Complex(0,0))
test_number(Complex(1,0))
test_number(Complex(-1,0))
test_number(Complex(0,1))
test_number(Complex(0,-1))
test_number(Complex(1,1))
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//pattern-matching-object1.py)

---

### Vzorky a OOP

```python
from fractions import Fraction


class Complex():

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"Complex number {self.real}+i{self.imag} represented as object"


def test_number(value):
    match value:
        case (0, 0):
            print("Zero")
        case (real, 0) if real>0:
            print(f"Positive real number {real}")
        case (real, 0):
            print(f"Negative real number {real}")
        case (0, imag) if imag<0:
            print(f"Negative imaginary number {imag}")
        case (0, imag):
            print(f"Negative imaginary number {imag}")
        case (real, imag):
            print(f"Complex number {real}+i{imag}")
        case Complex(real=0, imag=0):
            print(f"Zero complex represented as object")
        case Complex():
            print(value)
        case Fraction():
            print(f"Fraction {value}")
        case _:
            raise ValueError("Not a complex number")


test_number((0,0))
test_number((1,0))
test_number((-1,0))
test_number((0,1))
test_number((0,-1))
test_number((1,1))

test_number(Complex(0,0))
test_number(Complex(1,0))
test_number(Complex(-1,0))
test_number(Complex(0,1))
test_number(Complex(0,-1))
test_number(Complex(1,1))

test_number(Fraction(0,1))
test_number(Fraction(1,1))
test_number(Fraction(1,2))
test_number(Fraction(1,3))
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//pattern-matching-object2.py)

---

## Mroží operátor

* Přidáno do Pythonu 3.8
* PEP 572 - Assignment Expressions
* Možnost přiřazení v rámci `výrazu`
    - původní přiřazení lze jen v rámci `příkazu`
* Takzvané `pojmenované výrazy`

---

### Proměnná definovaná v podmínce

```python
limit = 8

password = "Hello world" 

if (length := len(password)) < limit:
    print(f"Password should be longer than {length} chars")
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//walrus-operator-1.py)

---

### Dtto, ale opačný výsledek

```python
limit = 8

password = "Hello" 

if (length := len(password)) < limit:
    print(f"Password should be longer than {length} chars")
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//walrus-operator-2.py)

---

### Problém: opakované výpočty

```python
values = (1, 2, 3, 4, 5)

result = {
        "count": len(values),
        "sum": sum(values),
        "mean": sum(values) / len(values)
        }

print(result)
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//walrus-operator-3.py)

---

### Předpočet hodnot

```python
values = (1, 2, 3, 4, 5)

count = len(values)
summ = sum(values)

result = {
        "count": count,
        "sum": summ,
        "mean": summ/count
        }

print(result)
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//walrus-operator-4.py)

---

### Úprava založená na walrus operátoru

```python
values = (1, 2, 3, 4, 5)

result = {
        "count": (count := len(values)),
        "sum": (summ := sum(values)),
        "mean": summ/count
        }

print(result)
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//walrus-operator-5.py)

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

```python
import asyncio
import time


async def task():
    print("task started")
    await asyncio.sleep(5)
    print("task finished")


def main():
    task1 = asyncio.create_task(task())
    print("task created")

    await task1

    print("done")


main()
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//async-await-1.py)

---

### `async` a `await`

* Korektní použití `await`

```python
import asyncio


async def task():
    print("task started")
    await asyncio.sleep(5)
    print("task finished")


async def main():
    task1 = asyncio.create_task(task())
    print("task created")

    await task1

    print("done")


asyncio.run(main())
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//async-await-2.py)

---

### Dvě souběžné úlohy

```python
import asyncio


async def task(name):
    print(f"{name} task started")
    await asyncio.sleep(5)
    print(f"{name} task finished")


async def main():
    task1 = asyncio.create_task(task("first"))
    print("first task created")

    task2 = asyncio.create_task(task("second"))
    print("second task created")

    await task1
    await task2

    print("done")


asyncio.run(main())
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//async-await-3.py)

---

### Tři souběžné úlohy, čtení výsledné hodnoty

```python
import asyncio


async def task(name):
    print(f"{name} task started")
    await asyncio.sleep(5)
    print(f"{name} task finished")
    return name[::-1]


async def main():
    task1 = asyncio.create_task(task("first"))
    print("first task created")

    task2 = asyncio.create_task(task("second"))
    print("second task created")

    task3 = asyncio.create_task(task("third"))
    print("third task created")

    print("result of task #1:", await task1)
    print("result of task #2:", await task2)
    print("result of task #3:", await task3)

    print("done")


asyncio.run(main())
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//async-await-4.py)

---

### Komunikace přes fronty

```python
import asyncio


async def task(name, queue):
    while not queue.empty():
        param = await queue.get()
        print(f"Task named {name} started with parameter {param}")
        await asyncio.sleep(5)
        print(f"{name} task finished")


async def main():
    queue = asyncio.Queue()

    for i in range(20):
        await queue.put(i)

    for n in range(1, 2):
        asyncio.create_task(task(f"{n}", queue))


asyncio.run(main())
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//async-queue-1.py)

---

### Čtení výsledků přes frontu

* Synchronizace

```python
import asyncio


async def task(name, queue):
    while not queue.empty():
        param = await queue.get()
        print(f"Task named {name} started with parameter {param}")
        await asyncio.sleep(5)
        print(f"{name} task finished")


async def main():
    queue = asyncio.Queue()

    for i in range(20):
        await queue.put(i)

    for n in range(1, 2):
        await asyncio.gather(asyncio.create_task(task(f"{n}", queue)))


asyncio.run(main())
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//async-queue-2.py)

---

### Producent-konzument

* Běžící asynchronně

```python
import asyncio


async def task(name, queue):
    while not queue.empty():
        param = await queue.get()
        print(f"Task named {name} started with parameter {param}")
        await asyncio.sleep(5)
        print(f"{name} task finished")


async def main():
    queue = asyncio.Queue()

    for i in range(20):
        await queue.put(i)

    await asyncio.gather(
        asyncio.create_task(task(1, queue)),
        asyncio.create_task(task(2, queue)),
        asyncio.create_task(task(3, queue)),
        asyncio.create_task(task(4, queue)),
    )


asyncio.run(main())
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//async-queue-3.py)

---

### Prioritní fronta

```python
import queue
import random

q = queue.PriorityQueue(40)

for item in range(30):
    print("Size", q.qsize())
    print("Empty?", q.empty())
    print("Full?", q.full())

    value = random.randint(1, 20)
    print(value)
    q.put("prvek # {:2d}".format(value))


while not q.empty():
    print("Read item:", q.get())
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//priority-queue.py)

---

### `aiohttp`

```python
import asyncio
import aiohttp
import time
 
 
async def download(name, queue):
    async with aiohttp.ClientSession() as session:
        while not queue.empty():
            url = await queue.get()
            print(f"Task named {name} getting URL: {url}")
            async with session.get(url) as response:
                t = await response.text()
                print(f"Task named {name} downloaded {len(t)} characters")
            print(f"Task named {name} finished")
 
 
async def main():
    queue = asyncio.Queue()
 
    for url in (
        "http://www.root.cz",
        "http://duckduckgo.com",
        "http://seznam.com",
        "https://www.root.cz/programovaci-jazyky/",
        "https://www.root.cz/clanky/soubezne-a-paralelne-bezici-ulohy-naprogramovane-v-pythonu/",
        "https://github.com/"
    ):
        await queue.put(url)
 
    await asyncio.gather(
            asyncio.create_task(download(1, queue)),
            asyncio.create_task(download(2, queue)))
 
 
asyncio.run(main())
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//aiohttp1.py)

---

### `aiohttp`

```python
import aiohttp
import time
 
 
async def download(name, queue, results):
    async with aiohttp.ClientSession() as session:
        while not queue.empty():
            url = await queue.get()
            t1 = time.time()
            print(f"Task named {name} getting URL: {url}")
            async with session.get(url) as response:
                t = await response.text()
                t2 = time.time()
                print(f"Task named {name} downloaded {len(t)} characters in {t2-t1} seconds")
                await results.put(t2-t1)
            print(f"Task named {name} finished")
 
 
async def main():
    queue = asyncio.Queue()
    results = asyncio.Queue()
 
    t1 = time.time()
 
    for url in (
        "http://www.root.cz",
        "http://duckduckgo.com",
        "http://seznam.com",
        "https://www.root.cz/programovaci-jazyky/",
        "https://www.root.cz/clanky/soubezne-a-paralelne-bezici-ulohy-naprogramovane-v-pythonu/",
        "https://www.root.cz/clanky/pywebio-interaktivni-webove-dialogy-a-formulare-v-cistem-pythonu/",
        "https://streamlit.io/",
        "https://pglet.io/",
        "https://www.root.cz/serialy/graficke-uzivatelske-rozhrani-v-pythonu/",
        "https://github.com/"
    ):
        await queue.put(url)
 
    await asyncio.gather(
            asyncio.create_task(download(1, queue, results)),
            asyncio.create_task(download(2, queue, results)),
            asyncio.create_task(download(3, queue, results)))
 
    process_time = 0
    while not results.empty():
        process_time += await results.get()
 
    print(f"Process time: {process_time} seconds")
 
    t2 = time.time()
    print(f"Total time:   {t2-t1} seconds")
 
asyncio.run(main())
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//aiohttp2.py)

---

## Skupiny výjimek

* Přidáno do Pythonu 3.11
* PEP 654 – Exception Groups and except

---

### Vyhození skupiny výjimek

```python
eg = ExceptionGroup(
    "one", [TypeError(1), ValueError(3), OSError(4)])

import traceback
traceback.print_exception(eg)
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//exception-group-1.py)

---

### Vyhození skupiny výjimek

```python
eg = ExceptionGroup(
    "one",
    [
        TypeError(1),
        ExceptionGroup(
            "two",
             [TypeError(2), ValueError(3)]
        ),
        ExceptionGroup(
             "three",
              [OSError(4)]
        )
    ]
)

import traceback
traceback.print_exception(eg)
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//exception-group-2.py)

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

```python
def add(a, b):
    return a+b
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//mypy-add-1.py)

* Typ `Any` je přidán automaticky

---

### Typové anotace

* specifikují se za dvojtečkou

```python
def add(a:int, b:int) -> int:
    return a+b
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//mypy-add-2.py)

---

### `bool` nebo `int`?

* Viz specifikace Pythonu!

```python
def add(a:int, b:int) -> int:
    return a+b

print(add(1, 2))
print(add(1, True))
print(add(1, False))
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//mypy-add-3.py)
```python
def add(a:bool, b:bool) -> bool:
    return a and b

print(add(1, 2))
print(add(1, True))
print(add(1, False))
print(add(True, False))
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//mypy-add-4.py)

---

### Výpis typových anotací

* `any`

```python
def add(a, b):
    return a+b


print(add.__annotations__)
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//mypy-add-5.py)

* explicitní typy

```python
def add(a:int, b:int) -> int:
    return a+b


print(add.__annotations__)
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//mypy-add-6.py)


---

### Výpis typových anotací

* složitější typy

```python
from typing import List, Set

def add(a:List[Set[int]], b:List[Set[int]]) -> List[Set[int]]:
    return a+b


print(add.__annotations__)
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//mypy-add-7.py)

---

### Typované n-tice

* nekorektní varianta

```python
from typing import Tuple

p: Tuple[int] = (1, 2, 3)
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//mypy-tuple-type-1.py)

* korektní varianta

```python
from typing import Tuple

p: Tuple[int, int, int] = (1, 2, 3)
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//mypy-tuple-type-2.py)

---

### Rozdílné typy prvků

* nekorektní varianta

```python
from typing import Tuple

p: Tuple[int, float, bool, str] = (1, 3.14, True, "Hello")
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//mypy-tuple-type-3.py)

* korektní varianta

```python
from typing import Tuple

p: Tuple[int, float, bool, str] = (2.0, 3.14, 1, "Hello")
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//mypy-tuple-type-4.py)

---

### Typované seznamy

* nekorektní varianta

```python
l: list[int] = []
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//mypy-list-type-1.py)

* import

```python
from typing import List

l: List[int] = []
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//mypy-list-type-2.py)

---

### Test typu prvků

* v pořádku

```python
from typing import List

l: List[int] = [1, 2, 3]
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//mypy-list-type-3.py)

* nekorektní

```python
from typing import List

l: List[int] = [1, 2, None]
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//mypy-list-type-4.py)

---

### Znovu problém bool-int

* v pořádku

```python
from typing import List

l: List[int] = [1, True, False]
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//mypy-list-type-5.py)

* nekorektní

```python
from typing import List

l: List[bool] = [True, False, 42]
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//mypy-list-type-6.py)

---

### Typované slovníky

* Slovníky v Pythonu

```python
d = {}

d["foo"] = 1
d["bar"] = 3
d["baz"] = 10

print(d)
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//mypy-dict-type-1.py)

* Libovolné klíče a hodnoty

```python
d = {}

d["foo"] = 1
d["bar"] = 3.14
d[10] = 10
d[42] = "answer"

print(d)
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//mypy-dict-type-2.py)

---

### Specifikace typu slovníku

* použití typu `any`

```python
from typing import Dict, Any

d:Dict[Any, Any] = {}

d["foo"] = 1
d["bar"] = 3.14
d[10] = 10
d[42] = "answer"

print(d)
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//mypy-dict-type-3.py)

---

### Specifikace typu slovníku

* explicitní specifikace

```python
from typing import Dict

d:Dict[str, float] = {}

d["foo"] = 1
d["bar"] = 3.14
d[10] = 10
d[42] = "answer"

print(d)
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//mypy-dict-type-4.py)

---

### Typ `union`

* Pro hodnoty

```python
from typing import Dict, Union

d:Dict[str, Union[int, float, str]] = {}

d["foo"] = 1
d["bar"] = 3.14
d[10] = 10
d[42] = "answer"

print(d)
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//mypy-dict-type-5.py)

---

### Typ `union`

* Pro klíče

```python
from typing import Dict, Union

d:Dict[Union[int, str], Union[int, float, str]] = {}

d["foo"] = 1
d["bar"] = 3.14
d[10] = 10
d[42] = "answer"

print(d)
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//mypy-dict-type-6.py)

---

### Typ `optional`

* Bez `optional`

```python
from typing import Dict

d:Dict[str, float] = {}

d["foo"] = 1
d["bar"] = 3.14
d["baz"] = None

print(d)
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//mypy-dict-type-7.py)

---

### Typ `optional`

* S `optional`

```python
from typing import Dict, Optional

d:Dict[str, Optional[float]] = {}

d["foo"] = 1
d["bar"] = 3.14
d["baz"] = None

print(d)
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//mypy-dict-type-8.py)

---

### Typy a funkce vyššího řádu

* typ `callable`

```python
#!/usr/bin/env python3
# vim: set fileencoding=utf-8

#
#  (C) Copyright 2023  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

from typing import Callable


def printIsPositive(condition:Callable[[float], bool]) -> None:
    if condition(5):
        print("Positive")
    else:
        print("Negative")


def positiveFloat(x:float) -> bool:
    return x > 0.0


def positiveInt(x:int) -> bool:
    return x > 0


printIsPositive(positiveFloat)
printIsPositive(positiveInt)
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//mypy-callable.py)

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

```python
from typing import List


class Ovoce:
    pass


class Hruska(Ovoce):
    def __repr__(self):
        return "Hruska"


class Jablko(Ovoce):
    def __repr__(self):
        return "Jablko"


def tiskni(kosik : List[Ovoce]):
    for ovoce in kosik:
        print(ovoce)


kosik : List[Hruska] = []

tiskni(kosik)
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//mypy-variance-1.py)

---

### Použití `sequence` a nikoli seznamu

```python
from typing import Sequence


class Ovoce:
    pass


class Hruska(Ovoce):
    def __repr__(self):
        return "Hruska"


class Jablko(Ovoce):
    def __repr__(self):
        return "Jablko"


def tiskni(kosik : Sequence[Ovoce]):
    for ovoce in kosik:
        print(ovoce)


kosik : Sequence[Hruska] = []

tiskni(kosik)
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//mypy-variance-2.py)

---

### Tisk typové anotace

```python
from typing import Sequence


class Ovoce:
    pass


class Hruska(Ovoce):
    def __repr__(self):
        return "Hruska"


class Jablko(Ovoce):
    def __repr__(self):
        return "Jablko"


def tiskni(kosik : Sequence[Ovoce]):
    for ovoce in kosik:
        print(ovoce)


kosik : Sequence[Hruska] = []

tiskni(kosik)

print(tiskni.__annotations__)
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//mypy-variance-3.py)

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

