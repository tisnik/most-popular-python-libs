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

    for name in ("foo", "bar", "baz", "other"):
        worker(name, d)

    print(d)


if __name__ == "__main__":
    print("Running main")
    main()
