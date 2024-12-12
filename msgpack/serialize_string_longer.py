import msgpack

value = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."

with open("longer_string.bin", "wb") as outfile:
    packed = msgpack.packb(value)
    outfile.write(packed)
