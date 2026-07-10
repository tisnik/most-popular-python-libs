"""Zápis vektorů s přidanými texty do databáze."""

from pymilvus import MilvusClient, DataType

# inicializace klienta pro připojení k vektorové databázi
milvus_client = MilvusClient(uri="./hf_milvus_demo.db")

# jméno databáze
COLLECTION_NAME = "milvus_db_4"

# počet dimenzí uložených vektorů
EMDEDDING_DIM = 2

# použitá metrika
SIMILARITY_METRICS = "foo"

# pokud datáze existuje, odstraníme ji
if milvus_client.has_collection(COLLECTION_NAME):
    milvus_client.drop_collection(COLLECTION_NAME)

# konstrukce schématu databáze
schema = milvus_client.create_schema(
    auto_id=True,
    enable_dynamic_fields=True,
)

# specifikace jednotlivých sloupců
schema.add_field(field_name="id", datatype=DataType.INT64, is_primary=True, max_length=100)
schema.add_field(field_name="vector_1", datatype=DataType.FLOAT_VECTOR, dim=2)
schema.add_field(field_name="vector_2", datatype=DataType.FLOAT_VECTOR, dim=10)

# vytvoření databáze
milvus_client.create_collection(
    collection_name=COLLECTION_NAME,
    dimension=EMDEDDING_DIM,
    metric_type=SIMILARITY_METRICS,
    consistency_level="Strong",
    # nastavení schématu
    schema=schema,
)

from pymilvus import MilvusClient, DataType


# x-ové souřadnice bodů v rovině
x = [-5, -4, -3,    3,  4,  5,   3, 3, 3,  4, 4, 4,  5, 5, 5]

# y-ové souřadnice bodů v rovině
y = [ 5,  3,  5,   -5, -3, -5,   3, 4, 5,  3, 4, 5,  3, 4, 5]

# příprava datové struktury pro zápis do databáze
data = []

for i in range(len(x)):
    vec1 = [x[i], y[i]]
    vec2 = [x[i], y[i], x[i], y[i], i, i, i, 0, 1, 2]
    print(i, vec1, vec2)
    # další záznam
    data.append({"id": i, "vector_1": vec1, "vector_2": vec2})

# strukturu před uložením do databáze zobrazíme
print(data)

# provedení zápisu
insert_res = milvus_client.insert(collection_name=COLLECTION_NAME, data=data)
print("Insertions: ", insert_res["insert_count"])

