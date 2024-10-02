# Strukturální pattern matching:
# - rozpoznání víceslovních příkazů


def perform_command():
    response = input("> ")

    match response.split():
        case ["quit"]:
            return "Quit"
        case ["list", "employees"]:
            return "List employees"
        case ["list", "departments"]:
            return "List departments"
        case ["list", "rooms"]:
            return "List rooms"
        case ["info", *subjects] if len(subjects) > 0:
            return f"Info about {len(subjects)} subjects '{subjects}'"
        case _:
            return "Wrong command"


print(perform_command())
