# Knihovna SQLite s rozšířením SQLite-vec
#
# - připojení k databázi uložené v souboru
# - databáze je v případě potřeby vytvořena
# - načtení rozšíření SQLite-vec
# - vytvoření virtuální tabulky s jedním sloupcem
# - nepoužívá se kurzor (zkrácený zápis)

import sqlite3
import sqlite_vec

# připojení k databázi uložené v souboru
# v případě potřeby je databáze vytvořena
db = sqlite3.connect("v1.db")

# načtení rozšíření SQLite-vec
db.enable_load_extension(True)
sqlite_vec.load(db)
db.enable_load_extension(False)

TABLE_STATEMENT = """
    CREATE virtual TABLE v1 USING vec0(
        embedding float[2]
    );
"""

# vytvoření virtuální tabulky
result = db.execute(TABLE_STATEMENT)
print(result)

db.commit()
db.close()
