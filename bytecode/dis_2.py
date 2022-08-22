#
# Modul s nekolika jednoduchymi funkcemi
# pro otestovani zakladnich vlastnosti bajtkodu jazyka Python
# prekladu Booleovskych vyrazu.
#
 
def vyraz1(x):
    result = not x
    return result
 
def vyraz2(x, y):
    result = x and y
    return result
 
def vyraz3(x, y):
    result = x or y
    return result
 
def vyraz4(x, y):
    result = x ^ y
    return result
 
def vyraz5(x, y, z):
    result = x or y and z
    return result
 
def vyraz6(x, y, z, w):
    result = (x or y) and (z or w)
    return result
 
 
#
# Vse je nutne otestovat.
#
def main():
    print(vyraz1(True))
    print(vyraz2(True, False))
    print(vyraz3(True, False))
    print(vyraz4(True, False))
    print(vyraz5(True, False, True))
    print(vyraz6(True, False, True, False))
 
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
 
main()
 
disassemble()
