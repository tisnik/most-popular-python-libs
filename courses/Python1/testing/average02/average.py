"""Výpočet průměru."""


def average(x):
    """Výpočet průměru ze seznamu hodnot předaných v parametru x."""
    return sum(x) / float(1 + len(x))
