# Strukturální pattern matching:
# - rozpoznání a zpracování příkazů zadaných uživatelem
# - ukázka použití vnořených řídicích struktur match.

def perform_command():
    # získat příkaz od uživatele
    response = input("> ")

    # rozvětvení na základě prvního slova
    match response.split():
        case ["quit"]:
            return "Quit"
        case ["list", obj]:
            # rozvětvení na základě druhého slova
            match obj:
                case "employees":
                    return "List employees"
                case "departments":
                    return "List departments"
                case "rooms":
                    return "List rooms"
                case _:
                    return "Invalid object: employees, departments, or rooms expected"
        case ["info", subject]:
            return f"Info about subject '{subject}'"
        case _:
            return "Wrong command"


print(perform_command())
