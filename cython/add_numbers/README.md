# Content of the subdirectory `add_numbers`

More variants of the function to add two numbers:

```
add_numbers_1.py
```

Pure Python implementation.


```
add_numbers_2.pyx
```

Cython implementation using `cdef`


```
add_numbers_3.pyx
```

Cython implementation using `cdef` and type hints.


```
add_numbers_4.pyx
```

Cython implementation using `cdef`, return value type declaration, and type hints.

```
add_numbers_5.pyx
```

Dtto, but using `nogil` clausule.

```
add_numbers_6.pyx
```

Dtto, but with `print` built-in function.


```
add_numbers_7.pyx
```

Use `printf` instead of `print`

```
add_numbers_dis.py
```

Disassembly (bytecode) for pure Python variant.

```
Makefile
```

To build binaries from Cython sources.
