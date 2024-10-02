# Strukturální pattern matching:
# - rozpoznání a zpracování příkazů zadaných uživatelem
# - nejjednodušší podoba pro víceslovní příkazy

def perform_command():
    # získat příkaz od uživatele
    response = input("> ")

    match response:
        case "quit":
            return "Quit"
        case "list employees":
            return "List employees"
        case "list departments":
            return "List departments"
        case "list rooms":
            return "List rooms"
        case _:
            return "Wrong command"


print(perform_command())
