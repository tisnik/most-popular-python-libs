n = 10000

def test_range(n):
    for _i in range(n):
        pass

def test_xrange(n):
    for _i in xrange(n):
        pass

test_range(n)
test_xrange(n)
