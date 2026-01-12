# Knihovna SQLite s rozšířením SQLite-vec
#
# - připojení k databázi uložené v souboru
# - databáze je v případě potřeby vytvořena (nový soubor)
# - načtení rozšíření SQLite-vec
# - tisk verze rozšíření SQLite-vec

import sqlite3
import sqlite_vec

# připojení k databázi uložené v souboru
# v případě potřeby je databáze vytvořena
db = sqlite3.connect("v0.db")

# načtení rozšíření SQLite-vec
db.enable_load_extension(True)
sqlite_vec.load(db)
db.enable_load_extension(False)

# tisk verze rozšíření SQLite-vec
vec_version, = db.execute("select vec_version()").fetchone()
print(f"vec_version={vec_version}")
