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

@ pattern-matching-fib.py

@ ackermann-if.py

@ ackermann-if-else.py

@ pattern-matching-ackermann.py

### Rozvětvení

@ pattern-matching-abort-retry-fail-1.py

@ pattern-matching-abort-retry-fail-2.py

@ pattern-matching-abort-retry-fail-3.py

### Python nehlídá, zda jsou pokryty všechny případy

@ pattern-matching-abort-retry-fail-4.py

### Vzory obsahující v&nbsp;každé větvi vetší množství hodnot

@ pattern-matching-abort-retry-fail-5.py

@ pattern-matching-abort-retry-fail-6.py

### Zachycení hodnoty proměnné v&nbsp;rozhodovací větvi

@ pattern-matching-abort-retry-fail-7.py

@ pattern-matching-abort-retry-fail-8.py

### Podmínka zapsaná v&nbsp;rozhodovacích větvích konstrukce `match`

@ pattern-matching-factorial1.py

@ pattern-matching-factorial2.py

@ pattern-matching-factorial3.py

@ pattern-matching-factorial4.py

---

### Pattern matching a n-tice a seznamy

@ pattern-matching-complex1.py

### Seznamy, n-tice a podmínky pro hodnoty prvků těchto kolekcí

@ pattern-matching-complex2.py

@ pattern-matching-complex2B.py

### Zpracování příkazů či strukturovaných textových souborů s&nbsp;využitím pattern matchingu

@ pattern-matching-multiword-commands-1.py

### Rozdělení na jednotlivá slova

@ pattern-matching-multiword-commands-2.py

### Rozpoznání a zpracování proměnné části víceslovních příkazů

@ pattern-matching-multiword-commands-3.py

### Vnořené řídicí struktury `match`

@ pattern-matching-multiword-commands-4.py
@ pattern-matching-multiword-commands-5.py

### Zachycení dopředu neznámého počtu hodnot

@ pattern-matching-multiword-commands-6.py
@ pattern-matching-multiword-commands-7.py

### Strukturální pattern matching a objekty

@ pattern-matching-object1.py
@ pattern-matching-object2.py

### Rozpoznání typu výjimky

@ pattern-matching-exception.py

### Ucelený příklad na konec: reprezentace barev různými metodami

@ colors.py
