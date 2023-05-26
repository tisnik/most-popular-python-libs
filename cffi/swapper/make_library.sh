gcc -Wall -ansi -c -fPIC swapper.c -o swapper.o

gcc -shared -Wl,-soname,libswapper.so -o libswapper.so swapper.o
