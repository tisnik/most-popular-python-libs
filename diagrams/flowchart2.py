from diagrams import Diagram
from diagrams.programming.flowchart import StartEnd
from diagrams.programming.flowchart import InputOutput
from diagrams.programming.flowchart import Action

# novy graf s urcenim jeho zakladnich vlastnosti
with Diagram("Flow chart #2", show=False):
    # definice uzlu
    start = StartEnd("Start")
    input = InputOutput("radius=")
    computation = Action("area=pi*radius^2")
    display = InputOutput("circle area=area")
    end = StartEnd("End")

    # propojeni uzlu grafu orientovanymi hranami
     >> input >> computation >> display >> end
