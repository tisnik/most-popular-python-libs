def dummyAdder(delta):
    def add(n):
        return delta + n
    return add



#
# Spusteni testu.
#
def main():
    adder1 = dummyAdder(0)
    adder2 = dummyAdder(42)
    for i in range(1,11):
        result1 = adder1(i)
        result2 = adder2(i)
        print("Iteration #%d" % i)
        print("    Adder1: %d" % result1)
        print("    Adder2: %d" % result2)


main()
