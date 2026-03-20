"""Implementace jednotkových testů."""

from primes import primes2


def test_primes_10():
    """Otestování výpočtu seznamu prvočísel až do limitu 10."""
    # získat seznam prvočísel až do limitu 10
    p = primes2(10)
    # testy lze dále rozšiřovat
    assert 2 in p
    assert 10 not in p


def test_primes_0():
    """Otestování výpočtu seznamu prvočísel do limitu 0."""
    p = primes2(0)
    # otestujeme, zda je sekvence prázdná (není zcela přesné)
    assert not p


def test_primes_2():
    """Otestování výpočtu seznamu prvočísel do limitu 2."""
    p = primes2(2)
    # otestujeme, zda sekvence obsahuje pouze hodnotu 2
    assert 2 in p
    assert p == [2]
