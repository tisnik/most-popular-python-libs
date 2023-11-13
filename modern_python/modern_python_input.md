# Evoluce Pythonu

---

* Pavel Tišnovský
* kurzy.python@centrum.cz

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

### Generátor Fibonacciho posloupnosti

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

## Správa projektů

* pip (+ venv či virtualenv)
* Pyenv
* Poetry
* Hatch
* PDM

---

## Lintery

* pycodestyle
* pydocstyle
* black
* ruff
* (mypy)

---

### pip

* `requirements.txt`
    - typicky zvolené verze
    - min/max/konkrétní/latest

---

### Problémy pipu

* jak pracovat s virtualenv
* kontrola verzí (konzistence)
* řešení tranzitivních závislostí
* striktní nebo příliš volný rozsah verzí
* nejsou k dispozici otisky balíčků
    - možný prostor pro útoky
    - nelze reprodukovat "build" na dalším počítači
    - či dokonce na stejném počítači později

---

### Další problémy

* kam uložit metadata projektu
    - nastavení linterů
    - informace o autorovi
    - aliasy příkazů
* `setup.py` je jen částečným řešením
* `setup.cfg`
    `.coveragerc`
    `tox.ini`
    - atd. atd.

---

### `setup.cfg`

```
[metadata]
name = ccx-data-pipeline
author = somebody
description-file = README.md
license = Apache 2.0
long_description_content_type = text/markdown
home-page = https://github.com/somebody/ccx-data-pipeline
classifier =
    Intended Audience :: Information Technology
    Intended Audience :: System Administrators
    Operating System :: POSIX :: Linux
    Programming Language :: Python
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3.7

[options]
zip_safe = False
packages = find:
install_requires =
    app-common-python
    insights-core-messaging
    ccx-ocp-core
    ccx-rules-ocp
    ccx-rules-ocm
    kafka-python
    requests
    jsonschema
    python-json-logger
    prometheus_client
    python-logstash
    boto3
    watchtower
setup_requires =
    setuptools
    setuptools_scm
    wheel

[options.packages.find]
exclude =
    test*

[options.entry_points]
console_scripts =
    ccx-data-pipeline = ccx_data_pipeline.command_line:ccx_data_pipeline

[options.extras_require]
dev =
    black
    coverage
    freezegun
    pycco
    pycodestyle
    pydocstyle
    pylint
    pytest
    pytest-cov

[pycodestyle]
ignore = E402
max-line-length = 100
exclude =
    .tox,
    .git,
    __pycache__,
    build,
    dist,
    tests/,
    samples/,
    *.pyc,
    *.egg-info,
    .cache,
    .eggs,
    docs,
    .venv,
    venv,

[flake8]
max-line-length = 100
```

---

### `setup.py`

```
from setuptools import setup


setup(use_scm_version={"local_scheme": "node-and-timestamp"})
```

---

### `requirements.txt`

```
-i https://repository.engineering.redhat.com/nexus/repository/ccx/simple

app-common-python==0.1.8
attrs==19.3.0
boto3==1.14.27
botocore==1.17.27
CacheControl==0.12.6
ccx-ocp-core==2021.12.08
ccx-rules-ocm==0.0.1
ccx-rules-ocp==2021.12.08
certifi==2020.6.20
cffi==1.14.0
chardet==3.0.4
colorama==0.4.3
cryptography==3.0
dateparser==0.7.6
decorator==4.4.2
defusedxml==0.6.0
docutils==0.15.2
fsspec==0.7.4
idna==2.10
importlib-metadata==1.7.0
insights-core>=3.0.235
insights-core-messaging==1.2.0
Jinja2==2.11.2
jmespath==0.10.0
jsonschema==3.2.0
kafka-python==2.0.1
lockfile==0.12.2
MarkupSafe==1.1.1
msgpack==1.0.0
numpy==1.19.1
packaging==20.7
pandas==1.0.5
prometheus-api-client==0.3.1
prometheus-client==0.9.0
py==1.9.0
pycparser==2.20
pyparsing==2.4.7
pyrsistent==0.16.0
python-dateutil==2.8.1
python-json-logger==0.1.11
python-logstash==0.4.6
pytz==2020.1
PyYAML==5.3.1
redis==3.5.3
regex==2020.7.14
requests==2.24.0
retry==0.9.2
retrying==1.3.3
s3fs==0.4.2
s3transfer==0.3.3
six==1.15.0
tzlocal==2.1
urllib3==1.25.10
watchtower==0.8.0
zipp==3.1.0
sentry-sdk==0.19.5
```

