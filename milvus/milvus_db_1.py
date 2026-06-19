"""Připojení k vektorové databázi."""

from pymilvus import MilvusClient

# inicializace klienta pro připojení k vektorové databázi
milvus_client = MilvusClient(uri="./hf_milvus_demo.db")

# jméno databáze
COLLECTION_NAME = "milvus_db_1"

# počet dimenzí uložených vektorů
EMDEDDING_DIM = 2

# použitá metrika
SIMILARITY_METRICS = "L2"

# vytvoření databáze
milvus_client.create_collection(
    collection_name=COLLECTION_NAME,
    dimension=EMDEDDING_DIM,
    metric_type=SIMILARITY_METRICS,
    consistency_level="Strong",
)
