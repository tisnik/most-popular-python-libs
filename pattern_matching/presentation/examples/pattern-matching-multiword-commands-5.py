# Strukturální pattern matching:
# - rozpoznání a zpracování příkazů zadaných uživatelem
# - ukázka použití vnořených řídicích struktur match
# - omezení hodnoty druhého slova v příkazu "list"

def perform_command():
    # získat příkaz od uživatele
    response = input("> ")

    # rozvětvení na základě prvního slova
    match response.split():
        case ["quit"]:
            return "Quit"
        case ["list", ("employees" | "departments" | "rooms") as obj]:
            # rozvětvení na základě druhého slova
            match obj:
                case "employees":
                    return "List employees"
                case "departments":
                    return "List departments"
                case "rooms":
                    return "List rooms"
        case ["info", subject]:
            return f"Info about subject '{subject}'"
        case _:
            return "Wrong command"


print(perform_command())