---

### `pyproject.toml`

* všechna metadata v jediném souboru
* PEP-621
* správa závislostí pro různá prostředí
* metadata pro další nástroje
    - `ruff`
    - `mypy`
    - `black`

---

### Lock file

* obsahuje konkrétní verze závislostí
* taktéž otisky balíčků
* i pro tranzitivní závislosti
* build lze kdykoli zopakovat
    - jiný počítač
    - stejný počítač v jiném okamžiku

---

### PDM

* správce závislostí
* správce prostředí
* používá `pyproject.toml`
* a lock file

---

### PDM

* vytvoření nového projektu
* soubor `pyproject.toml`
* přidání nové závislosti
* tranzitivní závislosti
* závislosti pro vývojáře
* lock file
* správa prostředí

---

### Lintery

* Black
* Pycodestyle
* Pydocstyle
* Ruff

---

### Black

* automatické formátování zdrojového kódu
* na základě specifikovaných pravidel

---

### Pycodestyle

* kontrola, zda zdrojový kód odovídá PEP-8
* whodné zkombinovat s dalšími podobnými nástroji
    - Ruff atd.
---

### Pydocstyle

- kontrola dokumentačních řetězců
- moduly
- třídy
- metody
- funkce

---

### Ruff

* nový nástroj pro kontrolu zdrojových kódů Pythonu
* napsáno v Rustu
    - velmi rychlý
* možno relativně snadno přidat do CI

---

### Ruff

* konfigurace v souboru `pyproject.toml`

```toml
[tool.ruff]
#select = ["E", "F", "W", "C", "D"]
select = ["E", "F", "W", "C"]
ignore = ["D211", "D213", "E402"]

line-length = 100
```

---

### Makefile

```
style:  code-style docs-style ## Perform all style checks

code-style: ## Check code style for all Python sources from this repository
        python3 tools/run_pycodestyle.py

ruff: ## Run Ruff linter
        ruff .

docs-style: ## Check documentation strings in all Python sources from this repository
        pydocstyle .

doc-check: ## Run gen_scenario_list.py to generate docs file and compare it to current one
        python3 tools/gen_scenario_list.py > tmp.md
        diff tmp.md docs/scenarios_list.md
```

---

### Kontrola na CI

* konfigurace repositáře
* TravisCI
* GitHub Actions
* atd.

---

### TravisCI

* `.travis.yml`

```yaml
language: python
python:
    #- "3.7"
  - "3.8"
  - "3.8-dev"  # 3.8 development branch
  - "nightly"  # nightly build
addons:
  apt:
    packages:
    - libsnappy-dev
# Pycodestyle part
# needed to work correctly with Python 3 shebang
env: SKIP_INTERPRETER=true
install:
  - pip install pycodestyle
  - pip install pytest-cov
  - pip install -r requirements.txt
script:
  - make code-style
  - pytest -v --cov=schemas/
```

---

### GitHub Actions

* `.github/workflows/*.yaml`

```yaml
name: Ruff
on: [ push, pull_request ]
jobs:
  ruff:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: chartboost/ruff-action@v1
```

---

### GitHub Actions

* `.github/workflows/*.yaml`

```yaml
name: Pytest

on:
  - push
  - pull_request

jobs:
  pytest:
    runs-on: ubuntu-20.04
    strategy:
      matrix:
        python-version:
          - "3.7"
          - "3.8"
          - "3.9"
          - "3.10"
          - "3.11"
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
      - run: pip install --upgrade setuptools
      - run: pip install --upgrade wheel
      - run: pip install pycodestyle
      - run: pip install pydocstyle
      - run: pip install pytest-cov
      - run: pip install --upgrade importlib-metadata
      - run: pip install behave
      - run: pip install semver
      - name: Style checks
        run: make style
      - name: Docstrings checks
        run: make doc-check
      - name: Unit tests
        run: make unit_tests
      - name: Unit tests coverage
        run: make coverage
```

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
* Proč?
    - viz další slajdy

