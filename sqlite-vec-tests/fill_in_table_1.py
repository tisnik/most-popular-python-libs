# Knihovna SQLite s rozšířením SQLite-vec
#
# - připojení k databázi uložené v souboru
# - databáze je v případě potřeby vytvořena
# - načtení rozšíření SQLite-vec
# - vytvoření virtuální tabulky
# - naplnění tabulky několika vektory

import sqlite3
import sqlite_vec

# připojení k databázi uložené v souboru
# v případě potřeby je databáze vytvořena
with sqlite3.connect("v2.db") as db:
    # načtení rozšíření SQLite-vec
    db.enable_load_extension(True)
    sqlite_vec.load(db)
    db.enable_load_extension(False)

    TABLE_STATEMENT = """
        CREATE virtual TABLE v2 USING vec0(
            embedding float[2]
        );
    """

    db.execute(TABLE_STATEMENT)

    INSERT_STATEMENT = "INSERT INTO v2(embedding) VALUES(?)"

    db.execute(INSERT_STATEMENT, [sqlite_vec.serialize_float32([1, 2])])
    db.execute(INSERT_STATEMENT, [sqlite_vec.serialize_float32([1, 2])])
    db.execute(INSERT_STATEMENT, [sqlite_vec.serialize_float32([1, 2])])

    db.commit()
