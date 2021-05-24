from diagrams import Diagram
from diagrams.programming.flowchart import StartEnd

# novy graf s urcenim jeho zakladnich vlastnosti
with Diagram("Flow chart #1", show=False):
    # definice uzlu grafu
    start = StartEnd("Start")
    end = StartEnd("End")

    # propojeni uzlu grafu orientovanymi hranami
    start >> end
