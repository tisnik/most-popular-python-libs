from pycrunch_trace.client.api import trace

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

"""Výpočet faktoriálu."""


@trace
def factorial(n):
    """Rekurzivní výpočet faktoriálu."""
    assert isinstance(n, int), "Integer expected"

    if n < 0:
        return None
    if n == 0:
        return 1
    result = n * factorial(n - 1)

    assert isinstance(result, int), "Internal error in factorial computation"
    return result


def main():
    for n in range(11):
        print(n, factorial(n))


if __name__ == "__main__":
    main()
