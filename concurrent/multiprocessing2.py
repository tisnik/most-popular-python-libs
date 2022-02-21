#!/usr/bin/env python3

from multiprocessing import Process
import time


def worker(name):
    print("hello", name)
    time.sleep(5)
    print("done", name)


def main():
    ps = []

    for name in ("foo", "bar", "baz", "other"):
        p = Process(target=worker, args=(name,))
        p.start()
        ps.append(p)

    for p in ps:
        p.join()


if __name__ == "__main__":
    print("Running main")
    main()
