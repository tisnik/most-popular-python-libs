#!/usr/bin/env python3

from multiprocessing import Process
import time


def worker(name, dictionary):
    dictionary[name] = "ok"
    print("hello", name)
    time.sleep(5)
    print("done", name)


def main():
    d = {}

    ps = []

    for name in ("foo", "bar", "baz", "other"):
        p = Process(target=worker, args=(name, d))
        p.start()
        ps.append(p)

    for p in ps:
        p.join()

    print(d)


if __name__ == "__main__":
    print("Running main")
    main()
