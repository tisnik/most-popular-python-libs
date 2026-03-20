def compute_bmi(mass, height):
    """Vlastní výpočet BMI za základě hmotnosti a výšky."""
    height = height / 100.0
    bmi = mass / (height * height)
    return bmi
