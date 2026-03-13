# Rozšíření pgvector pro databázi PostgreSQL
#
# - vytvoření tabulky používané benchmarkem
# - je použit výchozí index
# - zápis vektorů do nově vytvořené tabulky
# - měří se časy vyhledávání vektorů podle různých kritérií
# - vizualizace výsledků formou grafu

from time import time

import psycopg2
from pgvector.psycopg2 import register_vector

import matplotlib.pyplot as plt
import numpy as np

# parametry benchmarku
DIMENSIONS = 256
MAX_VECTOR_COUNT = 10000
STEPS = 10
REPEAT_COUNT = 100


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


def distance_function_to_operator(distance_function):
    operators = {
            "l1": "<+>",
            "l2": "<->",
            "inner product": "<#>",
            "cosine": "<=>",
    }
    return operators[distance_function]


def similarity_search(connection, dimensions, vector_count, repeat_count=1, distance_function="l2"):
    """Vyhledávání na základě podobnosti vektorů."""
    operator = distance_function_to_operator(distance_function)

    query = f"""
        SELECT embedding
          FROM v3
         ORDER BY embedding {operator} %s::vector
         LIMIT 5
    """

    t1 = time()
    with connection.cursor() as cursor:
        for i in range(repeat_count):
            vector = np.random.rand(dimensions).astype("float32")
            cursor.execute(query, (vector, ))
            records = cursor.fetchall()
            assert len(records) == min(vector_count, 5)
    t2 = time()
    return t2 - t1


def print_vector_count(connection):
    """Tisk počtu vektorů uložených v tabulce."""
    with connection.cursor() as cursor:
        cursor.execute("SELECT count(*) FROM v3")
        count = cursor.fetchone()
        print(f"Vectors stored in table v3: {count[0]}")


def display_graph(distance_functions, vector_count, time_search):
    """Vykreslení grafu s časy vyhledávání n-dimenzionálních vektorů."""
    plt.xlabel("# vectors")
    plt.ylabel("Time (sec)")
    for distance_function in distance_functions:
        plt.plot(vector_count, time_search[distance_function], label=distance_function)

    # přidání legendy
    plt.legend(loc="upper left")

    # povolení zobrazení mřížky
    plt.grid(True)

    plt.savefig("insert-benchmark-6.png")

    # zobrazení grafu
    plt.show()


def main():
    """Vstupní bod do benchmarku."""
    # připojení k databázi
    connection = psycopg2.connect(
        host="", port=5432, user="tester", password="123qwe", dbname="test"
    )

    distance_functions = (
        #"l1",
        "l2",
        "cosine",
        "inner product",
    )

    try:
        # budeme používat rozšíření pgvector
        register_vector(connection)

        # benchmark - vyhledávání v tabulce s vektory
        print("Vector count", "Function", "Time")
        vectors_inserted = []
        time_search = {}

        # příprava slovníku seznamů
        for distance_function in distance_functions:
            time_search[distance_function] = []

        for vector_count in range(0, MAX_VECTOR_COUNT+1, MAX_VECTOR_COUNT//STEPS):
            # vytvoření tabulky s vektory
            create_vector_table(connection, DIMENSIONS, print_tables=False)
            fill_in_vector_table(connection, DIMENSIONS, vector_count)

            for distance_function in distance_functions:
                t = similarity_search(connection, DIMENSIONS, vector_count, REPEAT_COUNT, distance_function) 
                time_search[distance_function].append(t)
                print(vector_count, distance_function, t)

            vectors_inserted.append(vector_count)

        display_graph(distance_functions, vectors_inserted, time_search)
    finally:
        connection.close()


# spuštění benchmarku
main()
