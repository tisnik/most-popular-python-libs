.PHONY: all clean

CC=gcc
CFLAGS=-Wall -pedantic -ansi -O2

all: bitfield.so

clean:
	rm -f bitfield.so

bitfield.so:	bitfield.c
	$(CC) $(CFLAGS) -shared -Wl,-soname,bitfield -o $@ -fPIC $<
