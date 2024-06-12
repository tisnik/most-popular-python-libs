#!/usr/bin/env python3

"""Vstupní bod do testované aplikace."""

from primes import find_primes

if __name__ == "__main__":
    # pouze se ujistíme, že lze spustit funkci primes2
    print(find_primes(1000))
