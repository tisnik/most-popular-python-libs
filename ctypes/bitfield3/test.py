from ctypes import (
    CDLL,
    Structure,
    c_uint,
    pointer,
)


class MyStruct(Structure):
    _fields_ = [
        ("a", c_uint, 5),
        ("b", c_uint, 6),
        ("c", c_uint, 7),
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
