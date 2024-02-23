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

@ pyproject.toml

---

## Kostra aplikace

* handler pro jediný "endpoint"
* automatický Swagger

@ main1.py

---

## První úpravy

* větší množství handlerů (CRUD)
* asynchronní handlery
* typové anotace
    - automatické odvození formátu dotazů
    - odpovědi ve funkcionálním stylu

---

## Výsledek prvních úprav

@ main2.py

---

## Jednoduchá "databáze"

@ main3.py

---

## Reakce na chyby

* vracet lze libovolné HTTP stavy

@ main4.py

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

@ pyproject2.toml

---

### Implementace základních CRUD operací

@ main5.py
