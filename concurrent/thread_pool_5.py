#
#  (C) Copyright 2022  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

from concurrent.futures.thread import ThreadPoolExecutor
import time


def worker(threadName, delay, n):
    result = 0

    for counter in range(1, n + 1):
        time.sleep(delay)
        print("{}: {}/{} - {}".format(threadName, counter, n, time.ctime(time.time())))
        result += delay

    print("{}: DONE!".format(threadName))
    return result


workers = 10

results = []

with ThreadPoolExecutor(max_workers=3) as executor:
    for w in range(workers):
        result = executor.submit(worker, "Thread-{}".format(w + 1), 0.5 + w / 10.0, 10)
        results.append(result)
        print(w, result)


print("Computing finished")

for result in results:
    print(result.result())

print("Done!")
