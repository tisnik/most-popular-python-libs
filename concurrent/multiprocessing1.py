#!/usr/bin/env python3

from multiprocessing import Process


def worker(name):
    print("hello", name)


def main():
    p = Process(target=worker, args=("foo",))
    p.start()
    p.join()


if __name__ == "__main__":
    print("Running main")
    main()
