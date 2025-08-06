import sys
from ctypes import (
    CDLL,
    c_int,
    c_uint,
    Structure,
    pointer,
    POINTER,
)


class MyStruct(Structure):
    _fields_ = [
        ("a", c_uint),
        ("b", c_uint),
        ("c", c_uint),
    ]


def main():
    # try to load dynamically linked library
    bitfield = CDLL("./bitfield.so")

    my_struct = MyStruct(1, 2, 3)

    # pass my value
    print("Pass struct by value:")
    bitfield.test_pass_by_value(my_struct)

    print()

    # pass my reference
    print("Pass struct by reference:")
    bitfield.test_pass_by_reference(pointer(my_struct))


if __name__ == "__main__":
    main()


# finito
