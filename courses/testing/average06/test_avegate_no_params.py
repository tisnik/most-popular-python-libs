"""Implementace jednotkových testů."""


from average import average


def test_average_basic_more_checks():
    """Otestování výpočtu průměru."""
    inputs = ((0, 0), (1, 0), (1, 1), (1, 2))
    expected_results = (0, 0.5, 1, 1.5)

    for input, expected in zip(inputs, expected_results):
        result = average(input)
        assert result == expected, "Očekávaná hodnota {}, vráceno {}".format(
            expected, result
        )
