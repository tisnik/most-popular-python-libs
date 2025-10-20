from concurrent import interpreters

interp = interpreters.create()

def run():
    print("Hello from new interpreter")
    0/0

print("Executing run()")
interp.exec(run)

print("Hello from the original interpreter")
