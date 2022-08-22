#
# Modul s jedinou funkci pro otestovani
# zakladnich vlastnosti bajtkodu jazyka Lua
# prekladu programove smycky typu while.
#
 
def loop(x):
    while x > 0:
        x = x - 1
    return x
 
 
#
# Vse je nutne otestovat.
#
def main():
    print(loop(10))
 
#
# Vypsani bajkkodu testovane funkce
#
def disassemble():
    from dis import dis
 
    print("\nloop:")
    dis(loop)
 
main()
 
disassemble()
