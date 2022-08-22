#
# Modul s nekolika jednoduchymi funkcemi
# pro otestovani zakladnich vlastnosti bajtkodu jazyka Python
# prekladu aritmetickych vyrazu.
#
 
def vyraz1(x, y):
    result = x + y
    return result
 
 
def vyraz2(x, y):
    result = x - y
    return result
 
 
def vyraz3(x, y):
    result = x * y
    return result
 
 
def vyraz4(x, y):
    result = x / y
    return result
 
 
def vyraz5(x, y):
    result = x % y
    return result
 
 
def vyraz6(x, y, z):
    result = x + y * z
    return result
 
 
def vyraz7(x, y, z, w):
    result = x + y * z + w
    return result
 
 
def vyraz8(x, y, z, w):
    result = 2 * (x + y) * (z + w) * ((x + z) / (y + w))
    return result
 
 
#
# Vse je nutne otestovat.
#
def main():
    print(vyraz1(4, 3))
    print(vyraz2(4, 3))
    print(vyraz3(4, 3))
    print(vyraz4(4, 3))
    print(vyraz5(4, 3))
    print(vyraz6(4, 3, 2))
    print(vyraz7(4, 3, 2, 1))
    print(vyraz8(4, 3, 2, 1))
 
def disassemble():
    from dis import dis
 
    print("\nvyraz1:")
    dis(vyraz1)
 
    print("\nvyraz2:")
    dis(vyraz2)
 
    print("\nvyraz3:")
    dis(vyraz3)
 
    print("\nvyraz4:")
    dis(vyraz4)
 
    print("\nvyraz5:")
    dis(vyraz5)
 
    print("\nvyraz6:")
    dis(vyraz6)
 
    print("\nvyraz7:")
    dis(vyraz7)
 
    print("\nvyraz8:")
    dis(vyraz8)
 
main()
 
disassemble()
