from concurrent import interpreters

interp = interpreters.create()

def run():
    print("Hello from new interpreter")

print("Executing call()")
interp.call(run)

print("Hello from the original interpreter")
