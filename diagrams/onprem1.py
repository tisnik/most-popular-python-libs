from diagrams import Diagram
from diagrams.onprem.queue import Kafka, Rabbitmq
from diagrams.programming.language import Go

# novy graf s urcenim jeho zakladnich vlastnosti
with Diagram("OnPrem #1", show=True):
    # definice uzlu
    consumer = Kafka("input stream")

    worker = Go("worker")

    producer = Rabbitmq("output stream")

    # propojeni uzlu grafu orientovanymi hranami
    consumer >> worker >> producer
