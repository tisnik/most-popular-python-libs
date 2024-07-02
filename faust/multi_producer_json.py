#!/usr/bin/env python3
#
#  (C) Copyright 2024  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

from time import sleep

from kafka import KafkaProducer

server = "localhost:9092"
topic1 = "greetings"
topic2 = "real_work"

print("Connecting to Kafka")
producer = KafkaProducer(
    bootstrap_servers=[server],
    value_serializer=lambda x: x.encode("utf-8")
)
print("Connected to Kafka")

for i in range(1000):
    print(i)
    message = {"subject": "Greeting", "value": i}
    producer.send(topic1, value=message)
    sleep(1)
    work = {"subject": "Real work", "value": i*2}
    producer.send(topic2, value=work)
    work = {"subject": "Real work", "value": i*2+1}
    producer.send(topic2, value=work)
    sleep(1)
