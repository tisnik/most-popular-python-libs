# Based on code snippets mentioned there:
# https://stackoverflow.com/questions/11141387/given-a-python-pyc-file-is-there-a-tool-that-let-me-view-the-bytecode

# Original authors:
# https://stackoverflow.com/users/6003870/padymko
# https://stackoverflow.com/users/5065946/powersource97

import sys
import struct
import marshal
import binascii
import time
import dis
import platform
import types

def view_pyc_file(path):
    """Read and display a content of the Python`s bytecode in a pyc-file."""

    with open(path, 'rb') as file:

        magic = file.read(4)
        bit_field = None
        timestamp = None
        hashstr = None
        size = None

        if sys.version_info.major == 3 and sys.version_info.minor >= 7:
            bit_field = int.from_bytes(file.read(4), byteorder=sys.byteorder)
            if 1 & bit_field == 1:
                hashstr = file.read(8)
            else:
                timestamp = file.read(4)
                size = file.read(4)
                size = struct.unpack('I', size)[0]
        elif sys.version_info.major == 3 and sys.version_info.minor >= 3:
            timestamp = file.read(4)
            size = file.read(4)
            size = struct.unpack('I', size)[0]
        else:
            timestamp = file.read(4)

        code = marshal.load(file)

    magic = binascii.hexlify(magic).decode('utf-8')
    timestamp = time.asctime(time.localtime(struct.unpack('I', timestamp)[0]))

    dis.disassemble(code)

    print('-' * 80)

    for i, const in enumerate(code.co_consts):
        print(i, "\t"+str(const) + "\t" + str(type(const)))
        # constant pool contains function/method bytecode, so let's try to disassemble it
        try:
            dis.disassemble(const)
        except:
            pass

    print('-' * 80)
    print(
        'Python version: {}\nMagic code: {}\nTimestamp: {}\nSize: {}\nHash: {}\nBitfield: {}'
        .format(platform.python_version(), magic, timestamp, size, hashstr, bit_field)
    )

if __name__ == '__main__':
    view_pyc_file(sys.argv[1])
