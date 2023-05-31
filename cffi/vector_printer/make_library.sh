gcc -Wall -ansi -c -fPIC vector_printer.c -o vector_printer.o

gcc -shared -Wl,-soname,libvprinter.so -o libvprinter.so vector_printer.o
