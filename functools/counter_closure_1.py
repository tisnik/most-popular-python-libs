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

def createCounter():
    counter = 0
    def next():
        counter += 1
        return counter
    return next



#
# Spusteni testu.
#
def main():
    counter1 = createCounter()
    counter2 = createCounter()
    for i in range(1,11):
        result1 = counter1()
        result2 = counter2()
        print("Iteration #%d" % i)
        print("    Counter1: %d" % result1)
        print("    Counter2: %d" % result2)


main()
