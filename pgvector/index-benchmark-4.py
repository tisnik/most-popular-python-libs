# Rozšíření pgvector pro databázi PostgreSQL
#
# - příprava pro benchmark rozšíření pgvector
# - vytvoření tabulky používané benchmarkem
# - je použit výchozí index
# - zápis vektorů do nově vytvořené tabulky
# - průběžně se mění počet dimenzí
# - měří se časy zápisu vektorů
# - vizualizace výsledků formou grafu

from time import time

import psycopg2
from pgvector.psycopg2 import register_vector

import matplotlib.pyplot as plt
import numpy as np

# parametry benchmarku
VECTOR_COUNT = 20000
MAX_DIMENSIONS = 1024
STEPS = 16


def create_vector_table(connection, dimensions, print_tables=True):
    """Vytvoření tabulky obsahující sloupec s vektory."""
    DROP_TABLE_STATEMENT = """
        DROP TABLE IF EXISTS v3
    """

    CREATE_TABLE_STATEMENT = """
        CREATE TABLE IF NOT EXISTS v3 (
            id bigserial PRIMARY KEY,
            embedding vector(%s) NOT NULL
        );
    """

    LIST_TABLES_QUERY = """
        SELECT table_schema,table_name
          FROM information_schema.tables
         WHERE table_schema='public'
         ORDER BY table_schema,table_name;
    """

    with connection.cursor() as cursor:
        cursor.execute(DROP_TABLE_STATEMENT)
        connection.commit()

        cursor.execute(CREATE_TABLE_STATEMENT, (dimensions,))
        connection.commit()

        cursor.execute(LIST_TABLES_QUERY)
        tables = cursor.fetchall()

        if print_tables:
            print("Tables in database:")
            for table in tables:
                print(f"    {table[0]}: {table[1]}")
            print()


def fill_in_vector_table(connection, dimensions, vector_count):
    """Naplnění tabulky náhodnými vektory."""
    t1 = time()
    with connection.cursor() as cursor:
        # prozatím budeme tabulku naplňovat po jednotlivých záznamech
        for i in range(vector_count):
            # náhodný vektor
            vector = np.random.rand(dimensions).astype("float32")
            cursor.execute("INSERT INTO v3 (embedding) VALUES (%s)", (vector,))
        connection.commit()
    t2 = time()
    return t2 - t1


def print_vector_count(connection):
    """Tisk počtu vektorů uložených v tabulce."""
    with connection.cursor() as cursor:
        cursor.execute("SELECT count(*) FROM v3")
        count = cursor.fetchone()
        print(f"Vectors stored in table v3: {count[0]}")


def display_graph(dimensions, time_inserts):
    """Vykreslení grafu s časem zápisu n-dimenzionálních vektorů do tabulky."""
    plt.xlabel("# dimensions")
    plt.ylabel("Time (sec)")
    plt.plot(dimensions, time_inserts, "m-", label="insertion")

    # přidání legendy
    plt.legend(loc="upper left")

    # povolení zobrazení mřížky
    plt.grid(True)

    plt.savefig("insert-benchmark-4.png")

    # zobrazení grafu
    plt.show()


def main():
    """Vstupní bod do benchmarku."""
    # připojení k databázi
    connection = psycopg2.connect(
        host="", port=5432, user="tester", password="123qwe", dbname="test"
    )

    try:
        # budeme používat rozšíření pgvector
        register_vector(connection)

        # benchmark - naplnění tabulky s vektory
        print("Dimensions", "Time")
        dimensions = []
        time_inserts = []

        for dimension in range(MAX_DIMENSIONS//STEPS, MAX_DIMENSIONS+1, MAX_DIMENSIONS//STEPS):
            # vytvoření tabulky s vektory
            create_vector_table(connection, dimension, print_tables=False)
            t = fill_in_vector_table(connection, dimension, VECTOR_COUNT)
            dimensions.append(dimension)
            time_inserts.append(t)
            print(dimension, t)

        display_graph(dimensions, time_inserts)

        # zjištění počtu skutečně uložených vektorů
        print_vector_count(connection)
    finally:
        connection.close()


# spuštění benchmarku
main()
