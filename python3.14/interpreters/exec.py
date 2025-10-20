from concurrent import interpreters

interp = interpreters.create()

print("Executing run()")
interp.exec(open("hello.py").read())

print("Hello from the original interpreter")
