gcc -Wall -ansi -c -fPIC adder.c -o adder.o

gcc -shared -Wl,-soname,libadder.so -o libadder.so adder.o
