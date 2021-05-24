from diagrams import Diagram
from diagrams.onprem.queue import Kafka, ActiveMQ
from diagrams.programming.language import Go, Rust
from diagrams.aws.database import RDS

with Diagram("OnPrem #6", show=True, direction="TB"):
    # definice uzlu
    consumer = Kafka("input stream")

    db = RDS("storage")

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
    db >> workersA
    producer >> db
