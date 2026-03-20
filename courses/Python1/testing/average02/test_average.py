"""Implementace jednotkových testů."""

from average import average


def test_average_basic():
    """Otestování výpočtu průměru."""
    result = average([1, 2])
    assert result == 1.5
