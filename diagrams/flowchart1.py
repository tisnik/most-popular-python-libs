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
from diagrams.programming.flowchart import StartEnd

# novy graf s urcenim jeho zakladnich vlastnosti
with Diagram("Flow chart #1", show=False):
    # definice uzlu grafu
    start = StartEnd("Start")

    # definice uzlu grafu
    end = StartEnd("End")

    # propojeni uzlu grafu orientovanymi hranami
    start >> end
