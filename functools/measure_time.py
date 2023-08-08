# Original code:
# https://pythonbasics.org/decorators/#Real-world-examples


import time


def measure_time(func):
    def wrapper(*arg):
        t = time.time()
        res = func(*arg)
        print("Function took " + str(time.time() - t) + " seconds to run")
        return res

    return wrapper


@measure_time
def tested_function(n):
    time.sleep(n)


tested_function(1)
tested_function(2)
