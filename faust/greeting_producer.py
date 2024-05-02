#!/usr/bin/env python3

from time import sleep

from kafka import KafkaProducer

server = "localhost:9092"
topic = "greetings"

print("Connecting to Kafka")
producer = KafkaProducer(
    bootstrap_servers=[server],
    value_serializer=lambda x: x.encode("utf-8")
)
print("Connected to Kafka")

for i in range(1000):
    print(i)
    message = f"Greeting #{i}"
    producer.send(topic, value=message)
    sleep(1)
