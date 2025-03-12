"""Implementace jednotkových testů."""

import pytest

from average import average


testdata = [
    ((1, 1), 1),
    ((1, 2), 1.5),
    ((0, 1), 0.5),
    ((1, 2, 3), 2.0),
    ((0, 10), 0.5),
]


@pytest.mark.parametrize("values,expected", testdata)
def test_average_basic_1(values, expected):
    """Otestování výpočtu průměru."""
    result = average(values)
    assert result == expected, "Očekávaná hodnota {}, vráceno {}".format(
        expected, result
    )


@pytest.mark.parametrize(
    "values,expected", testdata, ids=["1,1", "1,2", "0,1", "1,2,3", "0,10"]
)
def test_average_basic_2(values, expected):
    """Otestování výpočtu průměru."""
    result = average(values)
    assert result == expected, "Očekávaná hodnota {}, vráceno {}".format(
        expected, result
    )


@pytest.mark.parametrize(
    "values,expected",
    [
        pytest.param((1, 1), 1),
        pytest.param((1, 2), 1.5),
        pytest.param((0, 1), 0.5),
        pytest.param((1, 2, 3), 2.0),
        pytest.param((0, 10), 0.5),
        pytest.param((), 0),
    ],
)
def test_average_basic_3(values, expected):
    """Otestování výpočtu průměru."""
    result = average(values)
    assert result == expected, "Očekávaná hodnota {}, vráceno {}".format(
        expected, result
    )


def test_average_empty_list_1():
    """Otestování výpočtu průměru pro prázdný vstup."""
    with pytest.raises(ZeroDivisionError) as excinfo:
        result = average([])


def test_average_empty_list_2():
    """Otestování výpočtu průměru pro prázdný vstup."""
    with pytest.raises(Exception) as excinfo:
        result = average([])
    # poměrně křehký způsob testování!
    assert excinfo.type == ZeroDivisionError
    assert str(excinfo.value) == "float division by zero"
