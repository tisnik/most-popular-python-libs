#!/usr/bin/python
# vim: set fileencoding=utf-8

try:
    file = open("testfile", "w")
    file.write("test")
except IOError:
    print("soubor nelze otevrit pro zapis")
else:
    print("zapis uspesne proveden")
    file.close()
