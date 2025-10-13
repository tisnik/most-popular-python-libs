"""Implementace jednotkových testů."""

import unittest

from primes import primes2


class TestStringMethods(unittest.TestCase):
    def test_primes_10(self):
        """Otestování výpočtu seznamu prvočísel až do limitu 10."""
        # získat seznam prvočísel až do limitu 10
        p = primes2(10)
        # testy lze dále rozšiřovat
        assert 2 in p
        assert 10 not in p

    def test_primes_100000(self):
        """Otestování výpočtu seznamu prvočísel až do limitu 100000."""
        # získat seznam prvočísel až do limitu 100000
        p = primes2(100000)
        # testy lze dále rozšiřovat
        assert 2 in p
        assert 10 not in p
        # hodnoty získány ze seznamu:
        # https://primes.utm.edu/lists/small/10000.txt
        assert 99989 in p
        assert 99991 in p

    def test_primes_0(self):
        """Otestování výpočtu seznamu prvočísel do limitu 0."""
        p = primes2(0)
        # otestujeme, zda je sekvence prázdná (není zcela přesné)
        assert not p

    def test_primes_should_fail(self):
        """Otestování výpočtu seznamu prvočísel do limitu 2."""
        p = primes2(2)
        assert p == [1, 2, 3]

    def test_primes_2(self):
        """Otestování výpočtu seznamu prvočísel do limitu 2."""
        p = primes2(2)
        # otestujeme, zda sekvence obsahuje pouze hodnotu 2
        assert 2 in p
        assert p == [2]


if __name__ == "__main__":
    unittest.main()
