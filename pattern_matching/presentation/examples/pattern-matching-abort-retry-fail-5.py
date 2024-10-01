# Strukturální pattern matching:
# - použití rozhodovací konstrukce if-elif-else
# - podpora odpovědí psaných velkými i malými znaky

print("Not ready reading drive A")


def abort_retry_fail():
    # získání odpovědi od uživatele
    response = input("Abort, Retry, Fail? ")

    # rozhodnutí o provedené operaci na základě odpovědi
    if response in {"a", "A", "abort", "Abort", "ABORT"}:
        return "Abort"
    elif response in {"r", "R"}:
        return "Retry"
    elif response in {"f", "F"}:
        return "Fail"
    else:
        return "Wrong response"


print(abort_retry_fail())
