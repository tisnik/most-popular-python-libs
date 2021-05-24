from diagrams import Diagram
from diagrams.onprem.queue import Kafka, ActiveMQ
from diagrams.programming.language import Go, Rust

with Diagram("OnPrem #4", show=True, direction="TB"):
    # definice uzlu
    consumer = Kafka("input stream")

    # rozvetveni
    workersA = [Go("worker #1"),
                Go("worker #2"),
                Go("worker #3")]

    buffer = ActiveMQ("buffer")

    # rozvetveni
    workersB = [Rust("worker #1"),
                Rust("worker #2"),
                Rust("worker #3")]

    producer = Kafka("output stream")

    # propojeni uzlu grafu orientovanymi hranami
    consumer >> workersA >> buffer >> workersB >> producer
