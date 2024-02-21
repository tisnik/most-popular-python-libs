.PHONY: all clean

CC=gcc
CFLAGS=-Wall -pedantic -ansi

all: renderer.so

clean:
	rm -f renderer.so

renderer.so:	renderer.c
	$(CC) $(CFLAGS) -shared -Wl,-soname,renderer -o $@ -fPIC $<
