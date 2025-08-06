.PHONY: all clean

CC=gcc
CFLAGS=-Wall -pedantic -ansi -O2

all: renderer.so

clean:
	rm -f renderer.so

renderer.so:	renderer.c renderer.h
	$(CC) $(CFLAGS) -shared -Wl,-soname,renderer -o $@ -fPIC $<
