# Strukturální pattern matching:
# - rozhodování realizované pattern matchingem
# - podpora odpovědí psaných velkými i malými znaky

print("Not ready reading drive A")


def abort_retry_fail():
    # získání odpovědi od uživatele
    response = input("Abort, Retry, Fail? ")

    # rozhodnutí o provedené operaci na základě odpovědi
    match response:
        case "a" | "A" | "abort" | "Abort" | "ABORT":
            return "Abort"
        case "r" | "R":
            return "Retry"
        case "f" | "F":
            return "Fail"
        case _:
            return "Wrong response"


print(abort_retry_fail())
