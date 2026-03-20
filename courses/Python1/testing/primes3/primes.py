"""Výpočet seznamu prvočísel až do zadaného limitu."""

# originální kód lze nalézt na adrese:
# http://www.rosettacode.org/wiki/Sieve_of_Eratosthenes#Odds-only_version_of_the_array_sieve_above


def primes2(limit):
    """Výpočet seznamu prvočísel až do zadaného limitu."""
    # okrajový případ
    if limit < 2:  # pragma: no cover
        return []

    # druhý případ - 2 je speciálním prvočíslem
    if limit < 3:  # pragma: no cover
        return [2]

    lmtbf = (limit - 3) // 2

    # naplnění tabulky, která se bude prosívat
    buf = [True] * (lmtbf + 1)

    # vlastní prosívání
    for i in range((int(limit ** 0.5) - 3) // 2 + 1):
        if buf[i]:
            p = i + i + 3
            s = p * (i + 1) + i
            buf[s::p] = [False] * ((lmtbf - s) // p + 1)

    # vytvoření seznamu prvočísel
    return [2] + [i + i + 3 for i, v in enumerate(buf) if v]
