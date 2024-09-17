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

---

### Částečně flexibilní řešení

* Ne všechny vzory je možné použít
    - například `"literal" + x + "literal"`
    - možná se jejich podpora objeví v další verzi Pythonu?

---

### Ukázky pattern matchingu

---

