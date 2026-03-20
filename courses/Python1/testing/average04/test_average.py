"""Implementace jednotkových testů."""

from average import average


def test_average_basic():
    """Otestování výpočtu průměru."""
    result = average([1, 2])
    expected = 1.5
    assert result == expected, "Očekávaná hodnota {}, vráceno {}".format(
        expected, result
    )


def test_average_empty_list():
    """Otestování výpočtu průměru."""
    result = average([])
    expected = 0.0
    assert result == expected, "Očekávaná hodnota {}, vráceno {}".format(
        expected, result
    )
