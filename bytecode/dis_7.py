#
# Modul s jedinou funkci pro otestovani
# zakladnich vlastnosti bajtkodu jazyka Lua
# prekladu programove smycky typu while.
#
 
def loop(x, y):
    while x > 0:
        x = x - 1
        y = y * 2
    return y
 
 
#
# Vse je nutne otestovat.
#
def main():
    print(loop(10, 1))
 
def disassemble():
    from dis import dis
 
    print("\nloop:")
    dis(loop)
 
main()
 
disassemble()
