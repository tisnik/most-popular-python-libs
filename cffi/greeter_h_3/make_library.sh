gcc -Wall -ansi -c -fPIC greeter.c -o greeter.o

gcc -shared -Wl,-soname,libgreeter.so -o libgreeter.so greeter.o
