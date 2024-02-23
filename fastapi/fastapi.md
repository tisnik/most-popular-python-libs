# FastAPI

---

## FastAPI

* 2018
* Swagger
* Pydantic
* Vhodné pro produkční nasazení

---

## Pydantic

* Pydantic
   - psáno v Rustu (rychlost)
   - typové informace
   - validace
   - serializace
   - deserializace

---

## Uvicorn

* asynchronous server gateway interface (ASGI)
* https://asgi.readthedocs.io/en/latest/

---

## CRUD

* Create
* Read
* Update
* Delete

---

## CRUD v SQL

* INSERT
* SELECT
* UPDATE
* DELETE

---

## Příprava kostry projektu

* `pdm`
* úprava `pyproject.toml`
   - příkaz pro spuštění 
---

## `pyproject.toml`

```python
[project]
name = ""
version = ""
description = ""
authors = [
    {name = "", email = ""},
]
dependencies = [
    "fastapi>=0.104.0",
    "uvicorn>=0.23.2",
]
requires-python = ">=3.11"
readme = "README.md"
license = {text = "MIT"}

[tool.pdm.scripts]
start = "uvicorn --app-dir src/example_package main:app --reload"
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/fastapi/sources//pyproject.toml)

---

## Kostra aplikace

* handler pro jediný "endpoint"
* automatický Swagger

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def origin():
    return {"message": "My first FastAPI app"}
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/fastapi/sources//main1.py)

---

## První úpravy

* větší množství handlerů (CRUD)
* asynchronní handlery
* typové anotace
    - automatické odvození formátu dotazů
    - odpovědi ve funkcionálním stylu

---

## Výsledek prvních úprav

```python
from fastapi import FastAPI

app = FastAPI()

@app.post("/create")
async def create_operation(text: str):
    return {"created": text}

@app.get("/")
async def read_operation():
    return {"list": None}

@app.put("/update/{id}")
async def update_operation(id: int, text: str = ""):
    pass

@app.delete("/delete/{id}")
async def delete_operation(id: int):
    return {"deleted": id}
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/fastapi/sources//main2.py)

---

## Jednoduchá "databáze"

```python
from fastapi import FastAPI

class Storage():
    def __init__(self):
        self._items = {}
        self._id = 0

    def create(self, text):
        self._id += 1
        self._items[self._id] = text
        return self._id

    def read(self):
        return self._items

    def update(self, id, text):
        self._items[id] = text

    def delete(self, id):
        del self._items[id]


storage = Storage()

app = FastAPI()

@app.post("/create")
async def create_operation(text: str):
    id = storage.create(text)
    return {"created": id}

@app.get("/")
async def read_operation():
    return {"list": storage.read()}

@app.put("/update/{id}")
async def update_operation(id: int, text: str = ""):
    storage.update(id, text)
    return {"updated": id, "new text": text}

@app.delete("/delete/{id}")
async def delete_operation(id: int):
    storage.delete(id)
    return {"deleted": id}
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/fastapi/sources//main3.py)

---

## Reakce na chyby

* vracet lze libovolné HTTP stavy

```python
from fastapi import FastAPI
from fastapi import HTTPException

class Storage():
    def __init__(self):
        self._items = {}
        self._id = 0

    def create(self, text):
        self._id += 1
        self._items[self._id] = text
        return self._id

    def read(self):
        return self._items

    def update(self, id, text):
        # test???
        self._items[id] = text

    def delete(self, id):
        del self._items[id]


storage = Storage()

app = FastAPI()

@app.post("/create")
async def create_operation(text: str):
    id = storage.create(text)
    return {"created": id}

@app.get("/")
async def read_operation():
    return {"list": storage.read()}

@app.put("/update/{id}")
async def update_operation(id: int, text: str = ""):
    try:
        storage.update(id, text)
        return {"updated": id, "new text": text}
    except:
        raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/delete/{id}")
async def delete_operation(id: int):
    try:
        storage.delete(id)
        return {"deleted": id}
    except:
        raise HTTPException(status_code=404, detail="Item not found")
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/fastapi/sources//main4.py)

---

## Reálná databáze

```
postgres=# CREATE USER tester WITH PASSWORD '123qwe';
CREATE ROLE
postgres=# CREATE DATABASE test1 OWNER tester;
CREATE DATABASE
postgres=# GRANT ALL PRIVILEGES ON DATABASE test1 TO tester;
GRANT
```

---

## SQLAlchemy

* installation

```python
[project]
name = ""
version = ""
description = ""
authors = [
    {name = "", email = ""},
]
dependencies = [
    "fastapi>=0.104.0",
    "uvicorn>=0.23.2",
    "sqlalchemy>=2.0.22",
    "psycopg2-binary>=2.9.9",
]
requires-python = ">=3.11"
readme = "README.md"
license = {text = "MIT"}

[tool.pdm.scripts]
start = "uvicorn --app-dir src/example_package main:app --reload"
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/fastapi/sources//pyproject2.toml)

---

### Implementace základních CRUD operací

```python
from fastapi import FastAPI

from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker


def connect_to_db():
    url = URL.create(
        drivername="postgresql",
        username="tester",
        password="123qwe",
        host="localhost",
        database="test1",
        port=5432
    )
    print("url", url)

    engine = create_engine(url)
    print("engine", engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    print("session", session)

    return engine, session


engine, session = connect_to_db()


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Record(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True)
    text = Column(String)


# inicializace
Base.metadata.create_all(engine)

app = FastAPI()


@app.post("/create")
async def create_operation(text: str):
    record = Record(text=text)
    session.add(record)
    session.commit()
    return {"created": record.id}

@app.get("/")
async def read_operation():
    record_query = session.query(Record)
    return {"list": record_query.all()}

@app.put("/update/{id}")
async def update_operation(id: int, text: str = ""):
    record_query = session.query(Record).filter(Record.id==id)
    record = record_query.first()
    record.text = text
    session.add(record)
    session.commit()

@app.delete("/delete/{id}")
async def delete_operation(id: int):
    record = session.query(Record).filter(Record.id==id).first()
    session.delete(record)
    session.commit()
    return {"todo deleted": record.id}
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/fastapi/sources//main5.py)
