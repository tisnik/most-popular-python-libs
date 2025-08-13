import psycopg2
from pgvector.psycopg2 import register_vector

from sentence_transformers import SentenceTransformer
import faiss


connection = psycopg2.connect(
    host="", port=5432, user="tester", password="123qwe", dbname="test"
)

print(connection)
register_vector(connection)


model = SentenceTransformer("paraphrase-MiniLM-L6-v2")
print(model)


def find_similar_sentences(connection, query_sentence, k):
    print(f"Query: {query_sentence}")
    print(f"Most {k} similar sentences:")

    vector = model.encode(query_sentence)

    with connection.cursor() as cursor:
        query = """
            SELECT id, embedding
              FROM v384
             ORDER BY embedding <-> %s::vector
             LIMIT %s
        """
        cursor.execute(query, (vector, k))
        records = cursor.fetchall()
        for record in records:
            print(record[0])
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

