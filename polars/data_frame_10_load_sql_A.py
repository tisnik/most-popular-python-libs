#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import polars

# connection string a vlastní dotaz
connection_string = "postgresql://postgres:postgres@localhost:5432/testdb"
query = "select * from rule_hit"

# přečtení zdrojových dat
df = polars.read_sql(query, connection_string)

# zobrazíme datový rámec
print(df)
print()

# podrobnější informace o datovém rámci
print("Column types")
print(df.dtypes)
print()
