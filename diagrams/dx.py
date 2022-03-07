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

from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS, EKS, Lambda
from diagrams.aws.database import Redshift
from diagrams.aws.integration import SQS
from diagrams.aws.storage import S3

# definice diagramu se specifikaci jeho zakladnich vlastnosti
with Diagram("Event Processing", show=False):
    source = EKS("k8s source")

    # definice clusteru
    with Cluster("Event Flows"):
        # definice clusteru uvnitr clusteru
        with Cluster("Event Workers"):
            workers = [ECS("worker1"), ECS("worker2"), ECS("worker3")]

        # definice uzlu
        queue = SQS("event queue")

        # definice clusteru
        with Cluster("Processing"):
            handlers = [Lambda("proc1"), Lambda("proc2"), Lambda("proc3")]

    # definice uzlu
    store = S3("events store")
    dw = Redshift("analytics")

    # propojeni uzlu orientovanymi hranami
    source >> workers >> queue >> handlers

    # dalsi propojeni uzlu orientovanymi hranami
    handlers >> store

    # dalsi propojeni uzlu orientovanymi hranami
    handlers >> dw
