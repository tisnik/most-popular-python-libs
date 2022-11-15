from rich.console import Console
from time import sleep

console = Console()


def perform_computation(x, y):
    dictionary = {}
    dictionary["x"] = x
    dictionary["y"] = y

    try:
        z = x / y
        dictionary["result"] = z
        dictionary["success"] = True
    except Exception as e:
        dictionary["success"] = False
        dictionary["errors"] = e

    console.log(dictionary, log_locals=True)
    return dictionary


perform_computation(1, 2)
sleep(1)
perform_computation(1, 0)
sleep(1)
perform_computation("foo", 0)
