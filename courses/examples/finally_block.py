#!/usr/bin/python

try:
    file = open("testfile", "w")
    file.write("test")
except IOError:
    print("soubor nelze otevrit pro zapis")
else:
    print("zapis uspesne proveden")
finally:
    file.close()
