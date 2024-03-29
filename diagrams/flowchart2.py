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
from diagrams.programming.flowchart import Action, InputOutput, StartEnd

# novy graf s urcenim jeho zakladnich vlastnosti
with Diagram("Flow chart #2", show=False):
    # definice uzlu
    start = StartEnd("Start")
    input = InputOutput("radius=")

    # slozitejsi text v uzlu
    computation = Action("area=pi*radius^2")
    display = InputOutput("circle area=area")
    end = StartEnd("End")

    # propojeni uzlu grafu orientovanymi hranami
    start >> input >> computation >> display >> end
