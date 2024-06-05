# Compiled Coconut: -----------------------------------------------------------

try:  #1 (line in Coconut source)
    _coconut_sys_0 = sys  # type: ignore  #1 (line in Coconut source)
except _coconut.NameError:  #1 (line in Coconut source)
    _coconut_sys_0 = _coconut_sentinel  #1 (line in Coconut source)
sys = _coconut_sys  #1 (line in Coconut source)
if sys.version_info >= (3, 4):  #1 (line in Coconut source)
    import asyncio  #1 (line in Coconut source)
else:  #1 (line in Coconut source)
    import trollius as asyncio  #1 (line in Coconut source)
if _coconut_sys_0 is not _coconut_sentinel:  #1 (line in Coconut source)
    sys = _coconut_sys_0  #1 (line in Coconut source)


@_coconut.asyncio.coroutine  #4 (line in Coconut source)
def task():  #4 (line in Coconut source)
    print("task started")  #5 (line in Coconut source)
    (yield _coconut.asyncio.From(asyncio.sleep(5)))  #6 (line in Coconut source)
    print("task finished")  #7 (line in Coconut source)



    if False:  #10 (line in Coconut source)
        yield  #10 (line in Coconut source)
def main():  #10 (line in Coconut source)
    task1 = asyncio.create_task(task())  #11 (line in Coconut source)
    print("task created")  #12 (line in Coconut source)

    (yield _coconut.asyncio.From(task1))  #14 (line in Coconut source)

    print("done")  #16 (line in Coconut source)



main()  #19 (line in Coconut source)
