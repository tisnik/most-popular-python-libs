"""Vyhledávání vektorů na základě jejich podobnosti, použití odlišné metriky s normalizovanými vektory."""

import numpy as np
from pymilvus import MilvusClient
from pprint import pprint

# inicializace klienta pro připojení k vektorové databázi
milvus_client = MilvusClient(uri="./hf_milvus_demo.db")

# jméno databáze
COLLECTION_NAME = "milvus_db_6"

# počet dimenzí uložených vektorů
EMDEDDING_DIM = 2

# použitá metrika
SIMILARITY_METRICS = "IP"

# pokud datáze existuje, odstraníme ji
if milvus_client.has_collection(COLLECTION_NAME):
    milvus_client.drop_collection(COLLECTION_NAME)

# vytvoření databáze
milvus_client.create_collection(
    collection_name=COLLECTION_NAME,
    dimension=EMDEDDING_DIM,
    metric_type=SIMILARITY_METRICS,
    consistency_level="Strong",
)

# x-ové souřadnice bodů v rovině
x = [-5, -4, -3,    3,  4,  5,   3, 3, 3,  4, 4, 4,  5, 5, 5]

# y-ové souřadnice bodů v rovině
y = [ 5,  3,  5,   -5, -3, -5,   3, 4, 5,  3, 4, 5,  3, 4, 5]

# příprava datové struktury pro zápis do databáze
data = []

for i in range(len(x)):
    vec = [x[i], y[i]]
    normalized = vec / np.linalg.norm(vec)
    print(i, normalized)
    # další záznam
    data.append({"id": i, "vector": normalized, "text": f"vector [{x[i]}, {y[i]}]"})

# strukturu před uložením do databáze zobrazíme
print(data)

# provedení zápisu
insert_res = milvus_client.insert(collection_name=COLLECTION_NAME, data=data)
print("Insertions: ", insert_res["insert_count"])

print("-" * 50)
print("Searching:")

# vyhledávaný vektor
vector_to_search = [3, 3]
normalized = vec / np.linalg.norm(vec)

# pokusíme se nalézt čtyři nejbližší vektory
search_res = milvus_client.search(
    collection_name=COLLECTION_NAME,
    data=[normalized],
    limit=4,
    search_params={"metric_type": SIMILARITY_METRICS, "params": {}},
    output_fields=["text"],
)

# výpis výsledků
for vector in search_res[0]:
    print(vector)
