def compute_bmi(mass, height):
    height = height / 100.0
    bmi = mass / (height * height)
    return bmi
