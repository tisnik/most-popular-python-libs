from diagrams import Diagram
from diagrams.onprem.queue import Kafka, Rabbitmq
from diagrams.programming.language import Go

with Diagram("OnPrem #3", show=True, direction="BT"):
    # definice uzlu
    consumer = Kafka("input stream")

    # rozvetveni
    workers = [Go("worker #1"),
               Go("worker #2"),
               Go("worker #3")]

    producer = Rabbitmq("output stream")

    # propojeni uzlu grafu orientovanymi hranami
    consumer >> workers >> producer
