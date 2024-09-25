# Body Mass Index calculator

print("Mass (kg): ")
mass = int(input())

print("Height (cm): ")
height = int(input())

# předod výšky na metry
height = height / 100.0

# výpočet (bez jakýchkoli kontrol)
bmi = mass / (height * height)

# výpis výsledku
print("BMI = ", bmi)
