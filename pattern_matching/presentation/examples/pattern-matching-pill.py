from enum import Enum


class Color(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2

match pill:
    case Color.RED:
        print("you stay in Wonderland, and I show you how deep the rabbit hole goes.")
    case Color.BLUE:
        print("the story ends, you wake up in your bed and believe whatever you want to believe")
    case _:
        print("this does not compute")
