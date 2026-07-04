"""Zobrazení dokumentace k metodě MilvusClient.has_collection."""

from pymilvus import MilvusClient

# inicializace klienta pro připojení k vektorové databázi
milvus_client = MilvusClient(uri="./hf_milvus_demo.db")

help(milvus_client.has_collection)
