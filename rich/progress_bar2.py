#
#  (C) Copyright 2021  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

from rich.progress import track

# originální kód lze nalézt na adrese:
# http://www.rosettacode.org/wiki/Sieve_of_Eratosthenes#Using_array_lookup
def primes2(limit):
    """Výpočet seznamu prvočísel až do zadaného limitu."""
    is_prime = [False] * 2 + [True] * (limit - 1)
    for n in track(range(int(limit ** 0.5 + 1.5))):
        if is_prime[n]:
            for i in range(n * n, limit + 1, n):
                is_prime[i] = False
    return [i for i, prime in enumerate(is_prime) if prime]


print(primes2(100))
