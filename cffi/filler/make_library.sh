gcc -Wall -ansi -c -fPIC filler.c -o filler.o

gcc -shared -Wl,-soname,libfiller.so -o libfiller.so filler.o
