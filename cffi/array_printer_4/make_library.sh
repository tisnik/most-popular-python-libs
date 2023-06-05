gcc -Wall -ansi -c -fPIC array_printer.c -o array_printer.o

gcc -shared -Wl,-soname,libaprinter.so -o libaprinter.so array_printer.o
