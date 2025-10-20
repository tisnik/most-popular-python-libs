from concurrent import interpreters

for interpreter in interpreters.list_all():
    print(interpreter)
