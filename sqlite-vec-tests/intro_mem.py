# Knihovna SQLite s rozšířením SQLite-vec
#
# - připojení k databázi uložené v paměti
# - databáze je (nutně) vždy vytvořena
# - načtení rozšíření SQLite-vec
# - tisk verze rozšíření SQLite-vec

import sqlite3
import sqlite_vec

# připojení k databázi uložené v paměti
# databáze je vždy vytvořena
db = sqlite3.connect(":memory:")

# načtení rozšíření SQLite-vec
db.enable_load_extension(True)
sqlite_vec.load(db)
db.enable_load_extension(False)

# tisk verze rozšíření SQLite-vec
vec_version, = db.execute("select vec_version()").fetchone()
print(f"vec_version={vec_version}")
