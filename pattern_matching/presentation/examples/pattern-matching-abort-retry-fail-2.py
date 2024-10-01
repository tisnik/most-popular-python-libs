# Strukturální pattern matching:
# - rozhodování realizované slovníkem (mapou)
#   namísto pattern matchingu

print("Not ready reading drive A")


def abort_retry_fail():
    # získání odpovědi od uživatele
    response = input("Abort, Retry, Fail? ")

    # odpovědi a odpovídající operace
    commands = {
            "a": "Abort",
            "r": "Retry",
            "f": "Fail",
            }

    # rozhodnutí o provedené operaci na základě odpovědi
    return commands.get(response, "Wrong response")


print(abort_retry_fail())
