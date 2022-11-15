from rich.console import Console

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

    console.log(dictionary)
    return dictionary


perform_computation(1, 2)
perform_computation(1, 0)
