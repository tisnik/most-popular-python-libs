#
#  (C) Copyright 2023  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

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
