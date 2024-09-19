# Pattern matching v Pythonu

---

* Pavel Tišnovský
* kurzy.python@centrum.cz

---

![Python](images/python.png)

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

## Pattern matching

* Přidáno do Pythonu 3.10
* Zdánlivě lepší varianta konstrukce `switch-case`
    - ovšem možnosti jsou mnohem větší
* Další použití
    - zachycení hodnot
    - test typů
    - podmínky v rozhodovacích větvích

---

### Inspirováno dalšími programovacími jazyky

* SNOBOL
* AWK
* ML (Caml, OCaml, F#)
* Rust
* Coconut (překládáno do Pythonu)

---

### SNOBOL

```
          OUTPUT = "What is your name?"
          Username = INPUT
          Username "J"                                             :S(LOVE)
          Username "K"                                             :S(HATE)
MEH       OUTPUT = "Hi, " Username                                 :(END)
LOVE      OUTPUT = "How nice to meet you, " Username               :(END)
HATE      OUTPUT = "Oh. It's you, " Username
END
```

---

### ML (předchůdce OCamlu a jazyka F#)

```
fun fib 0 = 0
  | fib 1 = 1
  | fib n = fib (n - 1) + fib (n - 2);
```

```
fun length(x) = if null(x) then 0
                else 1 + length(tl(x));
```

```
fun length([]) = 0
  | length(a::x) = 1 + length(x)
```

---

### F#

```fsharp
let rec fib n =
    match n with
    | 0 -> 0
    | 1 -> 1
    | n -> fib(n-1) + fib(n-2)
```

---

### Rust

```rust
```
### Rust

```rust
```
### Rust

```rust
fn main() {
    let x:i32 = 1;

    match x {
        0 => println!("zero"),
        1 => println!("one"),
        2 => println!("two"),
        3 => println!("three"),
        _ => println!("something else"),
    }
}
```

```rust
fn fib(n: u32) -> u32 {
    match n {
        0 | 1 => 1,
        _ => fib(n - 1) + fib(n - 2),
    }
}

fn main() {
    for x in 0..10 {
        println!("{}:{}", x, fib(x))
    }
}
```

---

### Částečně flexibilní řešení

* Ne všechny vzory je možné použít
    - například `"literal" + x + "literal"`
    - možná se jejich podpora objeví v další verzi Pythonu?

---

### Ukázky pattern matchingu

```python
# Strukturální pattern matching:
# - Výpočet Fibonacciho posloupnost realizovaný s využitím
#   pattern matchingu


def fib(value):
    """Výpočet jednoho prvku Fibonacciho posloupnosti."""
    match value:
        case 0:
            return 0
        case 1:
            return 1
        case n if n>1:
            return fib(n-1) + fib(n-2)
        case _ as wrong:
            raise ValueError("Wrong input", wrong)


# tisk tabulky s prvky Fibonacciho posloupnosti
for n in range(0, 11):
    print(n, fib(n))

# test neplatného vstupu
fib(-1)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/pattern_matching/presentation//pattern-matching-fib.py)

```python
# Výpočet Ackermannovy funkce, založeno na konstrukci if

def A(m, n):
    """Ackermannova funkce."""
    if m == 0:
        return n + 1
    if n == 0:
        return A(m - 1, 1)
    return A(m - 1, A(m, n - 1))


# otestování korektnosti výpočtu Ackermannovy funkce
for m in range(4):
    for n in range(5):
        print(m, n, A(m, n))

```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/pattern_matching/presentation//ackermann-if.py)

```python
# Výpočet Ackermannovy funkce, založeno na konstrukci if-elif-else

def A(m, n):
    """Ackermannova funkce."""
    if m == 0:
        return n + 1
    elif n == 0:
        return A(m - 1, 1)
    else:
        return A(m - 1, A(m, n - 1))


# otestování korektnostni výpočtu Ackermannovy funkce
for m in range(4):
    for n in range(5):
        print(m, n, A(m, n))

```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/pattern_matching/presentation//ackermann-if-else.py)

```python
# Strukturální pattern matching:
# - Výpočet Ackermannovy funkce

def A(m, n):
    """Ackermannova funkce."""
    match (m, n):
        case (0, n):
            return n + 1
        case (m, 0):
            return A(m-1, 1)
        case (m, n):
            return A(m - 1, A(m, n - 1))


# otestování korektnosti výpočtu Ackermannovy funkce
for m in range(4):
    for n in range(5):
        print(m, n, A(m, n))

```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/pattern_matching/presentation//pattern-matching-ackermann.py)

### Rozvětvení

```python
# Strukturální pattern matching:
# - použití rozhodovací konstrukce if-elif-else
#   namísto pattern matchingu

print("Not ready reading drive A")


def abort_retry_fail():
    # získání odpovědi od uživatele
    response = input("Abort, Retry, Fail? ")

    # rozhodnutí o provedené operaci na základě odpovědi
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

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/pattern_matching/presentation//pattern-matching-abort-retry-fail-1.py)

```python
# Strukturální pattern matching:
# - rozhodování realizované slovníkem (mapou)
#   namísto pattern matchingu

print("Not ready reading drive A")


def abort_retry_fail():
    # získání odpovědi od uživatele
    response = input("Abort, Retry, Fail? ")

    # odpovědi a odpovídající operace
    commands = {
            "a": "Abort",
            "r": "Retry",
            "f": "Fail",
            }

    # rozhodnutí o provedené operaci na základě odpovědi
    return commands.get(response, "Wrong response")


print(abort_retry_fail())
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/pattern_matching/presentation//pattern-matching-abort-retry-fail-2.py)

```python
# Strukturální pattern matching:
# - rozhodování realizované pattern matchingem

print("Not ready reading drive A")


def abort_retry_fail():
    # získání odpovědi od uživatele
    response = input("Abort, Retry, Fail? ")

    # rozhodnutí o provedené operaci na základě odpovědi
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

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/pattern_matching/presentation//pattern-matching-abort-retry-fail-3.py)

### Python nehlídá, zda jsou pokryty všechny případy

```python
# Strukturální pattern matching:
# - rozhodování realizované pattern matchingem

print("Not ready reading drive A")


def abort_retry_fail():
    # získání odpovědi od uživatele
    response = input("Abort, Retry, Fail? ")

    # rozhodnutí o provedené operaci na základě odpovědi
    match response:
        case "a":
            return "Abort"
        case "r":
            return "Retry"
        case "f":
            return "Fail"


print(abort_retry_fail())
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/pattern_matching/presentation//pattern-matching-abort-retry-fail-4.py)

### Vzory obsahující v&nbsp;každé větvi vetší množství hodnot

```python
# Strukturální pattern matching:
# - použití rozhodovací konstrukce if-elif-else
# - podpora odpovědí psaných velkými i malými znaky

print("Not ready reading drive A")


def abort_retry_fail():
    # získání odpovědi od uživatele
    response = input("Abort, Retry, Fail? ")

    # rozhodnutí o provedené operaci na základě odpovědi
    if response in {"a", "A", "abort", "Abort", "ABORT"}:
        return "Abort"
    elif response in {"r", "R"}:
        return "Retry"
    elif response in {"f", "F"}:
        return "Fail"
    else:
        return "Wrong response"


print(abort_retry_fail())
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/pattern_matching/presentation//pattern-matching-abort-retry-fail-5.py)

```python
# Strukturální pattern matching:
# - rozhodování realizované pattern matchingem
# - podpora odpovědí psaných velkými i malými znaky

print("Not ready reading drive A")


def abort_retry_fail():
    # získání odpovědi od uživatele
    response = input("Abort, Retry, Fail? ")

    # rozhodnutí o provedené operaci na základě odpovědi
    match response:
        case "a" | "A" | "abort" | "Abort" | "ABORT":
            return "Abort"
        case "r" | "R":
            return "Retry"
        case "f" | "F":
            return "Fail"
        case _:
            return "Wrong response"


print(abort_retry_fail())
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/pattern_matching/presentation//pattern-matching-abort-retry-fail-6.py)

### Zachycení hodnoty proměnné v&nbsp;rozhodovací větvi

```python
# Strukturální pattern matching:
# - rozhodování realizované pattern matchingem
# - podpora odpovědí psaných velkými i malými znaky
# - zachycení neočekávané odpovědi

print("Not ready reading drive A")


def abort_retry_fail():
    # získání odpovědi od uživatele
    response = input("Abort, Retry, Fail? ")

    # rozhodnutí o provedené operaci na základě odpovědi
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

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/pattern_matching/presentation//pattern-matching-abort-retry-fail-7.py)

```python
# Strukturální pattern matching:
# - rozhodování realizované pattern matchingem

print("Not ready reading drive A")


def abort_retry_fail():
    # získání odpovědi od uživatele
    # a rozhodnutí o provedené operaci
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

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/pattern_matching/presentation//pattern-matching-abort-retry-fail-8.py)

### Podmínka zapsaná v&nbsp;rozhodovacích větvích konstrukce `match`

```python
# Strukturální pattern matching:
# - výpočet faktoriálu s využitím pattern matchingu
# - základní varianta akceptující neplatné vstupy

def factorial(n):
    """Rekurzivní výpočet faktoriálu."""
    match n:
        case 0:
            return 1
        case 1:
            return 1
        case x:
            return x * factorial(x-1)


# tisk tabulky faktoriálů
for i in range(0, 10):
    print(i, factorial(i))
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/pattern_matching/presentation//pattern-matching-factorial1.py)

```python
# Strukturální pattern matching:
# - výpočet faktoriálu s využitím pattern matchingu
# - test, zda je vstup nezáporný

def factorial(n):
    """Rekurzivní výpočet faktoriálu."""
    match n:
        case 0:
            return 1
        case 1:
            return 1
        case x if x>1:
            return x * factorial(x-1)
        case _:
            raise TypeError("expecting integer >= 0")


# tisk tabulky faktoriálů
for i in range(-1, 10):
    try:
        print(i, factorial(i))
    except Exception as e:
        print(e)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/pattern_matching/presentation//pattern-matching-factorial2.py)

```python
# Strukturální pattern matching:
# - výpočet faktoriálu s využitím pattern matchingu
# - test, zda má vstup korektní typ


def factorial(n):
    """Rekurzivní výpočet faktoriálu."""
    match n:
        case 0:
            return 1
        case 1:
            return 1
        case x if isinstance(x, int) and x>1:
            return x * factorial(x-1)
        case _:
            raise TypeError("expecting integer >= 0")


# tisk tabulky faktoriálů
for i in range(-1, 10):
    try:
        print(i, factorial(i))
    except Exception as e:
        print(e)

# test reakce na nekorektní vstup
try:
    print(factorial(3.14))
except Exception as e:
    print(e)

# test reakce na nekorektní vstup
try:
    print(factorial("hello"))
except Exception as e:
    print(e)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/pattern_matching/presentation//pattern-matching-factorial3.py)

```python
# Strukturální pattern matching:
# - výpočet faktoriálu s využitím pattern matchingu
# - použití vzoru s operátorem "or"


def factorial(n):
    """Rekurzivní výpočet faktoriálu."""
    match n:
        case 0 | 1:
            return 1
        case x if isinstance(x, int) and x>1:
            return x * factorial(x-1)
        case _:
            raise TypeError("expecting integer >= 0")


# tisk tabulky faktoriálů
for i in range(-1, 10):
    try:
        print(i, factorial(i))
    except Exception as e:
        print(e)

# test reakce na nekorektní vstup
try:
    print(factorial(3.14))
except Exception as e:
    print(e)

# test reakce na nekorektní vstup
try:
    print(factorial("hello"))
except Exception as e:
    print(e)
```

[Zdrojový kód tohoto příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/pattern_matching/presentation//pattern-matching-factorial4.py)

---

