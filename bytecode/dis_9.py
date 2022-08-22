#
# Modul s jedinou funkci pro otestovani
# zakladnich vlastnosti bajtkodu jazyka Lua
# prekladu programove smycky typu do-while.
# (presneji receno jeji emulace)
#
 
def loop(x):
    while True:
        x = x - 1
        if x <= 0: break
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
