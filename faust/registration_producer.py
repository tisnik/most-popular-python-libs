#!/usr/bin/env python3

from json import dumps

from kafka import KafkaProducer


def user(name, surname, id):
    return {
            "name": name,
            "surname": surname,
            "id": id
            }


server = "localhost:9092"
topic = "registrations"

print("Connecting to Kafka")
producer = KafkaProducer(
    bootstrap_servers=[server],
    value_serializer=lambda x: dumps(x).encode("utf-8")
)
print("Connected to Kafka")

producer.send(topic, value=user("Eliška", "Najbrtová", 4))
producer.send(topic, value=user("Jenny", "Suk", 3))
producer.send(topic, value=user("Anička", "Šafářová", 0))
producer.send(topic, value=user("Sváťa", "Pulec", 3))
producer.send(topic, value=user("Blažej", "Motyčka", 8))
producer.send(topic, value=user("Eda", "Wasserfall", 0))
producer.send(topic, value=user("Přemysl", "Hájek", 10))
producer.flush()

print("Done")
