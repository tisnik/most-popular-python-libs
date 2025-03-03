import psycopg2

from pgvector.psycopg2 import register_vector

connection = psycopg2.connect(
    host="", port=5432, user="tester", password="123qwe", dbname="test"
)

register_vector(connection)


def list_by_distance(title, query):
    print(title)
    print("-" * 70)
    with connection.cursor() as cursor:
        cursor.execute(query, ([0.6, 0.8], ))
        records = cursor.fetchall()
        for record in records:
            print(record[0], record[1])
    print()


query_l2_distance = """
        SELECT embedding, embedding <-> %s::vector as distance
          FROM normalized
         ORDER BY distance
    """


query_cosine_distance = """
        SELECT embedding, embedding <=> %s::vector as distance
          FROM normalized
         ORDER BY distance
    """


query_inner_product_distance = """
        SELECT embedding, (embedding <#> %s::vector) * -1 as distance
          FROM normalized
         ORDER BY distance
    """


list_by_distance("L2", query_l2_distance)
list_by_distance("cosine", query_cosine_distance)
list_by_distance("inner product", query_inner_product_distance)
