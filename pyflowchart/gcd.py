x = int(input("x= "))
y = int(input("y= "))

while x != y:
    if x > y:
        x = x - y
    if x < y:
        y = y - x

print("gcd=", x)
