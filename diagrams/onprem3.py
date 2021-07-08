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

with Diagram("OnPrem #3", show=True, direction="TB"):
    # definice uzlu
    consumer = Kafka("input stream")

    # rozvetveni
    workers = [Go("worker #1"),
               Go("worker #2"),
               Go("worker #3")]

    producer = Rabbitmq("output stream")

    # propojeni uzlu grafu orientovanymi hranami
    consumer >> workers >> producer
