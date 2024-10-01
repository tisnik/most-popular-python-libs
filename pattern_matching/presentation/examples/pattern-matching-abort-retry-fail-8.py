# Strukturální pattern matching:
# - rozhodování realizované pattern matchingem

print("Not ready reading drive A")


def abort_retry_fail():
    # získání odpovědi od uživatele
    # a rozhodnutí o provedené operaci
    match input("Abort, Retry, Fail? "):
        case "a" | "A":
            return "Abort"
        case "r" | "R":
            return "Retry"
        case "f" | "F":
            return "Fail"
        case _ as x:
            return f"Wrong response {x}"


print(abort_retry_fail())
