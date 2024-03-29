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

# novy graf s urcenim jeho zakladnich vlastnosti
with Diagram("OnPrem #1", show=True):
    # definice uzlu - konzument
    consumer = Kafka("input stream")

    # definice uzlu - worker
    worker = Go("worker")

    # definice uzlu - producent
    producer = Rabbitmq("output stream")

    # propojeni uzlu grafu orientovanymi hranami
    consumer >> worker >> producer