---

### Problematika výkonu aplikací psaných v Pythonu

[https://benchmarksgame-team.pages.debian.net/benchmarksgame/fastest/python3-gcc.html](https://benchmarksgame-team.pages.debian.net/benchmarksgame/fastest/python3-gcc.html)

---

### Řešený problém

* Dynamické typování + přetížené operátory
* Základní vlastnosti Pythonu

@ cython-1.py

---

### Jak tento problém vyřešit?

* AOT překladač
   - Cython
* JIT překladač
   - Numba

---

### Cython

* Nadmnožina Pythonu
    - (což už neplatí)
* Překládaný jazyk
    - jedná se o transpiler do jazyka C
    - `.pyx` -> `.c` -> `.so` -> `launch.py`
* Explicitní datové typy jsou nepovinné
* `nogil`
* Volání nativních funkcí

---

#### Překlad do C

@ cython-2.pyx

---

#### Explicitní typy parametrů

@ cython-3.pyx

---

### Zákaz GILu

@ cython-4.pyx

---

### Zavolání standardní C funkce

@ cython-5.pyx

---

### Numba

* JIT pro Python

---

### Dekorátor @jit

@ numba-1.py

---

### Jednodušší a rychlejší `print`

* Pouze pro čísla a řetězce
* Bez nepovinných argumentů `file` a `sep`

---

### Vynucení JITu

@ numba-2.py

---

### Porovnání výkonnosti

* ANSI C: ANSI C (ne Python)
* Cython #1: základní varianta
* Cython #2: bez typových informací
* Cython #3: optimalizace + `nogil`
* Numba #1: původní varianta
* Numba #2: s dekorátorem `@jit`
* Numba #3: nativní funkce `print`
* Numba #4: nativní funkce `print` + @jit(nopython=True)

---

### ANSI C: ANSI C (ne Python)

@ mandelbrot.c

---

### Cython #1: základní varianta

@ mandelbrot-1.pyx

---

### Cython #2: bez typových informací

@ mandelbrot-2.pyx

---

### Cython #3: optimalizace + `nogil`

@ mandelbrot-3.pyx

---

### Numba #1: původní varianta

@ mandelbrot-1.py

---

### Numba #2: s dekorátorem `@jit`

@ mandelbrot-2.py

---

### Numba #3: nativní funkce `print`

@ mandelbrot-3.py

---

### Numba #4: nativní funkce `print` + @jit(nopython=True)

@ mandelbrot-4.py

---

### Výsledky benchmarků 1/2

![images/benchmarks-1.png](images/benchmarks-1.png)

---

### Výsledky benchmarků 2/2

![images/benchmarks-2.png](images/benchmarks-2.png)

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

### Transpilery

* "Code to code compilers"
    - transformace kódu mezi dvěma jazyky
    - použito právě pro konverzi do JavaScriptu
* AOT nebo JIT

---

### Mnoho typů transpilerů

```
#   Jazyk či transpřekladač Poznámka
1   CoffeeScript            přidání syntaktického cukru do JavaScriptu
2   ClojureScript           překlad aplikací psaných v Clojure do JavaScriptu
3   TypeScript              nadmnožina jazyka JavaScript, přidání datových typů
4   6to5                    transpřeklad z ECMAScript 6 (nová varianta JavaScriptu) do starší varianty JavaScriptu
5   Kaffeine                rozšíření JavaScriptu o nové vlastnosti
6   RedScript               jazyk inspirovaný Ruby
7   GorillaScript           další rozšíření JavaScriptu
8   ghcjs                   transpřekladač pro fanoušky programovacího jazyka Haskell
9   Haxe                    transpřekladač, mezi jehož cílové jazyka patří i Java a JavaScript
10  Wisp                    transpřekladač jazyka podobného Clojure, opět do JavaScriptu
11  ScriptSharp             transpřekladač z C# do JavaScriptu
12  Dart                    transpřekladač z jazyka Dart do JavaScriptu
13  COBOL → C               transpřekladač OpenCOBOL
14  COBOL → Java            transpřekladač P3COBOL
15  lua2js                  transpřekladač jazyka Lua, opět do JavaScriptu
16  Coconut                 transpřekladač jazyka Coconut do Pythonu
```

---

### Brython

* Transpiler Python -> JavaScript
* JIT
    - kód se překládá až při inicialiazi stránky
    - jakékoli úpravy se ihned projeví po F5

---

### Transcrypt

* Transpiler Python -> JavaScript
* AOT
    - výsledný JS lze načíst do webové stránky
* Podpora DOM
* `print` na konzoli
    - plus většina standardních funkcí Pythonu
* Malý runtime
    - cca 20kB
* Podpora Numscryptu
    - (nedokonalá) varianta Numpy

---

### Základní datové typy (seznamy)

@ transcrypt-lists.py

---

### Základní datové typy (seznamy)

@ transcrypt-lists.js

---

### Základní datové typy (slovníky)

@ transcrypt-maps.py

---

### Základní datové typy (slovníky)

@ transcrypt-maps.js

---

### Funkce

@ transcrypt-adder.py

---

### Funkce

@ transcrypt-adder.js

---

### Uzávěry

@ transcrypt-counter-closure.py

---

### Uzávěry

@ transcrypt-counter-closure.js

---

### Komunikace s webovou stránkou

* Skript v Pythonu

@ transcrypt-hello.py

---

### Komunikace s webovou stránkou

* Výsledek transpřekladu

@ transcrypt-hello.js

---

### Kreslení na canvas

* Skript v Pythonu

@ transcrypt-canvas1.py

---

### Kreslení na canvas

* Výsledek transpřekladu

@ transcrypt-canvas1.js

---

### Kreslení na canvas

* Podpůrná HTML stránka s canvasem

@ transcrypt-canvas1.html

---

# Alternativní projekty a jazyky

![Python](images/python.png)

---

## Alterntivní projekty a jazyky

* Coconut
* Mojo

---

### Coconut

* Jazyk překládaný do JavaScriptu
* Nové jazykové konstrukce
* Vylepšené jazykové konstrukce

---

### Hello world

@ coconut-01-hello-world.coco

---

### Hello world

@ coconut-01-hello-world.py

---

### Sekvence

@ coconut-02-sequences.coco

---

### Sekvence
@ coconut-02-sequences.py

---

### Anonymní funkce

@ coconut-03-anonymous-functions.coco

---

### Anonymní funkce

@ coconut-03-anonymous-functions.py

---

### Neměnitelné datové typy

@ coconut-04-immutable-types.coco

---

### Neměnitelné datové typy

@ coconut-04-immutable-types.py

---

### Infixová notace

@ coconut-05-infix-notation.coco

---

### Infixová notace

@ coconut-05-infix-notation.py

---

### Kolony

@ coconut-06-pipeline.coco

---

### Kolony: po překladu

@ coconut-06-pipeline-compiled.py

---

### Kolony: původní kód

@ coconut-06-pipeline-compiled-original-code.py

---

### Kolony: čísla řádků

@ coconut-06-pipeline-compiled-line-numbers.py

---

### Kompozice funkcí

@ coconut-07-function-composition.coco

---

### Kompozice funkcí

@ coconut-07-function-composition.py

---

### Zřetězení operací

@ coconut-08-generator-chaining.coco

---

### Zřetězení operací

@ coconut-08-generator-chaining.py

---

### Operátor ??

@ coconut-09-??-operator.coco

---

### Operátor ??

@ coconut-09-??-operator.py

---

### Operátor ??=

@ coconut-10-??=-operator.coco

---

### Operátor ??=

@ coconut-10-??=-operator.py

---

### Elvisův operátor

@ coconut-11-elvis-operator.coco

---

### Elvisův operátor

@ coconut-11-elvis-operator.py

---

### Podpora Unicode

@ coconut-12-unicode-chars.coco

---

### Podpora Unicode

@ coconut-12-unicode-chars.py

---

### Pattern matching

@ coconut-13-pattern-matching.coco

---

### Pattern matching

@ coconut-13-pattern-matching.py

---

### Pattern matching

@ coconut-14-pattern-matching-2.coco

---

### Pattern matching

@ coconut-14-pattern-matching-2.py

---

### TCO

@ coconut-15-tail-call-optimization.coco

---

### TCO

@ coconut-15-tail-call-optimization.py

---

### Mojo

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

