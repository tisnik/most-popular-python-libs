#!/usr/bin/env python3

from multiprocessing import Process
import time


def worker(name):
    print("hello", name)
    time.sleep(5)
    print("done", name)


def main():
    ps = [Process(target=worker, args=(name,)) for name in ("foo", "bar", "baz", "other")]

    for p in ps:
        p.start()

    for p in ps:
        p.join()


if __name__ == '__main__':
    print("Running main")
    main()
