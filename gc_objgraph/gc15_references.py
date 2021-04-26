import gc
import sys
import pprint


def foo(ref):
    """Function called during test."""
    bar(ref)


def bar(ref):
    """Function that retrieves and prints reference counts."""
    print(sys.getrefcount(ref))
    pprint.pprint(len(gc.get_referrers(ref)))
    pprint.pprint(gc.get_referrers(ref))


x = "Test!"
pprint.pprint(gc.get_referrers(x))
print()

foo(x)
