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

import sys

from kafka import KafkaConsumer

server = "localhost:9092"
topic = "greetings"
group_id = "group1"

print("Connecting to Kafka")
consumer = KafkaConsumer(
    topic, group_id=group_id,
    bootstrap_servers=[server],
    auto_offset_reset="earliest"
)
print("Connected to Kafka")

try:
    for message in consumer:
        print(
            "%s:%d:%d: key=%s value=%s"
            % (
                message.topic,
                message.partition,
                message.offset,
                message.key,
                message.value,
            )
        )
except KeyboardInterrupt:
    sys.exit()
