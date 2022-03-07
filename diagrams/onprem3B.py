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
from diagrams.onprem.queue import Kafka, Rabbitmq
from diagrams.programming.language import Go

# definice diagramu se specifikaci jeho zakladnich vlastnosti
with Diagram("OnPrem #3", show=True, direction="BT"):
    # definice uzlu - konzument
    consumer = Kafka("input stream")

    # rozvetveni - vetsi mnozstvi workeru
    workers = [Go("worker #1"), Go("worker #2"), Go("worker #3")]

    # definice uzlu - producent
    producer = Rabbitmq("output stream")

    # propojeni uzlu grafu orientovanymi hranami
    consumer >> workers >> producer
