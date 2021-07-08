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
from diagrams.aws.compute import EC2
from diagrams.aws.integration import SQS

# novy graf s urcenim jeho zakladnich vlastnosti
with Diagram("AWS", show=True, direction="TB"):
    # definice uzlu
    consumer = SQS("input stream")

    # rozvetveni
    workers = [EC2("worker #1"),
               EC2("worker #2"),
               EC2("worker #3")]

    producer = SQS("output stream")

    # propojeni uzlu grafu orientovanymi hranami
    consumer >> workers >> producer
