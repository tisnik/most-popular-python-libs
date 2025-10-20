from concurrent import interpreters

interp = interpreters.create()

for interpreter in interpreters.list_all():
    print(interpreter)
