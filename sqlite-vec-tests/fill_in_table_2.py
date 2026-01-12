# Knihovna SQLite s rozšířením SQLite-vec
#
# - připojení k databázi uložené v souboru
# - databáze je v případě potřeby vytvořena
# - načtení rozšíření SQLite-vec
# - vytvoření virtuální tabulky
# - naplnění tabulky patnácti vektory

import sqlite3
import sqlite_vec

# připojení k databázi uložené v souboru
# v případě potřeby je databáze vytvořena
with sqlite3.connect("v2.db") as db:
    # načtení rozšíření SQLite-vec
    db.enable_load_extension(True)
    sqlite_vec.load(db)
    db.enable_load_extension(False)

    table_statement = """
    CREATE virtual TABLE v2 USING vec0(
        embedding float[2]
    );
    """

    db.execute(table_statement)

    INSERT_STATEMENT = "INSERT INTO v2(rowid, embedding) VALUES(?, ?)"

    data_to_insert = [
        [1, [-5,  5]],
        [2, [-4,  3]],
        [3, [-3,  5]],
        [4, [ 3, -5]],
        [5, [ 4, -3]],
        [6, [ 5, -5]],
        [7, [ 3,  3]],
        [8, [ 3,  4]],
        [9, [ 3,  5]],
        [10, [ 4,  3]],
        [11, [ 4,  4]],
        [12, [ 4,  5]],
        [13, [ 5,  3]],
        [14, [ 5,  4]],
        [15, [ 5,  5]],
    ]

    for data in data_to_insert:
        print(f"Inserting {data[1]}")
        db.execute(INSERT_STATEMENT, [data[0], sqlite_vec.serialize_float32(data[1])])

    db.commit()
