import struct

# uložení hodnoty bajtu do binární struktury
bytes = struct.pack("b", 42)
print("Serialized:  ", bytes.hex(" ", 1))

# přečtení binární struktury, která obsahuje jediný bajt
s = struct.Struct("b")
from_struct = s.unpack(bytes)

# vypsat přečtenou hodnotu
print("Deserialized:", from_struct)
print("Type:        ", type(from_struct))
