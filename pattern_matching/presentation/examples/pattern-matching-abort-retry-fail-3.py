# Strukturální pattern matching:
# - rozhodování realizované pattern matchingem

print("Not ready reading drive A")


def abort_retry_fail():
    # získání odpovědi od uživatele
    response = input("Abort, Retry, Fail? ")

    # rozhodnutí o provedené operaci na základě odpovědi
    match response:
        case "a":
            return "Abort"
        case "r":
            return "Retry"
        case "f":
            return "Fail"
        case _:
            return "Wrong response"


print(abort_retry_fail())
