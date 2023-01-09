#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import polars

# connection string a vlastní dotaz
connection_string = "postgresql://postgres:postgres@localhost:5432/testdb"
query = """
    SELECT org_id, cluster_id, rule_fqdn
      FROM rule_hit
     ORDER by org_id, cluster_id
"""

# přečtení zdrojových dat
df = polars.read_sql(query, connection_string)

# zobrazíme datový rámec
print(df)
print()

# podrobnější informace o datovém rámci
print("Column types")
print(df.dtypes)
print()
