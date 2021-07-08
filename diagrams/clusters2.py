#
#  (C) Copyright 2021  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

from diagrams import Diagram
from diagrams import Cluster
from diagrams.onprem.queue import Kafka, ActiveMQ
from diagrams.programming.language import Go, Rust
from diagrams.aws.database import RDS

with Diagram("Clusters #2", show=True, direction="LR"):
    # definice clusteru
    with Cluster("Input processor"):
        # definice uzlu v clusteru
        consumer = Kafka("input stream")

        # rozvetveni
        workersA = [Go("worker #1"),
                    Go("worker #2"),
                    Go("worker #3")]

        db = RDS("storage")

    # definice uzlu mimo cluster
    buffer = ActiveMQ("buffer")

    # rozvetveni
    workersB = [Rust("worker #1"),
                Rust("worker #2"),
                Rust("worker #3")]

    producer = Kafka("output stream")

    # propojeni uzlu grafu orientovanymi hranami
    consumer >> workersA >> buffer >> workersB >> producer
    db >> workersA
