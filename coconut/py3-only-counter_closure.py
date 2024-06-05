# Compiled Coconut: -----------------------------------------------------------

def createCounter():  #1 (line in Coconut source)
    counter = 0  #2 (line in Coconut source)
    def nextValue():  #3 (line in Coconut source)
        nonlocal counter  #4 (line in Coconut source)
        counter += 1  #5 (line in Coconut source)
        return counter  #6 (line in Coconut source)

    return nextValue  #7 (line in Coconut source)




def main():  #11 (line in Coconut source)
    counter1 = createCounter()  #12 (line in Coconut source)
    counter2 = createCounter()  #13 (line in Coconut source)
    for i in range(1, 11):  #14 (line in Coconut source)
        result1 = counter1()  #15 (line in Coconut source)
        result2 = counter2()  #16 (line in Coconut source)
        print("Iteration #%d" % i)  #17 (line in Coconut source)
        print("    Counter1: %d" % result1)  #18 (line in Coconut source)
        print("    Counter2: %d" % result2)  #19 (line in Coconut source)



main()  #22 (line in Coconut source)
