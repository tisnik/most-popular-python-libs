import psycopg2
from sentence_transformers import SentenceTransformer

from pgvector.psycopg2 import register_vector

connection = psycopg2.connect(
    host="localhost", port=54321, user="tester", password="123qwe", dbname="test"
)

print(connection)
register_vector(connection)


model = SentenceTransformer("mixedbread-ai/mxbai-embed-large-v1")
print(model)


def find_similar_sentences(connection, query_sentence, k):
    print(f"Query: {query_sentence}")
    print(f"Most {k} similar sentences:")

    vector = model.encode(query_sentence, precision="ubinary")

    with connection.cursor() as cursor:
        query = """
            SELECT sentence
              FROM b2
             ORDER BY embedding <~> %s::bit(1024)
             LIMIT %s
        """
        ascii_vector = ""
        for i, byte in enumerate(vector):
            ascii_vector += format(byte, "08b")
        cursor.execute(query, (ascii_vector, k))
        records = cursor.fetchall()
        for i, record in enumerate(records):
            print(f"    #{i}: {record[0]}")
    print("-"*40)


find_similar_sentences(connection, "The quick brown fox jumps over the lazy dog", 3)
find_similar_sentences(connection, "quick brown fox jumps over lazy dog", 3)
find_similar_sentences(connection, "The quick brown fox jumps over the angry dog", 3)
find_similar_sentences(connection, "The quick brown cat jumps over the lazy dog", 3)
find_similar_sentences(connection, "What is your age?", 3)
find_similar_sentences(connection, "Shakespeare", 3)
find_similar_sentences(connection, "animal", 3)
find_similar_sentences(connection, "geometry", 3)
find_similar_sentences(connection, "weather", 3)

