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
from diagrams.aws.database import RDS
from diagrams.onprem.queue import ActiveMQ, Kafka
from diagrams.programming.language import Go, Rust

# definice diagramu se specifikaci jeho zakladnich vlastnosti
with Diagram("OnPrem #6", show=True, direction="TB"):
    # definice uzlu - konzument
    consumer = Kafka("input stream")

    # definice uzlu - databaze
    db = RDS("storage")

    # rozvetveni - vetsi mnozstvi workeru
    workersA = [Go("worker #1"), Go("worker #2"), Go("worker #3")]

    # buffer vlozeny mezi skupiny workeru
    buffer = ActiveMQ("buffer")

    # rozvetveni - vetsi mnozstvi workeru
    workersB = [Rust("worker #1"), Rust("worker #2"), Rust("worker #3")]

    # definice uzlu - producent
    producer = Kafka("output stream")

    # propojeni uzlu grafu orientovanymi hranami
    consumer >> workersA >> buffer >> workersB >> producer
    db >> workersA
    producer >> db
